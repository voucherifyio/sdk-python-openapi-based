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
from voucherify_client.models.simple_campaign import SimpleCampaign
from voucherify_client.models.simple_customer import SimpleCustomer
from voucherify_client.models.simple_order import SimpleOrder
from voucherify_client.models.simple_promotion_tier import SimplePromotionTier
from voucherify_client.models.simple_redemption import SimpleRedemption
from voucherify_client.models.simple_voucher import SimpleVoucher

class EventCustomerRedemptionRollbackSucceeded(BaseModel):
    """
    Event data object schema for `customer.redemption.rollback.succeeded`.  # noqa: E501
    """
    customer: Optional[SimpleCustomer] = None
    order: Optional[SimpleOrder] = None
    campaign: Optional[SimpleCampaign] = None
    voucher: Optional[SimpleVoucher] = None
    holder: Optional[SimpleCustomer] = None
    promotion_tier: Optional[SimplePromotionTier] = None
    redemption: Optional[SimpleRedemption] = None
    redemption_rollback: Optional[SimpleRedemption] = None
    __properties = ["customer", "order", "campaign", "voucher", "holder", "promotion_tier", "redemption", "redemption_rollback"]

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
    def from_json(cls, json_str: str) -> EventCustomerRedemptionRollbackSucceeded:
        """Create an instance of EventCustomerRedemptionRollbackSucceeded from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaign
        if self.campaign:
            _dict['campaign'] = self.campaign.to_dict()
        # override the default output from pydantic by calling `to_dict()` of voucher
        if self.voucher:
            _dict['voucher'] = self.voucher.to_dict()
        # override the default output from pydantic by calling `to_dict()` of holder
        if self.holder:
            _dict['holder'] = self.holder.to_dict()
        # override the default output from pydantic by calling `to_dict()` of promotion_tier
        if self.promotion_tier:
            _dict['promotion_tier'] = self.promotion_tier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redemption
        if self.redemption:
            _dict['redemption'] = self.redemption.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redemption_rollback
        if self.redemption_rollback:
            _dict['redemption_rollback'] = self.redemption_rollback.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventCustomerRedemptionRollbackSucceeded:
        """Create an instance of EventCustomerRedemptionRollbackSucceeded from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventCustomerRedemptionRollbackSucceeded.parse_obj(obj)

        _obj = EventCustomerRedemptionRollbackSucceeded.parse_obj({
            "customer": SimpleCustomer.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "order": SimpleOrder.from_dict(obj.get("order")) if obj.get("order") is not None else None,
            "campaign": SimpleCampaign.from_dict(obj.get("campaign")) if obj.get("campaign") is not None else None,
            "voucher": SimpleVoucher.from_dict(obj.get("voucher")) if obj.get("voucher") is not None else None,
            "holder": SimpleCustomer.from_dict(obj.get("holder")) if obj.get("holder") is not None else None,
            "promotion_tier": SimplePromotionTier.from_dict(obj.get("promotion_tier")) if obj.get("promotion_tier") is not None else None,
            "redemption": SimpleRedemption.from_dict(obj.get("redemption")) if obj.get("redemption") is not None else None,
            "redemption_rollback": SimpleRedemption.from_dict(obj.get("redemption_rollback")) if obj.get("redemption_rollback") is not None else None
        })
        return _obj


