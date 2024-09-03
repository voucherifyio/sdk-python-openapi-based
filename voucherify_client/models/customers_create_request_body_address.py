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
from pydantic import BaseModel, Field, StrictStr

class CustomersCreateRequestBodyAddress(BaseModel):
    """
    Customer's address.  # noqa: E501
    """
    city: Optional[StrictStr] = Field(None, description="City")
    state: Optional[StrictStr] = Field(None, description="State")
    line_1: Optional[StrictStr] = Field(None, description="First line of address.")
    line_2: Optional[StrictStr] = Field(None, description="Second line of address.")
    country: Optional[StrictStr] = Field(None, description="Country.")
    postal_code: Optional[StrictStr] = Field(None, description="Postal code.")
    __properties = ["city", "state", "line_1", "line_2", "country", "postal_code"]

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
    def from_json(cls, json_str: str) -> CustomersCreateRequestBodyAddress:
        """Create an instance of CustomersCreateRequestBodyAddress from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if city (nullable) is None
        # and __fields_set__ contains the field
        if self.city is None and "city" in self.__fields_set__:
            _dict['city'] = None

        # set to None if state (nullable) is None
        # and __fields_set__ contains the field
        if self.state is None and "state" in self.__fields_set__:
            _dict['state'] = None

        # set to None if line_1 (nullable) is None
        # and __fields_set__ contains the field
        if self.line_1 is None and "line_1" in self.__fields_set__:
            _dict['line_1'] = None

        # set to None if line_2 (nullable) is None
        # and __fields_set__ contains the field
        if self.line_2 is None and "line_2" in self.__fields_set__:
            _dict['line_2'] = None

        # set to None if country (nullable) is None
        # and __fields_set__ contains the field
        if self.country is None and "country" in self.__fields_set__:
            _dict['country'] = None

        # set to None if postal_code (nullable) is None
        # and __fields_set__ contains the field
        if self.postal_code is None and "postal_code" in self.__fields_set__:
            _dict['postal_code'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomersCreateRequestBodyAddress:
        """Create an instance of CustomersCreateRequestBodyAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomersCreateRequestBodyAddress.parse_obj(obj)

        _obj = CustomersCreateRequestBodyAddress.parse_obj({
            "city": obj.get("city"),
            "state": obj.get("state"),
            "line_1": obj.get("line_1"),
            "line_2": obj.get("line_2"),
            "country": obj.get("country"),
            "postal_code": obj.get("postal_code")
        })
        return _obj


