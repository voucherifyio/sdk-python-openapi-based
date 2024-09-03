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

class RedemptionsListResponseBodyRedemptionsItemOrderReferrer(BaseModel):
    """
    RedemptionsListResponseBodyRedemptionsItemOrderReferrer
    """
    id: Optional[StrictStr] = Field(None, description="A unique identifier of an existing customer.")
    object: Optional[StrictStr] = Field('customer', description="The type of the object represented by JSON.")
    __properties = ["id", "object"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('customer',):
            raise ValueError("must be one of enum values ('customer')")
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
    def from_json(cls, json_str: str) -> RedemptionsListResponseBodyRedemptionsItemOrderReferrer:
        """Create an instance of RedemptionsListResponseBodyRedemptionsItemOrderReferrer from a JSON string"""
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

        # set to None if object (nullable) is None
        # and __fields_set__ contains the field
        if self.object is None and "object" in self.__fields_set__:
            _dict['object'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RedemptionsListResponseBodyRedemptionsItemOrderReferrer:
        """Create an instance of RedemptionsListResponseBodyRedemptionsItemOrderReferrer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RedemptionsListResponseBodyRedemptionsItemOrderReferrer.parse_obj(obj)

        _obj = RedemptionsListResponseBodyRedemptionsItemOrderReferrer.parse_obj({
            "id": obj.get("id"),
            "object": obj.get("object") if obj.get("object") is not None else 'customer'
        })
        return _obj


