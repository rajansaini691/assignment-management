from django.test import TestCase
from .schemas import question_schema, answer_schema, assignment_schema

from jsonschema import validate
import jsonschema
import json

class AssignmentSchemaTestCase(TestCase):
    # TODO Test actual example assignment things instead of these tiny things

    def test_assignment_schema_accept_valid_json(self):
        test_assignment_json = "[]"
        test_assignment_dict = json.loads(test_assignment_json)
        validate(test_assignment_dict, schema=assignment_schema)

    def test_assignment_schema_reject_invalid_json(self):
        test_assignment_json = "["
        with self.assertRaises(json.decoder.JSONDecodeError):
            json.loads(test_assignment_json)

    def test_assignment_schema_reject_invalid_schema(self):
        test_assignment_json = "{}"
        with self.assertRaises(jsonschema.exceptions.ValidationError):
            test_assignment_dict = json.loads(test_assignment_json)
            validate(test_assignment_dict, schema=assignment_schema)

    def test_assignment_schema_accept_valid_assignment(self):
        test_assignment_data = [{
            'question': [
                {'type': 'TXT', 'content': 'What is the number after'},
                {'type': 'VAR', 'content': 'x'},
                {'type': 'TXT', 'content': '?'}],
            'answer': [
                {'choice': 'x + 42', 'correct': False},
                {'choice': 'x + 1', 'correct': True},
                {'choice': 'x - 1', 'correct': False},
                {'choice': 'x', 'correct': False}]}]

        # Ensure serialize -> parse preserves data
        test_assignment_json = json.dumps(test_assignment_data)
        test_assignment_dict = json.loads(test_assignment_json)

        validate(test_assignment_dict, schema=assignment_schema)
