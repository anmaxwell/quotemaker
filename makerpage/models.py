from datetime import datetime
from makerpage import db

class QuoteForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quotetext = db.Column(db.Text, nullable=False)
    classify = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f"Quote('{self.id}', '{self.quotetext})"
