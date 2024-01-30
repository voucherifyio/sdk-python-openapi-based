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
from pydantic import BaseModel, Field, constr
from voucherify_client.models.client_events_create_request_body_loyalty import ClientEventsCreateRequestBodyLoyalty
from voucherify_client.models.client_events_create_request_body_referral import ClientEventsCreateRequestBodyReferral
from voucherify_client.models.customer import Customer

class EventsCreateRequestBody(BaseModel):
    """
    Request body schema for **POST** `/events`.  # noqa: E501
    """
    event: constr(strict=True, max_length=300, min_length=1) = Field(..., description="Event name. This is the same name that you used to define a custom event in the **Dashboard** > **Project Settings** > **Event Schema**.")
    customer: Customer = Field(...)
    referral: Optional[ClientEventsCreateRequestBodyReferral] = None
    loyalty: Optional[ClientEventsCreateRequestBodyLoyalty] = None
    metadata: Optional[Dict[str, Any]] = Field(None, description="The metadata object stores all custom attributes assigned to the event. A set of key/value pairs that you can attach to an event object. It can be useful for storing additional information about the event in a structured format. Event metadata schema is defined in the **Dashboard** > **Project Settings** > **Event Schema** > **Edit particular event** > **Metadata property definition**.")
    __properties = ["event", "customer", "referral", "loyalty", "metadata"]

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
    def from_json(cls, json_str: str) -> EventsCreateRequestBody:
        """Create an instance of EventsCreateRequestBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of loyalty
        if self.loyalty:
            _dict['loyalty'] = self.loyalty.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventsCreateRequestBody:
        """Create an instance of EventsCreateRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventsCreateRequestBody.parse_obj(obj)

        _obj = EventsCreateRequestBody.parse_obj({
            "event": obj.get("event"),
            "customer": Customer.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "referral": ClientEventsCreateRequestBodyReferral.from_dict(obj.get("referral")) if obj.get("referral") is not None else None,
            "loyalty": ClientEventsCreateRequestBodyLoyalty.from_dict(obj.get("loyalty")) if obj.get("loyalty") is not None else None,
            "metadata": obj.get("metadata")
        })
        return _obj

