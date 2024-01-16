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

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field
from openapi_client.models.simple_customer import SimpleCustomer

class EventCustomerBatchSent(BaseModel):
    """
    Event data object schema for `customer.batch.sent`.  # noqa: E501
    """
    customer: Optional[SimpleCustomer] = None
    distribution: Optional[Dict[str, Any]] = None
    sent_at: datetime = Field(..., description="Timestamp representing the date and time when the distribution was sent in ISO 8601 format.")
    __properties = ["customer", "distribution", "sent_at"]

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
    def from_json(cls, json_str: str) -> EventCustomerBatchSent:
        """Create an instance of EventCustomerBatchSent from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventCustomerBatchSent:
        """Create an instance of EventCustomerBatchSent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventCustomerBatchSent.parse_obj(obj)

        _obj = EventCustomerBatchSent.parse_obj({
            "customer": SimpleCustomer.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "distribution": obj.get("distribution"),
            "sent_at": obj.get("sent_at")
        })
        return _obj


