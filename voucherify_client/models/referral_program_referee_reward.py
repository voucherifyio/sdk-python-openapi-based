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
from pydantic import BaseModel, Field, StrictStr, validator
from voucherify_client.models.referral_program_referee_reward_related_object_parent import ReferralProgramRefereeRewardRelatedObjectParent

class ReferralProgramRefereeReward(BaseModel):
    """
    Defines the referee reward.  # noqa: E501
    """
    related_object_parent: Optional[ReferralProgramRefereeRewardRelatedObjectParent] = None
    type: Optional[StrictStr] = Field(None, description="Type of reward.")
    amount: Optional[StrictStr] = Field(None, description="Define the number of `points` to add to a loyalty card or `credits` to the balance on a gift card. In case of the gift card, the value is multiplied by 100 to precisely represent 2 decimal places. For example, $100 amount is written as 10000.")
    __properties = ["related_object_parent", "type", "amount"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('DISCOUNT_VOUCHER', 'LOYALTY_CARD', 'GIFT_VOUCHER', 'LUCKY_DRAW_CODE',):
            raise ValueError("must be one of enum values ('DISCOUNT_VOUCHER', 'LOYALTY_CARD', 'GIFT_VOUCHER', 'LUCKY_DRAW_CODE')")
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
    def from_json(cls, json_str: str) -> ReferralProgramRefereeReward:
        """Create an instance of ReferralProgramRefereeReward from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of related_object_parent
        if self.related_object_parent:
            _dict['related_object_parent'] = self.related_object_parent.to_dict()
        # set to None if related_object_parent (nullable) is None
        # and __fields_set__ contains the field
        if self.related_object_parent is None and "related_object_parent" in self.__fields_set__:
            _dict['related_object_parent'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if amount (nullable) is None
        # and __fields_set__ contains the field
        if self.amount is None and "amount" in self.__fields_set__:
            _dict['amount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReferralProgramRefereeReward:
        """Create an instance of ReferralProgramRefereeReward from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReferralProgramRefereeReward.parse_obj(obj)

        _obj = ReferralProgramRefereeReward.parse_obj({
            "related_object_parent": ReferralProgramRefereeRewardRelatedObjectParent.from_dict(obj.get("related_object_parent")) if obj.get("related_object_parent") is not None else None,
            "type": obj.get("type"),
            "amount": obj.get("amount")
        })
        return _obj


