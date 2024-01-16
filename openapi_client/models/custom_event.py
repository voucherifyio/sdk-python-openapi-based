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
from pydantic import BaseModel, Field, StrictStr, validator
from openapi_client.models.custom_event_referral import CustomEventReferral
from openapi_client.models.simple_customer_required_object_type import SimpleCustomerRequiredObjectType

class CustomEvent(BaseModel):
    """
    CustomEvent
    """
    id: Optional[StrictStr] = Field(None, description="Unique custom event ID.")
    object: StrictStr = Field(..., description="The object represented is an `event`.")
    type: StrictStr = Field(..., description="The event name.")
    customer: SimpleCustomerRequiredObjectType = Field(...)
    referral: CustomEventReferral = Field(...)
    loyalty: Dict[str, Any] = Field(...)
    metadata: Optional[Dict[str, Any]] = Field(None, description="A set of custom key/value pairs that you can attach to a customer. The metadata object stores all custom attributes assigned to the custom event.")
    created_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the custom event was created in ISO 8601 format.")
    __properties = ["id", "object", "type", "customer", "referral", "loyalty", "metadata", "created_at"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('event',):
            raise ValueError("must be one of enum values ('event')")
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
    def from_json(cls, json_str: str) -> CustomEvent:
        """Create an instance of CustomEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of referral
        if self.referral:
            _dict['referral'] = self.referral.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomEvent:
        """Create an instance of CustomEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomEvent.parse_obj(obj)

        _obj = CustomEvent.parse_obj({
            "id": obj.get("id"),
            "object": obj.get("object") if obj.get("object") is not None else 'event',
            "type": obj.get("type"),
            "customer": SimpleCustomerRequiredObjectType.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "referral": CustomEventReferral.from_dict(obj.get("referral")) if obj.get("referral") is not None else None,
            "loyalty": obj.get("loyalty"),
            "metadata": obj.get("metadata"),
            "created_at": obj.get("created_at")
        })
        return _obj

