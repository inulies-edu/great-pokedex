from instance.db import db


class Pokemon(db.Model):
    __tablename__ = 'pokemon'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False, unique=True)
    image = db.Column(db.String(255), nullable=False, unique=True)
    primary_type = db.Column(db.String(10), nullable=False)
    secondary_type = db.Column(db.String(10), nullable=False)
    
    def to_json(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'image' : self.image,
            'primary-type' : self.primary_type,
            'secondary-type' : self.secondary_type
        }

