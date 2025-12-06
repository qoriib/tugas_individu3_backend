from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review_text = db.Column(db.String(500), nullable=False)
    sentiment = db.Column(db.String(20), nullable=False)
    key_points = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f"<Review {self.id}>"
