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
from openapi_client.models.customer_base_address import CustomerBaseAddress

class CustomersCreateRequestBody(BaseModel):
    """
    Request body schema for **POST** `/customers`.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="The ID of an existing customer.")
    source_id: Optional[StrictStr] = Field(None, description="A unique identifier of the customer who validates a voucher. It can be a customer ID or email from a CRM system, database, or a third-party service. If you also pass a customer ID (unique ID assigned by Voucherify), the source ID will be ignored.")
    name: Optional[StrictStr] = Field(None, description="Customer's first and last name.")
    description: Optional[StrictStr] = Field(None, description="An arbitrary string that you can attach to a customer object.")
    email: Optional[StrictStr] = Field(None, description="Customer's email address.")
    phone: Optional[StrictStr] = Field(None, description="Customer's phone number. This parameter is mandatory when you try to send out codes to customers via an SMS channel.")
    birthday: Optional[date] = Field(None, description="*Deprecated* Customer's birthdate; format YYYY-MM-DD.")
    birthdate: Optional[date] = Field(None, description="Customer's birthdate; format YYYY-MM-DD.")
    address: Optional[CustomerBaseAddress] = None
    metadata: Optional[Dict[str, Any]] = Field(None, description="A set of custom key/value pairs that you can attach to a customer. The metadata object stores all custom attributes assigned to the customer. It can be useful for storing additional information about the customer in a structured format. This metadata can be used for validating whether the customer qualifies for a discount or it can be used in building customer segments.")
    __properties = ["id", "source_id", "name", "description", "email", "phone", "birthday", "birthdate", "address", "metadata"]

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
    def from_json(cls, json_str: str) -> CustomersCreateRequestBody:
        """Create an instance of CustomersCreateRequestBody from a JSON string"""
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
        # set to None if address (nullable) is None
        # and __fields_set__ contains the field
        if self.address is None and "address" in self.__fields_set__:
            _dict['address'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomersCreateRequestBody:
        """Create an instance of CustomersCreateRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomersCreateRequestBody.parse_obj(obj)

        _obj = CustomersCreateRequestBody.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("source_id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "email": obj.get("email"),
            "phone": obj.get("phone"),
            "birthday": obj.get("birthday"),
            "birthdate": obj.get("birthdate"),
            "address": CustomerBaseAddress.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "metadata": obj.get("metadata")
        })
        return _obj


