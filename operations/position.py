"""Operations used by /positions API endpoints"""

from app import db
from connexion import NoContent
from models.position import Position, PositionSchema
from marshmallow import ValidationError
from typing import Tuple


def get(position_id: int) -> Tuple[dict, int]:
    """Gets position by ID from datastore

    Returns a tuple containing position and HTTP return code

    :param position_id: ID of position to return
    :type position_id: int

    :rtype: Tuple[dict, int]
    """

    position: Position = db.session.query(Position).get(position_id)
    if position is None:
        return NoContent, 404
    schema: PositionSchema = PositionSchema()
    data: dict = schema.dump(position)
    return data, 200


def get_all() -> Tuple[dict, int]:
    """Gets all positions from datastore

    Returns a tuple containing positions and HTTP return code

    :rtype: Tuple[dict, int]
    """

    schema: PositionSchema = PositionSchema(many=True)
    data: dict = schema.dump(db.session.query(Position))
    return {"positions": data}, 200


def create(new_position: dict) -> Tuple[dict, int]:
    """Adds new position to the datastore

    Returns a tuple containing added position and HTTP return code

    :param new_position: Dict containing new position data
    :type new_position: dict

    :rtype: Tuple[dict, int]
    """

    schema: PositionSchema = PositionSchema()
    # Validation done again because connexion doesn't filter properties not defined in yaml specs
    try:
        new_position: dict = schema.load(new_position)
    except ValidationError as err:
        return {"errors": err.messages}, 400
    new_position: Position = Position(**new_position)
    db.session.add(new_position)
    db.session.commit()
    return schema.dump(new_position), 201


def update(position_id: int, updated_position: dict) -> Tuple[dict, int]:
    """Updates an existing position in the datastore

    Returns a tuple containing updated position and HTTP return code

    :param position_id: ID of position to update
    :type position_id: int
    :param updated_position: Dict containing updated position data
    :type updated_position: dict

    :rtype: Tuple[dict, int]
    """

    position: Position = db.session.query(Position).get(position_id)
    if position is None:
        return NoContent, 404

    schema: PositionSchema = PositionSchema()
    try:
        updated_position: dict = schema.load(updated_position)
    except ValidationError as err:
        return {"errors": err.messages}, 400

    for key, val in updated_position.items():
        setattr(position, key, val)
    db.session.commit()

    return schema.dump(position), 200


def delete(position_id: int) -> Tuple[dict, int]:
    """Deletes an existing position in the datastore

    Returns HTTP return code

    :param position_id: ID of position to delete
    :type position_id: int

    :rtype: Tuple[dict, int]
    """
    position: Position = db.session.query(Position).get(position_id)
    if position is None:
        return NoContent, 404
    db.session.delete(position)
    db.session.commit()
    return NoContent, 200
