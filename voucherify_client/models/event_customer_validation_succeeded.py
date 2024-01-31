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
from pydantic import BaseModel
from voucherify_client.models.simple_customer import SimpleCustomer
from voucherify_client.models.validation_entity import ValidationEntity

class EventCustomerValidationSucceeded(BaseModel):
    """
    Event data object schema for `customer.validation.succeeded`.  # noqa: E501
    """
    customer: Optional[SimpleCustomer] = None
    validation: Optional[ValidationEntity] = None
    __properties = ["customer", "validation"]

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
    def from_json(cls, json_str: str) -> EventCustomerValidationSucceeded:
        """Create an instance of EventCustomerValidationSucceeded from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validation
        if self.validation:
            _dict['validation'] = self.validation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventCustomerValidationSucceeded:
        """Create an instance of EventCustomerValidationSucceeded from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventCustomerValidationSucceeded.parse_obj(obj)

        _obj = EventCustomerValidationSucceeded.parse_obj({
            "customer": SimpleCustomer.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "validation": ValidationEntity.from_dict(obj.get("validation")) if obj.get("validation") is not None else None
        })
        return _obj


