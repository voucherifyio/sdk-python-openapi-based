# coding: utf-8

"""
    Voucherify API

    Voucherify promotion engine REST API. Please see https://docs.voucherify.io/docs for more details.

    The version of the OpenAPI document: v2018-08-01
    Contact: support@voucherify.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr

class MemberActivity(BaseModel):
    """
    This is an object representing member activity.    This is a general object which presents moments from members' activity. There are all types of different events that members perform during their journey once they participate in a loyalty program. Events describe moments when the members redeem loyalty cards and earn points or rewards. The list of all types of activities is listed below.  The details describing the activity are collected in an array property named `data`. In this object, software integrators can find all further information explaining the event context.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="Unique event ID, assigned by Voucherify.")
    type: Optional[StrictStr] = Field(None, description="Event type.")
    data: Optional[Dict[str, Any]] = Field(None, description="Contains details about the event. The objects that are returned in the data attribute differ based on the context of the event type.")
    created_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the member activity occurred in ISO 8601 format.")
    group_id: Optional[StrictStr] = Field(None, description="Unique identifier of the request that caused the event.")
    __properties = ["id", "type", "data", "created_at", "group_id"]

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
    def from_json(cls, json_str: str) -> MemberActivity:
        """Create an instance of MemberActivity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if data (nullable) is None
        # and __fields_set__ contains the field
        if self.data is None and "data" in self.__fields_set__:
            _dict['data'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if group_id (nullable) is None
        # and __fields_set__ contains the field
        if self.group_id is None and "group_id" in self.__fields_set__:
            _dict['group_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MemberActivity:
        """Create an instance of MemberActivity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MemberActivity.parse_obj(obj)

        _obj = MemberActivity.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "data": obj.get("data"),
            "created_at": obj.get("created_at"),
            "group_id": obj.get("group_id")
        })
        return _obj


