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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr

class SimpleCustomerRequiredObjectType(BaseModel):
    """
    This is an object representing a customer with limited properties used in Event Tracking endpoints.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="The unique ID of a customer that is assigned by Voucherify.")
    source_id: Optional[StrictStr] = Field(None, description="The merchant’s customer ID if it is different from the Voucherify customer ID. It is really useful in case of an integration between multiple systems. It can be a customer ID from a CRM system, database or 3rd-party service.")
    name: Optional[StrictStr] = Field(None, description="Customer's first and last name.")
    email: Optional[StrictStr] = Field(None, description="Customer's email address.")
    metadata: Optional[Dict[str, Any]] = Field(None, description="A set of custom key/value pairs that you can attach to a customer. The metadata object stores all custom attributes assigned to the customer. It can be useful for storing additional information about the customer in a structured format. This metadata can be used for validating whether the customer qualifies for a discount or it can be used in building customer segments. ")
    object: StrictStr = Field(..., description="The type of object represented by the JSON. This object stores information about the customer.")
    __properties = ["id", "source_id", "name", "email", "metadata", "object"]

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
    def from_json(cls, json_str: str) -> SimpleCustomerRequiredObjectType:
        """Create an instance of SimpleCustomerRequiredObjectType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SimpleCustomerRequiredObjectType:
        """Create an instance of SimpleCustomerRequiredObjectType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SimpleCustomerRequiredObjectType.parse_obj(obj)

        _obj = SimpleCustomerRequiredObjectType.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("source_id"),
            "name": obj.get("name"),
            "email": obj.get("email"),
            "metadata": obj.get("metadata"),
            "object": obj.get("object") if obj.get("object") is not None else 'customer'
        })
        return _obj


