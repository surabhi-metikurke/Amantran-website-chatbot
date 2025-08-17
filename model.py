from . import db

class TicketBooking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    tickets = db.Column(db.Integer)

    def __repr__(self):
        return f'<TicketBooking {self.user_name}>'
