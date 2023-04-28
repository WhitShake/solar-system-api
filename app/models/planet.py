from app import db

class Planet(db.Model):
    id = db.Column(
            db.Integer, 
            primary_key=True, 
            autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    mass = db.Column(db.Integer, nullable=False)