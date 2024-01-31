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
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class Category(BaseModel):
    """
    This is an object representing a category.  # noqa: E501
    """
    id: StrictStr = Field(..., description="Unique category ID assigned by Voucherify.")
    name: StrictStr = Field(..., description="Category name.")
    hierarchy: StrictInt = Field(..., description="Category hierarchy.")
    object: StrictStr = Field(..., description="The type of object represented by the JSON. This object stores information about the category.")
    created_at: datetime = Field(..., description="Timestamp representing the date and time when the category was created in ISO 8601 format.")
    updated_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the category was updated in ISO 8601 format.")
    stacking_rules_type: Optional[StrictStr] = Field(None, description="The type of the stacking rule eligibility.")
    __properties = ["id", "name", "hierarchy", "object", "created_at", "updated_at", "stacking_rules_type"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('category',):
            raise ValueError("must be one of enum values ('category')")
        return value

    @validator('stacking_rules_type')
    def stacking_rules_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('JOINT', 'EXCLUSIVE',):
            raise ValueError("must be one of enum values ('JOINT', 'EXCLUSIVE')")
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
    def from_json(cls, json_str: str) -> Category:
        """Create an instance of Category from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Category:
        """Create an instance of Category from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Category.parse_obj(obj)

        _obj = Category.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "hierarchy": obj.get("hierarchy"),
            "object": obj.get("object") if obj.get("object") is not None else 'category',
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "stacking_rules_type": obj.get("stacking_rules_type")
        })
        return _obj


