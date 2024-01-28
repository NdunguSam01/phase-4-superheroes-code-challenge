from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    serialize_rules=('-powers.hero',)
    serialize_rules=('-hero_powers.hero',)

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    super_name=db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    #Secondary indicates the association table that connects the Hero and Power tables
    powers=db.relationship("Power", secondary="heropowers", backref="hero", viewonly=True)
    hero_powers=db.relationship("HeroPower", backref="hero")

    def __repr__(self):
        return f"\nSuperhero name: {self.name}\nSuper name: {self.super_name}\nCreated at: {self.created_at}\n"

class Power(db.Model, SerializerMixin):

    __tablename__= "powers"

    serialize_rules=('-powers.power',)

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False, unique=True)
    description=db.Column(db.String, nullable=False) 
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    powers=db.relationship("HeroPower", backref="power")

    @validates("description")
    def  validate_description(self, key, description):
        if len(description) < 20:
            raise ValueError("Description cannot be empty and must be at least 20 characters long")
        
        return description

    def __repr__(self):
        return f"\nPower name: {self.name}\nDescription: {self.description}\nCreated at: {self.created_at}\n"

class HeroPower(db.Model, SerializerMixin):

    __tablename__= "heropowers"
    
    id=db.Column(db.Integer, primary_key=True)
    strength=db.Column(db.String)
    hero_id=db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id=db.Column(db.Integer, db.ForeignKey('powers.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    @validates("strength")
    def  validate_strength(self, key, strength):
        valid_strngths=['Strong', 'Weak', 'Average']

        if strength not in valid_strngths:
            raise ValueError("Strength must be Strong, Weak or Average")
        
        return strength

    def __repr__(self):
        return f"\nStrength: {self.strength}\nSuper Hero: {self.hero}\nPower name: {self.power}\n"