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

from datetime import date
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from voucherify_client.models.customers_update_request_body_address import CustomersUpdateRequestBodyAddress

class CustomersUpdateRequestBody(BaseModel):
    """
    Request body schema for **PUT** `v1/customers/{customerId}`.  # noqa: E501
    """
    name: Optional[StrictStr] = Field(None, description="Customer's first and last name.")
    description: Optional[StrictStr] = Field(None, description="An arbitrary string that you can attach to a customer object.")
    email: Optional[StrictStr] = Field(None, description="Customer's email address.")
    phone: Optional[StrictStr] = Field(None, description="Customer's phone number. This parameter is mandatory when you try to send out codes to customers via an SMS channel.")
    birthday: Optional[date] = Field(None, description="`Deprecated`. ~~Customer's birthdate; format YYYY-MM-DD~~.")
    birthdate: Optional[date] = Field(None, description="Customer's birthdate; format YYYY-MM-DD.")
    address: Optional[CustomersUpdateRequestBodyAddress] = None
    metadata: Optional[Dict[str, Any]] = Field(None, description="A set of custom key/value pairs that you can attach to a customer. The metadata object stores all custom attributes assigned to the customer. It can be useful for storing additional information about the customer in a structured format. This metadata can be used for validating whether the customer qualifies for a discount or it can be used in building customer segments.")
    __properties = ["name", "description", "email", "phone", "birthday", "birthdate", "address", "metadata"]

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
    def from_json(cls, json_str: str) -> CustomersUpdateRequestBody:
        """Create an instance of CustomersUpdateRequestBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if email (nullable) is None
        # and __fields_set__ contains the field
        if self.email is None and "email" in self.__fields_set__:
            _dict['email'] = None

        # set to None if phone (nullable) is None
        # and __fields_set__ contains the field
        if self.phone is None and "phone" in self.__fields_set__:
            _dict['phone'] = None

        # set to None if birthday (nullable) is None
        # and __fields_set__ contains the field
        if self.birthday is None and "birthday" in self.__fields_set__:
            _dict['birthday'] = None

        # set to None if birthdate (nullable) is None
        # and __fields_set__ contains the field
        if self.birthdate is None and "birthdate" in self.__fields_set__:
            _dict['birthdate'] = None

        # set to None if address (nullable) is None
        # and __fields_set__ contains the field
        if self.address is None and "address" in self.__fields_set__:
            _dict['address'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomersUpdateRequestBody:
        """Create an instance of CustomersUpdateRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomersUpdateRequestBody.parse_obj(obj)

        _obj = CustomersUpdateRequestBody.parse_obj({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "email": obj.get("email"),
            "phone": obj.get("phone"),
            "birthday": obj.get("birthday"),
            "birthdate": obj.get("birthdate"),
            "address": CustomersUpdateRequestBodyAddress.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "metadata": obj.get("metadata")
        })
        return _obj


