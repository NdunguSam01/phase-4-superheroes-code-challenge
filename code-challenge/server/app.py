#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import db, Hero, HeroPower, Power
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
api=Api(app)
db.init_app(app)

@app.route('/')
def home():
    return '<h1>Superheroes code challenge</h1>'


class Heroes(Resource):
    def get(self):

        all_heroes=Hero.query.all()
        response=[]
        for hero in all_heroes:
            hero={
                "id": hero.id,  
                "name": hero.name,
            }
            response.append(hero)

        return make_response(jsonify(response), 200)

api.add_resource(Heroes, "/heroes")

class HeroById(Resource):

    def get(self, id):
        hero=Hero.query.filter(Hero.id == id).first()

        if not hero:
            response={
                "error":"Hero not found"
            }
            return make_response(jsonify(response),404)
        
        else:        
            response=[]
            response.append({
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name,
                "powers": []
            })
            for power in hero.powers:
                print(power)
                power_dict={
                    "id": power.id,
                    "name": power.name,
                    "description": power.description
                }
                response[0]["powers"].append(power_dict)
            
            return make_response(jsonify(response), 200)

api.add_resource(HeroById, "/heroes/<int:id>")
    
class Powers(Resource):

    def get(self):
        powers = Power.query.all()
        response=[]

        if not powers:
            response.append({"error": "Power not found"})
            return make_response(jsonify(response),404)
        else:
            for power in powers:
                power={
                    'id':power.id,
                    'name': power.name,
                    "description": power.description
                }
                response.append(power)
            return make_response(jsonify(response),200)
        
api.add_resource(Powers, "/powers")

class PowerByID(Resource):

    def get(self, id):

        power=Power.query.filter(Power.id == id).first()

        if not power:
            response={
                "error":"Power not found"
            }
            return make_response(jsonify(response),404)
        
        else:        
            power_dict={
                    'id':power.id,
                    'name': power.name,
                    "description": power.description
                }
            
            return make_response(jsonify(power_dict), 200)
        
    def patch(self, id):

        power_to_patch=Power.query.filter(Power.id == id).first()

        if not power_to_patch:
            response={
                "error": "Power not found"
            }
            return make_response(jsonify(response), 404)
        
        elif power_to_patch:
            for attr in request.json:
                setattr(power_to_patch, attr, request.json[attr])

            db.session.add(power_to_patch)
            db.session.commit()
            
            return make_response(PowerByID().get(power_to_patch.id),200)

api.add_resource(PowerByID, "/powers/<int:id>")

class HeroPowers(Resource):

    def post(self):
        new_hero_power=HeroPower(
            strength=request.form["strength"],
            power_id=request.form["power_id"],
            hero_id=request.form["hero_id"]
        )

        if ValueError:
            response={
                "error": ["validation errors"]
            }
            return make_response(jsonify(response), 422)
        
        else:
            db.session.add(new_hero_power)
            db.session.commit()

            response=HeroById().get(new_hero_power.hero_id)
            print(response)
            return make_response(response, 201)

api.add_resource(HeroPowers, "/hero_powers")

if __name__ == '__main__':
    app.run(port=5555, debug=True)
