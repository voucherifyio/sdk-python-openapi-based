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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator
from voucherify_client.models.redemption_entry_channel import RedemptionEntryChannel
from voucherify_client.models.redemption_entry_customer import RedemptionEntryCustomer
from voucherify_client.models.redemption_entry_gift import RedemptionEntryGift
from voucherify_client.models.redemption_entry_loyalty_card import RedemptionEntryLoyaltyCard
from voucherify_client.models.redemption_entry_order import RedemptionEntryOrder
from voucherify_client.models.redemption_entry_promotion_tier import RedemptionEntryPromotionTier
from voucherify_client.models.redemption_entry_related_redemptions import RedemptionEntryRelatedRedemptions
from voucherify_client.models.redemption_entry_voucher import RedemptionEntryVoucher
from voucherify_client.models.redemption_reward_result import RedemptionRewardResult

class RedemptionEntry(BaseModel):
    """
    RedemptionEntry
    """
    id: Optional[StrictStr] = None
    object: Optional[StrictStr] = None
    var_date: Optional[datetime] = Field(None, alias="date", description="Timestamp representing the date and time when the object was created. The value is shown in the ISO 8601 format.")
    customer_id: Optional[StrictStr] = Field(None, description="Unique customer ID of the redeeming customer.")
    tracking_id: Optional[StrictStr] = Field(None, description="Hashed customer source ID.")
    metadata: Optional[Dict[str, Any]] = None
    amount: Optional[StrictInt] = Field(None, description="For gift cards, this is a positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the number of redeemed credits. For loyalty cards, this is the number of loyalty points used in the transaction. and For gift cards, this represents the number of the credits restored to the card in the rolledback redemption. The number is a negative integer in the smallest currency unit, e.g. -100 cents for $1.00 added back to the card. For loyalty cards, this represents the number of loyalty points restored to the card in the rolledback redemption. The number is a negative integer.")
    redemption: Optional[StrictStr] = Field(None, description="Unique redemption ID of the parent redemption.")
    result: Optional[StrictStr] = Field(None, description="Redemption result.")
    status: Optional[StrictStr] = None
    related_redemptions: Optional[RedemptionEntryRelatedRedemptions] = None
    failure_code: Optional[StrictStr] = Field(None, description="If the result is `FAILURE`, this parameter will provide a generic reason as to why the redemption failed.")
    failure_message: Optional[StrictStr] = Field(None, description="If the result is `FAILURE`, this parameter will provide a more expanded reason as to why the redemption failed.")
    order: Optional[RedemptionEntryOrder] = None
    channel: Optional[RedemptionEntryChannel] = None
    customer: Optional[RedemptionEntryCustomer] = None
    related_object_type: Optional[StrictStr] = Field(None, description="Defines the related object.")
    related_object_id: Optional[StrictStr] = None
    voucher: Optional[RedemptionEntryVoucher] = None
    promotion_tier: Optional[RedemptionEntryPromotionTier] = None
    reward: Optional[RedemptionRewardResult] = None
    gift: Optional[RedemptionEntryGift] = None
    loyalty_card: Optional[RedemptionEntryLoyaltyCard] = None
    reason: Optional[StrictStr] = Field(None, description="System generated cause for the redemption being invalid in the context of the provided parameters.")
    __properties = ["id", "object", "date", "customer_id", "tracking_id", "metadata", "amount", "redemption", "result", "status", "related_redemptions", "failure_code", "failure_message", "order", "channel", "customer", "related_object_type", "related_object_id", "voucher", "promotion_tier", "reward", "gift", "loyalty_card", "reason"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('redemption', 'redemption_rollback',):
            raise ValueError("must be one of enum values ('redemption', 'redemption_rollback')")
        return value

    @validator('result')
    def result_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('SUCCESS', 'FAILURE',):
            raise ValueError("must be one of enum values ('SUCCESS', 'FAILURE')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('SUCCEEDED', 'FAILED', 'ROLLED_BACK',):
            raise ValueError("must be one of enum values ('SUCCEEDED', 'FAILED', 'ROLLED_BACK')")
        return value

    @validator('related_object_type')
    def related_object_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('voucher', 'promotion_tier', 'redemption',):
            raise ValueError("must be one of enum values ('voucher', 'promotion_tier', 'redemption')")
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
    def from_json(cls, json_str: str) -> RedemptionEntry:
        """Create an instance of RedemptionEntry from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of related_redemptions
        if self.related_redemptions:
            _dict['related_redemptions'] = self.related_redemptions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of channel
        if self.channel:
            _dict['channel'] = self.channel.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of voucher
        if self.voucher:
            _dict['voucher'] = self.voucher.to_dict()
        # override the default output from pydantic by calling `to_dict()` of promotion_tier
        if self.promotion_tier:
            _dict['promotion_tier'] = self.promotion_tier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reward
        if self.reward:
            _dict['reward'] = self.reward.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gift
        if self.gift:
            _dict['gift'] = self.gift.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loyalty_card
        if self.loyalty_card:
            _dict['loyalty_card'] = self.loyalty_card.to_dict()
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if object (nullable) is None
        # and __fields_set__ contains the field
        if self.object is None and "object" in self.__fields_set__:
            _dict['object'] = None

        # set to None if var_date (nullable) is None
        # and __fields_set__ contains the field
        if self.var_date is None and "var_date" in self.__fields_set__:
            _dict['date'] = None

        # set to None if customer_id (nullable) is None
        # and __fields_set__ contains the field
        if self.customer_id is None and "customer_id" in self.__fields_set__:
            _dict['customer_id'] = None

        # set to None if tracking_id (nullable) is None
        # and __fields_set__ contains the field
        if self.tracking_id is None and "tracking_id" in self.__fields_set__:
            _dict['tracking_id'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        # set to None if amount (nullable) is None
        # and __fields_set__ contains the field
        if self.amount is None and "amount" in self.__fields_set__:
            _dict['amount'] = None

        # set to None if redemption (nullable) is None
        # and __fields_set__ contains the field
        if self.redemption is None and "redemption" in self.__fields_set__:
            _dict['redemption'] = None

        # set to None if result (nullable) is None
        # and __fields_set__ contains the field
        if self.result is None and "result" in self.__fields_set__:
            _dict['result'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if related_redemptions (nullable) is None
        # and __fields_set__ contains the field
        if self.related_redemptions is None and "related_redemptions" in self.__fields_set__:
            _dict['related_redemptions'] = None

        # set to None if failure_code (nullable) is None
        # and __fields_set__ contains the field
        if self.failure_code is None and "failure_code" in self.__fields_set__:
            _dict['failure_code'] = None

        # set to None if failure_message (nullable) is None
        # and __fields_set__ contains the field
        if self.failure_message is None and "failure_message" in self.__fields_set__:
            _dict['failure_message'] = None

        # set to None if order (nullable) is None
        # and __fields_set__ contains the field
        if self.order is None and "order" in self.__fields_set__:
            _dict['order'] = None

        # set to None if channel (nullable) is None
        # and __fields_set__ contains the field
        if self.channel is None and "channel" in self.__fields_set__:
            _dict['channel'] = None

        # set to None if customer (nullable) is None
        # and __fields_set__ contains the field
        if self.customer is None and "customer" in self.__fields_set__:
            _dict['customer'] = None

        # set to None if related_object_type (nullable) is None
        # and __fields_set__ contains the field
        if self.related_object_type is None and "related_object_type" in self.__fields_set__:
            _dict['related_object_type'] = None

        # set to None if related_object_id (nullable) is None
        # and __fields_set__ contains the field
        if self.related_object_id is None and "related_object_id" in self.__fields_set__:
            _dict['related_object_id'] = None

        # set to None if voucher (nullable) is None
        # and __fields_set__ contains the field
        if self.voucher is None and "voucher" in self.__fields_set__:
            _dict['voucher'] = None

        # set to None if promotion_tier (nullable) is None
        # and __fields_set__ contains the field
        if self.promotion_tier is None and "promotion_tier" in self.__fields_set__:
            _dict['promotion_tier'] = None

        # set to None if gift (nullable) is None
        # and __fields_set__ contains the field
        if self.gift is None and "gift" in self.__fields_set__:
            _dict['gift'] = None

        # set to None if loyalty_card (nullable) is None
        # and __fields_set__ contains the field
        if self.loyalty_card is None and "loyalty_card" in self.__fields_set__:
            _dict['loyalty_card'] = None

        # set to None if reason (nullable) is None
        # and __fields_set__ contains the field
        if self.reason is None and "reason" in self.__fields_set__:
            _dict['reason'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RedemptionEntry:
        """Create an instance of RedemptionEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RedemptionEntry.parse_obj(obj)

        _obj = RedemptionEntry.parse_obj({
            "id": obj.get("id"),
            "object": obj.get("object"),
            "var_date": obj.get("date"),
            "customer_id": obj.get("customer_id"),
            "tracking_id": obj.get("tracking_id"),
            "metadata": obj.get("metadata"),
            "amount": obj.get("amount"),
            "redemption": obj.get("redemption"),
            "result": obj.get("result"),
            "status": obj.get("status"),
            "related_redemptions": RedemptionEntryRelatedRedemptions.from_dict(obj.get("related_redemptions")) if obj.get("related_redemptions") is not None else None,
            "failure_code": obj.get("failure_code"),
            "failure_message": obj.get("failure_message"),
            "order": RedemptionEntryOrder.from_dict(obj.get("order")) if obj.get("order") is not None else None,
            "channel": RedemptionEntryChannel.from_dict(obj.get("channel")) if obj.get("channel") is not None else None,
            "customer": RedemptionEntryCustomer.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "related_object_type": obj.get("related_object_type"),
            "related_object_id": obj.get("related_object_id"),
            "voucher": RedemptionEntryVoucher.from_dict(obj.get("voucher")) if obj.get("voucher") is not None else None,
            "promotion_tier": RedemptionEntryPromotionTier.from_dict(obj.get("promotion_tier")) if obj.get("promotion_tier") is not None else None,
            "reward": RedemptionRewardResult.from_dict(obj.get("reward")) if obj.get("reward") is not None else None,
            "gift": RedemptionEntryGift.from_dict(obj.get("gift")) if obj.get("gift") is not None else None,
            "loyalty_card": RedemptionEntryLoyaltyCard.from_dict(obj.get("loyalty_card")) if obj.get("loyalty_card") is not None else None,
            "reason": obj.get("reason")
        })
        return _obj


