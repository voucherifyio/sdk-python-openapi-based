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
from pydantic import BaseModel, conlist
from openapi_client.models.simple_consent import SimpleConsent
from openapi_client.models.simple_customer import SimpleCustomer

class EventCustomerConsentsGiven(BaseModel):
    """
    Event data object schema for `customer.consents.given`.  # noqa: E501
    """
    customer: Optional[SimpleCustomer] = None
    consents: Optional[conlist(SimpleConsent)] = None
    __properties = ["customer", "consents"]

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
    def from_json(cls, json_str: str) -> EventCustomerConsentsGiven:
        """Create an instance of EventCustomerConsentsGiven from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in consents (list)
        _items = []
        if self.consents:
            for _item in self.consents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['consents'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventCustomerConsentsGiven:
        """Create an instance of EventCustomerConsentsGiven from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventCustomerConsentsGiven.parse_obj(obj)

        _obj = EventCustomerConsentsGiven.parse_obj({
            "customer": SimpleCustomer.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "consents": [SimpleConsent.from_dict(_item) for _item in obj.get("consents")] if obj.get("consents") is not None else None
        })
        return _obj


