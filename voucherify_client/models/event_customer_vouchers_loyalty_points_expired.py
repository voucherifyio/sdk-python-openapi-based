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
from pydantic import BaseModel, StrictInt, conlist
from voucherify_client.models.simple_campaign import SimpleCampaign
from voucherify_client.models.simple_customer import SimpleCustomer
from voucherify_client.models.simple_voucher import SimpleVoucher
from voucherify_client.models.voucher_transaction import VoucherTransaction

class EventCustomerVouchersLoyaltyPointsExpired(BaseModel):
    """
    Event data object schema for `customer.voucher.loyalty_card.points_expired`.  # noqa: E501
    """
    customer: Optional[SimpleCustomer] = None
    campaign: Optional[SimpleCampaign] = None
    voucher: Optional[SimpleVoucher] = None
    points: Optional[StrictInt] = None
    buckets: Optional[conlist(VoucherTransaction)] = None
    transaction: Optional[VoucherTransaction] = None
    __properties = ["customer", "campaign", "voucher", "points", "buckets", "transaction"]

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
    def from_json(cls, json_str: str) -> EventCustomerVouchersLoyaltyPointsExpired:
        """Create an instance of EventCustomerVouchersLoyaltyPointsExpired from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of campaign
        if self.campaign:
            _dict['campaign'] = self.campaign.to_dict()
        # override the default output from pydantic by calling `to_dict()` of voucher
        if self.voucher:
            _dict['voucher'] = self.voucher.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in buckets (list)
        _items = []
        if self.buckets:
            for _item in self.buckets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['buckets'] = _items
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventCustomerVouchersLoyaltyPointsExpired:
        """Create an instance of EventCustomerVouchersLoyaltyPointsExpired from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventCustomerVouchersLoyaltyPointsExpired.parse_obj(obj)

        _obj = EventCustomerVouchersLoyaltyPointsExpired.parse_obj({
            "customer": SimpleCustomer.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "campaign": SimpleCampaign.from_dict(obj.get("campaign")) if obj.get("campaign") is not None else None,
            "voucher": SimpleVoucher.from_dict(obj.get("voucher")) if obj.get("voucher") is not None else None,
            "points": obj.get("points"),
            "buckets": [VoucherTransaction.from_dict(_item) for _item in obj.get("buckets")] if obj.get("buckets") is not None else None,
            "transaction": VoucherTransaction.from_dict(obj.get("transaction")) if obj.get("transaction") is not None else None
        })
        return _obj


