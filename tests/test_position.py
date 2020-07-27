import unittest
from app import db
from main import application
from models.position import Position
import json
import os


class PositionTestCase(unittest.TestCase):
    """This class represents the Position test case"""

    def setUp(self):
        """Define test variables and initialize DB"""
        self.client = application.test_client
        self.position_json = {
          "latitudeE7": 488182212,
          "altitude": 88,
          "longitudeE7": 22446445,
          "timestampMs": "1562563557125",
          "verticalAccuracy": 6,
          "accuracy": 14
        }
        self.position: Position = Position(**self.position_json)
        with application.app_context():
            db.create_all()

    def test_position_creation_201(self):
        """Test api/positions can create a Position (POST request)"""

        # When
        res = self.client().post('api/positions', json=self.position_json)

        # Then
        self.assertEqual(res.status_code, 201)
        data = json.loads(res.data)
        self.assertEqual(data["latitudeE7"], self.position_json["latitudeE7"])
        self.assertEqual(data["altitude"], self.position_json["altitude"])
        self.assertEqual(data["longitudeE7"], self.position_json["longitudeE7"])
        self.assertEqual(data["timestampMs"], self.position_json["timestampMs"])
        self.assertEqual(data["verticalAccuracy"], self.position_json["verticalAccuracy"])
        self.assertEqual(data["accuracy"], self.position_json["accuracy"])

    def test_position_creation_400(self):
        """Test api/positions returns BAD REQUEST (POST request)"""

        # Given
        bad_position = {"some_field": "not valid data"}

        # When
        res = self.client().post('api/positions', json=bad_position)

        # Then
        self.assertEqual(res.status_code, 400)

    def test_position_get_by_id_200(self):
        """Test api/positions/{position_id} can retrieve a Position (GET request)"""

        # Given
        db.session.add(self.position)
        db.session.commit()

        # When
        res = self.client().get('api/positions/' + str(self.position.position_id))

        # Then
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data["position_id"], self.position.position_id)
        self.assertEqual(data["latitudeE7"], self.position.latitudeE7)
        self.assertEqual(data["altitude"], self.position.altitude)
        self.assertEqual(data["longitudeE7"], self.position.longitudeE7)
        self.assertEqual(data["timestampMs"], self.position.timestampMs)
        self.assertEqual(data["verticalAccuracy"], self.position.verticalAccuracy)
        self.assertEqual(data["accuracy"], self.position.accuracy)

    def test_position_get_by_id_404(self):
        """Test api/positions/{position_id} returns NOT FOUND (GET request)"""

        # When
        res = self.client().get('api/positions/2')

        # Then
        self.assertEqual(res.status_code, 404)

    def test_position_get_all_200(self):
        """Test api/positions returns positions (GET request)"""

        # Given
        db.session.add(self.position)
        db.session.commit()

        # When
        res = self.client().get('api/positions')

        # Then
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(len(data["positions"]), 1)

    def test_position_delete_200(self):
        """Test api/positions/{position_id} deletes Position (DELETE request)"""

        # Given
        db.session.add(self.position)
        db.session.commit()

        # When
        res = self.client().delete('api/positions/' + str(self.position.position_id))

        # Then
        self.assertEqual(res.status_code, 200)
        self.assertEqual(db.session.query(Position).count(), 0)

    def test_position_delete_404(self):
        """Test api/positions/{position_id} returns NOT FOUND (DELETE request)"""

        # When
        res = self.client().delete('api/positions/2')

        # Then
        self.assertEqual(res.status_code, 404)

    def tearDown(self):
        """teardown all initialized variables and delete DB SQLite file."""
        with application.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()
        os.remove(application.config['SQLALCHEMY_DATABASE_PATH'])
