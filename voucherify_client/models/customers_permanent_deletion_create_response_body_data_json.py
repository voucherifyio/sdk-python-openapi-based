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
from pydantic import BaseModel, Field, StrictInt

class CustomersPermanentDeletionCreateResponseBodyDataJson(BaseModel):
    """
    Statistics summarizing the number of related information that was deleted.  # noqa: E501
    """
    events: Optional[StrictInt] = Field(None, description="Number of events deleted.")
    customer_events: Optional[StrictInt] = Field(None, description="Number of customer events deleted.")
    daily_events: Optional[StrictInt] = Field(None, description="Number of daily events deleted.")
    segments: Optional[StrictInt] = Field(None, description="Number of segments deleted.")
    orders: Optional[StrictInt] = Field(None, description="Number of orders deleted.")
    order_events: Optional[StrictInt] = Field(None, description="Number of order events deleted.")
    customer: Optional[StrictInt] = Field(1, description="Number of customers deleted.")
    __properties = ["events", "customer_events", "daily_events", "segments", "orders", "order_events", "customer"]

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
    def from_json(cls, json_str: str) -> CustomersPermanentDeletionCreateResponseBodyDataJson:
        """Create an instance of CustomersPermanentDeletionCreateResponseBodyDataJson from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if events (nullable) is None
        # and __fields_set__ contains the field
        if self.events is None and "events" in self.__fields_set__:
            _dict['events'] = None

        # set to None if customer_events (nullable) is None
        # and __fields_set__ contains the field
        if self.customer_events is None and "customer_events" in self.__fields_set__:
            _dict['customer_events'] = None

        # set to None if daily_events (nullable) is None
        # and __fields_set__ contains the field
        if self.daily_events is None and "daily_events" in self.__fields_set__:
            _dict['daily_events'] = None

        # set to None if segments (nullable) is None
        # and __fields_set__ contains the field
        if self.segments is None and "segments" in self.__fields_set__:
            _dict['segments'] = None

        # set to None if orders (nullable) is None
        # and __fields_set__ contains the field
        if self.orders is None and "orders" in self.__fields_set__:
            _dict['orders'] = None

        # set to None if order_events (nullable) is None
        # and __fields_set__ contains the field
        if self.order_events is None and "order_events" in self.__fields_set__:
            _dict['order_events'] = None

        # set to None if customer (nullable) is None
        # and __fields_set__ contains the field
        if self.customer is None and "customer" in self.__fields_set__:
            _dict['customer'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomersPermanentDeletionCreateResponseBodyDataJson:
        """Create an instance of CustomersPermanentDeletionCreateResponseBodyDataJson from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomersPermanentDeletionCreateResponseBodyDataJson.parse_obj(obj)

        _obj = CustomersPermanentDeletionCreateResponseBodyDataJson.parse_obj({
            "events": obj.get("events"),
            "customer_events": obj.get("customer_events"),
            "daily_events": obj.get("daily_events"),
            "segments": obj.get("segments"),
            "orders": obj.get("orders"),
            "order_events": obj.get("order_events"),
            "customer": obj.get("customer") if obj.get("customer") is not None else 1
        })
        return _obj


