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
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator
from voucherify_client.models.simple_customer import SimpleCustomer
from voucherify_client.models.simple_order import SimpleOrder
from voucherify_client.models.simple_promotion_tier import SimplePromotionTier
from voucherify_client.models.simple_redemption_reward_result import SimpleRedemptionRewardResult
from voucherify_client.models.simple_voucher import SimpleVoucher

class SimpleRedemption(BaseModel):
    """
    This is an object representing a simple redemption.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="Unique redemption ID.")
    customer_id: Optional[StrictStr] = Field(None, description="Unique customer ID of the redeeming customer.")
    tracking_id: Optional[StrictStr] = Field(None, description="Hashed customer source ID.")
    var_date: Optional[datetime] = Field(None, alias="date", description="Timestamp representing the date and time when the redemption was created in ISO 8601 format.")
    amount: Optional[StrictInt] = Field(None, description="A positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the total amount of the order. This is the sum of the order items' amounts.")
    order: Optional[SimpleOrder] = None
    reward: Optional[SimpleRedemptionRewardResult] = None
    customer: Optional[SimpleCustomer] = None
    result: Optional[StrictStr] = Field(None, description="Redemption result.")
    voucher: Optional[SimpleVoucher] = None
    promotion_tier: Optional[SimplePromotionTier] = None
    redemption: Optional[StrictStr] = Field(None, description="Unique redemption ID of the parent redemption.")
    object: Optional[StrictStr] = Field('redemption', description="The type of object represented by the JSON. This object stores information about the `redemption`.")
    __properties = ["id", "customer_id", "tracking_id", "date", "amount", "order", "reward", "customer", "result", "voucher", "promotion_tier", "redemption", "object"]

    @validator('result')
    def result_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('SUCCESS', 'FAILURE',):
            raise ValueError("must be one of enum values ('SUCCESS', 'FAILURE')")
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
    def from_json(cls, json_str: str) -> SimpleRedemption:
        """Create an instance of SimpleRedemption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reward
        if self.reward:
            _dict['reward'] = self.reward.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of voucher
        if self.voucher:
            _dict['voucher'] = self.voucher.to_dict()
        # override the default output from pydantic by calling `to_dict()` of promotion_tier
        if self.promotion_tier:
            _dict['promotion_tier'] = self.promotion_tier.to_dict()
        # set to None if customer_id (nullable) is None
        # and __fields_set__ contains the field
        if self.customer_id is None and "customer_id" in self.__fields_set__:
            _dict['customer_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SimpleRedemption:
        """Create an instance of SimpleRedemption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SimpleRedemption.parse_obj(obj)

        _obj = SimpleRedemption.parse_obj({
            "id": obj.get("id"),
            "customer_id": obj.get("customer_id"),
            "tracking_id": obj.get("tracking_id"),
            "var_date": obj.get("date"),
            "amount": obj.get("amount"),
            "order": SimpleOrder.from_dict(obj.get("order")) if obj.get("order") is not None else None,
            "reward": SimpleRedemptionRewardResult.from_dict(obj.get("reward")) if obj.get("reward") is not None else None,
            "customer": SimpleCustomer.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "result": obj.get("result"),
            "voucher": SimpleVoucher.from_dict(obj.get("voucher")) if obj.get("voucher") is not None else None,
            "promotion_tier": SimplePromotionTier.from_dict(obj.get("promotion_tier")) if obj.get("promotion_tier") is not None else None,
            "redemption": obj.get("redemption"),
            "object": obj.get("object") if obj.get("object") is not None else 'redemption'
        })
        return _obj


