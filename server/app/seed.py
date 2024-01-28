from app import app
from models import db, Hero, HeroPower, Power
from random import choice

if __name__ == "__main__":
    with app.app_context():
        
        powers=[]

        powers.append(Power(name="super strength", description="gives the wielder super-human strengths"))
        powers.append(Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"))
        powers.append(Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"))
        powers.append(Power(name="elasticity", description="can stretch the human body to extreme lengths"))

        db.session.add_all(powers)

        heroes=[]
        heroes.append(Hero(name="Kamala Khan", super_name="Ms. Marvel"))
        heroes.append(Hero(name="Doreen Green", super_name="Squirrel Girl"))
        heroes.append(Hero(name="Gwen Stacy", super_name="Spider-Gwen"))
        heroes.append(Hero(name="Janet Van Dyne", super_name="The Wasp"))
        heroes.append(Hero(name="Wanda Maximoff", super_name="Scarlet Witch"))
        heroes.append(Hero(name="Carol Danvers", super_name="Captain Marvel"))
        heroes.append(Hero(name="Jean Grey", super_name="Dark Phoenix"))
        heroes.append(Hero(name="Ororo Munroe", super_name="Storm"))
        heroes.append(Hero(name="Kitty Pryde", super_name="Shadowcat"))
        heroes.append(Hero(name="Elektra Natchios", super_name="Elektra"))

        db.session.add_all(heroes)

        strengths=["Strong", "Weak", "Average"]
        hero_powers=[]
        for n in range(20):
          hero_powers.append(HeroPower(strength=choice(strengths), hero=choice(heroes), power=choice(powers)))

        db.session.add_all(hero_powers)

        db.session.commit()