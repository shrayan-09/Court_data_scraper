from . import db
from datetime import datetime

class QueryLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case_type = db.Column(db.String(10))
    case_number = db.Column(db.String(20))
    filing_year = db.Column(db.String(10))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    raw_html = db.Column(db.Text)
    parsed_data = db.Column(db.JSON)
