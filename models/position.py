"""SQLAlchemy model and schema definition for GPS Position"""

from app import db
from marshmallow import Schema, fields


class Position(db.Model):
    """SQLAlchemy model definition of GPS position"""
    __tablename__ = 'positions'
    position_id = db.Column(db.Integer, primary_key=True)
    latitudeE7 = db.Column(db.Integer, nullable=False)
    altitude = db.Column(db.Integer, nullable=False)
    longitudeE7 = db.Column(db.Integer, nullable=False)
    timestampMs = db.Column(db.String(15), nullable=False)
    verticalAccuracy = db.Column(db.Integer, nullable=False)
    accuracy = db.Column(db.Integer, nullable=False)


class PositionSchema(Schema):
    """Marshmallow Schema definition for Position class"""
    position_id = fields.Integer(dump_only=True)
    latitudeE7 = fields.Integer(required=True)
    altitude = fields.Integer(required=True)
    longitudeE7 = fields.Integer(required=True)
    timestampMs = fields.String(required=True)
    verticalAccuracy = fields.Integer(required=True)
    accuracy = fields.Integer(required=True)
