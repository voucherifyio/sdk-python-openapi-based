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
from pydantic import BaseModel, Field, StrictStr, validator

class LoyaltyTiersExpirationAllStartDate(BaseModel):
    """
    Defines the conditions for the start date of the tier.  # noqa: E501
    """
    type: Optional[StrictStr] = Field(None, description="What triggers the tier to be valid for a customer.     `IMMEDIATE`: After reaching the minimum required points.  `NEXT_PERIOD`: When the next qualification period starts.")
    __properties = ["type"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('IMMEDIATE', 'NEXT_PERIOD',):
            raise ValueError("must be one of enum values ('IMMEDIATE', 'NEXT_PERIOD')")
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
    def from_json(cls, json_str: str) -> LoyaltyTiersExpirationAllStartDate:
        """Create an instance of LoyaltyTiersExpirationAllStartDate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltyTiersExpirationAllStartDate:
        """Create an instance of LoyaltyTiersExpirationAllStartDate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltyTiersExpirationAllStartDate.parse_obj(obj)

        _obj = LoyaltyTiersExpirationAllStartDate.parse_obj({
            "type": obj.get("type")
        })
        return _obj


