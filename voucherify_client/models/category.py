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
    id: Optional[StrictStr] = Field(None, description="Unique category ID assigned by Voucherify.")
    name: Optional[StrictStr] = Field(None, description="Category name.")
    hierarchy: Optional[StrictInt] = Field(None, description="Category hierarchy.")
    object: Optional[StrictStr] = Field('category', description="The type of the object represented by the JSON. This object stores information about the category.")
    created_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the category was created. The value is shown in the ISO 8601 format.")
    updated_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the category was updated. The value is shown in the ISO 8601 format.")
    stacking_rules_type: Optional[StrictStr] = Field(None, description="The type of the stacking rule eligibility.")
    __properties = ["id", "name", "hierarchy", "object", "created_at", "updated_at", "stacking_rules_type"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

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
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if hierarchy (nullable) is None
        # and __fields_set__ contains the field
        if self.hierarchy is None and "hierarchy" in self.__fields_set__:
            _dict['hierarchy'] = None

        # set to None if object (nullable) is None
        # and __fields_set__ contains the field
        if self.object is None and "object" in self.__fields_set__:
            _dict['object'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        # set to None if stacking_rules_type (nullable) is None
        # and __fields_set__ contains the field
        if self.stacking_rules_type is None and "stacking_rules_type" in self.__fields_set__:
            _dict['stacking_rules_type'] = None

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


