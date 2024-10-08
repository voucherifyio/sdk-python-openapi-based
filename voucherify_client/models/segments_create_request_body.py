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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator

class SegmentsCreateRequestBody(BaseModel):
    """
    SegmentsCreateRequestBody
    """
    name: Optional[StrictStr] = Field(None, description="Segment name.")
    type: Optional[StrictStr] = None
    customers: Optional[conlist(StrictStr)] = Field(None, description="Array of customer IDs.")
    filter: Optional[Dict[str, Any]] = Field(None, description="Defines a set of criteria for an `auto-update` segment type.")
    __properties = ["name", "type", "customers", "filter"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('static', 'auto-update',):
            raise ValueError("must be one of enum values ('static', 'auto-update')")
        return value

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
    def from_json(cls, json_str: str) -> SegmentsCreateRequestBody:
        """Create an instance of SegmentsCreateRequestBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if customers (nullable) is None
        # and __fields_set__ contains the field
        if self.customers is None and "customers" in self.__fields_set__:
            _dict['customers'] = None

        # set to None if filter (nullable) is None
        # and __fields_set__ contains the field
        if self.filter is None and "filter" in self.__fields_set__:
            _dict['filter'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SegmentsCreateRequestBody:
        """Create an instance of SegmentsCreateRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SegmentsCreateRequestBody.parse_obj(obj)

        _obj = SegmentsCreateRequestBody.parse_obj({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "customers": obj.get("customers"),
            "filter": obj.get("filter")
        })
        return _obj


