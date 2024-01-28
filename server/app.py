#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from models import db, Hero, HeroPower, Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Superheroes code challenge</h1>'


@app.route("/heroes")
def heroes():

    all_heroes=Hero.query.all()
    response=[]
    for hero in all_heroes:
        hero={
            "id": hero.id,  
            "name": hero.name,
        }
        response.append(hero)

    return make_response(jsonify(response), 200)
    
@app.route("/heroes/<int:id>")
def hero_by_id(id):
    
    hero=Hero.query.filter(Hero.id == id).first()

    if not hero:
        response={
            "error":"Hero not found"
        }
        return make_response(jsonify(response),404)
    else:        
        print(hero)
        for power in hero.powers:
            hero_dict={
                f"id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name,
                "powers": [
                    {
                        "id": power.id,
                        "name": power.name,
                        "description": power.description
                    }
                ]
            }
            response= make_response(jsonify(hero_dict), 200)
            return response
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
