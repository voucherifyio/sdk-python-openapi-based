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
from pydantic import BaseModel, Field, StrictStr, validator
from voucherify_client.models.simple_customer_required_object_type import SimpleCustomerRequiredObjectType

class EventsCreateResponseBody(BaseModel):
    """
    Response body schema for **POST** `v1/events`.  # noqa: E501
    """
    object: Optional[StrictStr] = Field('event', description="The object represented is an `event`.")
    type: Optional[StrictStr] = Field(None, description="The event name.")
    customer: SimpleCustomerRequiredObjectType = Field(...)
    referral: Optional[Dict[str, Any]] = Field(None, description="A `null` referral object.")
    loyalty: Optional[Dict[str, Any]] = Field(None, description="A `null` loyalty object.")
    metadata: Optional[Dict[str, Any]] = None
    __properties = ["object", "type", "customer", "referral", "loyalty", "metadata"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

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
    def from_json(cls, json_str: str) -> EventsCreateResponseBody:
        """Create an instance of EventsCreateResponseBody from a JSON string"""
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
        # set to None if object (nullable) is None
        # and __fields_set__ contains the field
        if self.object is None and "object" in self.__fields_set__:
            _dict['object'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if referral (nullable) is None
        # and __fields_set__ contains the field
        if self.referral is None and "referral" in self.__fields_set__:
            _dict['referral'] = None

        # set to None if loyalty (nullable) is None
        # and __fields_set__ contains the field
        if self.loyalty is None and "loyalty" in self.__fields_set__:
            _dict['loyalty'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventsCreateResponseBody:
        """Create an instance of EventsCreateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventsCreateResponseBody.parse_obj(obj)

        _obj = EventsCreateResponseBody.parse_obj({
            "object": obj.get("object") if obj.get("object") is not None else 'event',
            "type": obj.get("type"),
            "customer": SimpleCustomerRequiredObjectType.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "referral": obj.get("referral"),
            "loyalty": obj.get("loyalty"),
            "metadata": obj.get("metadata")
        })
        return _obj


