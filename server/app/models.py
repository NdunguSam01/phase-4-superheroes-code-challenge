from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False, unique=True)
    super_name=db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #Secondary indicates the association table that connects the Hero and Power tables
    powers=db.relationship("Power", secondary= "heropowers", back_populates="heroes")

    def __repr__(self):
        return f"Superhero name: {self.name}\nSuper name: {self.super_name}\nCreated at: {self.created_at}"

class Power(db.Model, SerializerMixin):

    __tablename__= "powers"

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False, unique=True)
    description=db.Column(db.String, nullable=False) 
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #Secondary indicates the association table that connects the Hero and Power tables
    heroes=db.relationship("Heroes", secondary= "heropowers", back_populates="powers")

    @validates("description")
    def  validate_description(self, key, description):
        if not description and len(description) < 20:
            raise ValueError("Description cannot be empty and must be at least 20 characters long")

    def __repr__(self):
        return f"Power name: {self.name}\nDescription: {self.description}\nCreated at: {self.created_at}"

class HeroPower(db.Model, SerializerMixin):

    __tablename__= "heropowers"

    id=db.Column(db.Integer, primary_key=True)
    strength=db.Column(db.String, nullable=False)
    hero_id=db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id=db.Column(db.Integer, db.ForeignKey('powers.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #Creating attributes in the heropowers table that will reference the Hero and Powers tables
    hero=db.relationship("Hero", back_populates="powers")
    power=db.relationship("Power",back_populates="heroes")

    @validates("strength")
    def  validate_strength(self, key, strength):
        valid_strngths=['Strong', 'Weak', 'Average']

        if strength not in valid_strngths:
            raise ValueError("Strength must be Strong, Weak or Average")

    def __repr__(self):
        return f"Strength: {self.strength}\nSuper Hero: {self.hero}\nPower name: {self.power}"