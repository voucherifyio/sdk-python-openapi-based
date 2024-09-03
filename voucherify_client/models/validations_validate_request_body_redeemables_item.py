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
from pydantic import BaseModel, StrictStr, validator
from voucherify_client.models.validations_validate_request_body_redeemables_item_gift import ValidationsValidateRequestBodyRedeemablesItemGift
from voucherify_client.models.validations_validate_request_body_redeemables_item_reward import ValidationsValidateRequestBodyRedeemablesItemReward

class ValidationsValidateRequestBodyRedeemablesItem(BaseModel):
    """
    ValidationsValidateRequestBodyRedeemablesItem
    """
    object: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    gift: Optional[ValidationsValidateRequestBodyRedeemablesItemGift] = None
    reward: Optional[ValidationsValidateRequestBodyRedeemablesItemReward] = None
    __properties = ["object", "id", "gift", "reward"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('voucher', 'promotion_tier', 'promotion_stack',):
            raise ValueError("must be one of enum values ('voucher', 'promotion_tier', 'promotion_stack')")
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
    def from_json(cls, json_str: str) -> ValidationsValidateRequestBodyRedeemablesItem:
        """Create an instance of ValidationsValidateRequestBodyRedeemablesItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of gift
        if self.gift:
            _dict['gift'] = self.gift.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reward
        if self.reward:
            _dict['reward'] = self.reward.to_dict()
        # set to None if gift (nullable) is None
        # and __fields_set__ contains the field
        if self.gift is None and "gift" in self.__fields_set__:
            _dict['gift'] = None

        # set to None if reward (nullable) is None
        # and __fields_set__ contains the field
        if self.reward is None and "reward" in self.__fields_set__:
            _dict['reward'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ValidationsValidateRequestBodyRedeemablesItem:
        """Create an instance of ValidationsValidateRequestBodyRedeemablesItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ValidationsValidateRequestBodyRedeemablesItem.parse_obj(obj)

        _obj = ValidationsValidateRequestBodyRedeemablesItem.parse_obj({
            "object": obj.get("object"),
            "id": obj.get("id"),
            "gift": ValidationsValidateRequestBodyRedeemablesItemGift.from_dict(obj.get("gift")) if obj.get("gift") is not None else None,
            "reward": ValidationsValidateRequestBodyRedeemablesItemReward.from_dict(obj.get("reward")) if obj.get("reward") is not None else None
        })
        return _obj


