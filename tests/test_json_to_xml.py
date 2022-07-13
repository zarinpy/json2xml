from json2xml import Json2Xml
import pytest


class TestJson2Xml:
    def test_json_to_xml(self):
        d = {
            "name": "John",
            "age": 30,
            "cars": [{"name": "Ford"}],
            "family": "johnson",
        }
        t = Json2Xml(d)
        assert str(t), '<name>John</name><age>30</age><cars><name>Ford</name></cars><family>johnson</family>'

    def test_json_to_xml_with_line_spacing(self):
        d = {
            "name": "John",
            "age": 30,
            "cars": [{"name": "Ford"}],
            "family": "johnson",
        }
        t = Json2Xml(d, line_spacing="  ")
        assert str(t), ('<?xml version="1.0" encoding="UTF-8"?><data>  <name>John</name>  <age>30</age>  <cars>    '
                        '<name>Ford</name>  </cars>  <family>johnson</family>  </data>')

    def test_json_to_xml_invalid_type_list(self):
        d = [1, 2, 3]
        with pytest.raises(ValueError):
            Json2Xml(d)

    def test_json_to_xml_invalid_type_str(self):
        d = "John"
        with pytest.raises(ValueError):
            Json2Xml(d)

    def test_json_to_xml_invalid_type_empty_str(self):
        d = ""
        with pytest.raises(ValueError):
            Json2Xml(d)
