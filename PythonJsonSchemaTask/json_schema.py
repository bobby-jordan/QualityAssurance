#  -*- coding: utf-8 -*-
#  ! python
"""This module is about json schema validation and unit test"""
import unittest
from jsonschema import validate
import jsonschema
import logging


def validate_invalid():
    """Unit test validate invalid"""
    if "price" != int:
        raise ValueError("Price must be a number, not a string")
    else:
        print("Price is a number")

def validate_valid():
    """Unit test validate valid"""
    if "price" == int:
        print("The object is valid")
    if var == 'string':
        print("The object is valid")

def validate_null():
    """Unit test for validation null"""
    if "price" == 0:
        raise ValueError("The object is null")

class TestJsonObjects(unittest.TestCase):
    """Test class JSON object"""

    # initialize the the schema object
    def setUp(self):
        self.schema = {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "price": {"type": "number"},
            },
        }

    # assertion if json is null
    def test_json_is_null(self):
        """Test class null json"""
        schema = self.schema
        assert_raises = self.assertRaises
        error = ValueError
        assert_raises(error, validate({"title": "Honey", "price": 0}, schema))

    # assertion if json is valid
    def test_json_is_valid(self):
        """Test class for valid json"""
        schema = self.schema
        error = None
        assert_equal = self.assertEqual
        assert_equal(error, validate({"title": "Eggs", "price": 10.99}, schema))

    # assertion if json is invalid
    def test_json_is_invalid(self):
        """Test class for invalid json"""
        schema = self.schema
        assert_raises = self.assertRaises
        error = jsonschema.exceptions.ValidationError
        assert_raises(error, validate, {"title": "Milk", "price": "string"}, schema)


if __name__ == '__main__':
    unittest.main(verbosity=2)
