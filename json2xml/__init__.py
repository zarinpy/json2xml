import xml.etree.cElementTree as e
from typing import Any

__all__ = ["Json2Xml"]


class Json2Xml(object):
    def __init__(self, json_obj: Any, line_spacing: str = ""):
        head = """<?xml version="1.0" encoding="UTF-8"?><data>"""
        self.data = head + self._json2xml(json_obj, line_spacing) + "</data>"

    def _json2xml(self, json_obj, line_spacing):
        result_list = list()
        json_obj_type = type(json_obj)

        if json_obj_type is list:

            for sub_elem in json_obj:
                result_list.append(self._json2xml(sub_elem, line_spacing))

            return "".join(result_list)

        if json_obj_type is dict:

            for tag_name in json_obj:
                sub_obj = json_obj[tag_name]
                result_list.append("""%s<%s>""" % (line_spacing, tag_name))
                result_list.append(self._json2xml(sub_obj, "" + line_spacing))
                result_list.append("%s</%s>" % (line_spacing, tag_name))

            return "".join(result_list)

        return "%s%s" % (line_spacing, json_obj)

    def __str__(self):
        return self.data

    def to_xml_object(self) -> Any:
        root = e.fromstring(self.data)
        return root
