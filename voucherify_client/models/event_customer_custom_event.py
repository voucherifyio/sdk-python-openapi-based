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



from pydantic import BaseModel, Field
from voucherify_client.models.customer_with_summary_loyalty_referrals import CustomerWithSummaryLoyaltyReferrals

class EventCustomerCustomEvent(BaseModel):
    """
    Event data object schema for `customer.custom_event`.  # noqa: E501
    """
    customer: CustomerWithSummaryLoyaltyReferrals = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["customer"]

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
    def from_json(cls, json_str: str) -> EventCustomerCustomEvent:
        """Create an instance of EventCustomerCustomEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventCustomerCustomEvent:
        """Create an instance of EventCustomerCustomEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventCustomerCustomEvent.parse_obj(obj)

        _obj = EventCustomerCustomEvent.parse_obj({
            "customer": CustomerWithSummaryLoyaltyReferrals.from_dict(obj.get("customer")) if obj.get("customer") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


