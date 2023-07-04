# coding: utf-8

"""
    LINE Messaging API

    This document describes LINE Messaging API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, StrictStr, conlist
from linebot.v3.messaging.models.action import Action
from linebot.v3.messaging.models.template import Template

class ConfirmTemplate(Template):
    """
    ConfirmTemplate
    """
    text: Optional[StrictStr] = None
    actions: Optional[conlist(Action)] = None
    type: str = "confirm"

    __properties = ["type", "text", "actions"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ConfirmTemplate:
        """Create an instance of ConfirmTemplate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item in self.actions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['actions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfirmTemplate:
        """Create an instance of ConfirmTemplate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfirmTemplate.parse_obj(obj)

        _obj = ConfirmTemplate.parse_obj({
            "type": obj.get("type"),
            "text": obj.get("text"),
            "actions": [Action.from_dict(_item) for _item in obj.get("actions")] if obj.get("actions") is not None else None
        })
        return _obj
