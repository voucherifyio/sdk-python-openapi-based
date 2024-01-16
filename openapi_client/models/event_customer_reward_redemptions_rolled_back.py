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
from pydantic import BaseModel, StrictInt, StrictStr
from openapi_client.models.reward_assignment import RewardAssignment
from openapi_client.models.simple_campaign import SimpleCampaign
from openapi_client.models.simple_customer import SimpleCustomer
from openapi_client.models.simple_redemption_reward_result import SimpleRedemptionRewardResult
from openapi_client.models.simple_voucher import SimpleVoucher

class EventCustomerRewardRedemptionsRolledBack(BaseModel):
    """
    Event data object schema for `customer.reward_redemptions.rolledback`.  # noqa: E501
    """
    customer: Optional[SimpleCustomer] = None
    holder: Optional[SimpleCustomer] = None
    voucher: Optional[SimpleVoucher] = None
    campaign: Optional[SimpleCampaign] = None
    reward_redemption: Optional[Dict[str, Any]] = None
    reward: Optional[SimpleRedemptionRewardResult] = None
    reward_assignment: Optional[RewardAssignment] = None
    source: Optional[StrictStr] = None
    balance: Optional[StrictInt] = None
    __properties = ["customer", "holder", "voucher", "campaign", "reward_redemption", "reward", "reward_assignment", "source", "balance"]

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
    def from_json(cls, json_str: str) -> EventCustomerRewardRedemptionsRolledBack:
        """Create an instance of EventCustomerRewardRedemptionsRolledBack from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of holder
        if self.holder:
            _dict['holder'] = self.holder.to_dict()
        # override the default output from pydantic by calling `to_dict()` of voucher
        if self.voucher:
            _dict['voucher'] = self.voucher.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaign
        if self.campaign:
            _dict['campaign'] = self.campaign.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reward
        if self.reward:
            _dict['reward'] = self.reward.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reward_assignment
        if self.reward_assignment:
            _dict['reward_assignment'] = self.reward_assignment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventCustomerRewardRedemptionsRolledBack:
        """Create an instance of EventCustomerRewardRedemptionsRolledBack from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventCustomerRewardRedemptionsRolledBack.parse_obj(obj)

        _obj = EventCustomerRewardRedemptionsRolledBack.parse_obj({
            "customer": SimpleCustomer.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "holder": SimpleCustomer.from_dict(obj.get("holder")) if obj.get("holder") is not None else None,
            "voucher": SimpleVoucher.from_dict(obj.get("voucher")) if obj.get("voucher") is not None else None,
            "campaign": SimpleCampaign.from_dict(obj.get("campaign")) if obj.get("campaign") is not None else None,
            "reward_redemption": obj.get("reward_redemption"),
            "reward": SimpleRedemptionRewardResult.from_dict(obj.get("reward")) if obj.get("reward") is not None else None,
            "reward_assignment": RewardAssignment.from_dict(obj.get("reward_assignment")) if obj.get("reward_assignment") is not None else None,
            "source": obj.get("source"),
            "balance": obj.get("balance")
        })
        return _obj


