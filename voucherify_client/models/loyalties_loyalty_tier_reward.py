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



from pydantic import BaseModel, Field, StrictStr, validator
from voucherify_client.models.reward import Reward
from voucherify_client.models.reward_assignment import RewardAssignment

class LoyaltiesLoyaltyTierReward(BaseModel):
    """
    This is an object representing a loyalty tier reward.  # noqa: E501
    """
    reward: Reward = Field(...)
    assignment: RewardAssignment = Field(...)
    object: StrictStr = Field(..., description="The type of the object represented by JSON. This object stores information about the loyalty tier reward.")
    __properties = ["reward", "assignment", "object"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('loyalty_tier_reward',):
            raise ValueError("must be one of enum values ('loyalty_tier_reward')")
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
    def from_json(cls, json_str: str) -> LoyaltiesLoyaltyTierReward:
        """Create an instance of LoyaltiesLoyaltyTierReward from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of reward
        if self.reward:
            _dict['reward'] = self.reward.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assignment
        if self.assignment:
            _dict['assignment'] = self.assignment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltiesLoyaltyTierReward:
        """Create an instance of LoyaltiesLoyaltyTierReward from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesLoyaltyTierReward.parse_obj(obj)

        _obj = LoyaltiesLoyaltyTierReward.parse_obj({
            "reward": Reward.from_dict(obj.get("reward")) if obj.get("reward") is not None else None,
            "assignment": RewardAssignment.from_dict(obj.get("assignment")) if obj.get("assignment") is not None else None,
            "object": obj.get("object") if obj.get("object") is not None else 'loyalty_tier_reward'
        })
        return _obj


