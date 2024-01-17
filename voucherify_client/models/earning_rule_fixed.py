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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class EarningRuleFixed(BaseModel):
    """
    EarningRuleFixed
    """
    type: Optional[StrictStr] = Field('FIXED', description="The number of points to be added to the loyalty card.")
    points: Optional[StrictInt] = Field(None, description="Defines how the points will be added to the loyalty card. FIXED adds a fixed number of points.")
    __properties = ["type", "points"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('FIXED', 'PROPORTIONAL',):
            raise ValueError("must be one of enum values ('FIXED', 'PROPORTIONAL')")
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
    def from_json(cls, json_str: str) -> EarningRuleFixed:
        """Create an instance of EarningRuleFixed from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EarningRuleFixed:
        """Create an instance of EarningRuleFixed from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EarningRuleFixed.parse_obj(obj)

        _obj = EarningRuleFixed.parse_obj({
            "type": obj.get("type") if obj.get("type") is not None else 'FIXED',
            "points": obj.get("points")
        })
        return _obj

