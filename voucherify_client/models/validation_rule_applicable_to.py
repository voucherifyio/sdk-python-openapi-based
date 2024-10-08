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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, conlist
from voucherify_client.models.applicable_to import ApplicableTo

class ValidationRuleApplicableTo(BaseModel):
    """
    ValidationRuleApplicableTo
    """
    excluded: Optional[conlist(ApplicableTo)] = Field(None, description="Defines which items are excluded from a discount.")
    included: Optional[conlist(ApplicableTo)] = Field(None, description="Defines which items are included in a discount.")
    included_all: Optional[StrictBool] = Field(None, description="Indicates whether all items are included in the discount.")
    __properties = ["excluded", "included", "included_all"]

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
    def from_json(cls, json_str: str) -> ValidationRuleApplicableTo:
        """Create an instance of ValidationRuleApplicableTo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in excluded (list)
        _items = []
        if self.excluded:
            for _item in self.excluded:
                if _item:
                    _items.append(_item.to_dict())
            _dict['excluded'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in included (list)
        _items = []
        if self.included:
            for _item in self.included:
                if _item:
                    _items.append(_item.to_dict())
            _dict['included'] = _items
        # set to None if excluded (nullable) is None
        # and __fields_set__ contains the field
        if self.excluded is None and "excluded" in self.__fields_set__:
            _dict['excluded'] = None

        # set to None if included (nullable) is None
        # and __fields_set__ contains the field
        if self.included is None and "included" in self.__fields_set__:
            _dict['included'] = None

        # set to None if included_all (nullable) is None
        # and __fields_set__ contains the field
        if self.included_all is None and "included_all" in self.__fields_set__:
            _dict['included_all'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ValidationRuleApplicableTo:
        """Create an instance of ValidationRuleApplicableTo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ValidationRuleApplicableTo.parse_obj(obj)

        _obj = ValidationRuleApplicableTo.parse_obj({
            "excluded": [ApplicableTo.from_dict(_item) for _item in obj.get("excluded")] if obj.get("excluded") is not None else None,
            "included": [ApplicableTo.from_dict(_item) for _item in obj.get("included")] if obj.get("included") is not None else None,
            "included_all": obj.get("included_all")
        })
        return _obj


