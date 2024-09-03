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
from pydantic import BaseModel, Field
from voucherify_client.models.loyalties_members_redemption_redeem_request_body_reward import LoyaltiesMembersRedemptionRedeemRequestBodyReward
from voucherify_client.models.order import Order

class LoyaltiesMembersRedemptionRedeemRequestBody(BaseModel):
    """
    Request body schema for **POST** `v1/loyalties/{campaignId}/members/{memberId}/redemption` and for **POST** `v1/loyalties/members/{memberId}/redemption`.  # noqa: E501
    """
    reward: Optional[LoyaltiesMembersRedemptionRedeemRequestBodyReward] = None
    order: Optional[Order] = None
    metadata: Optional[Dict[str, Any]] = Field(None, description="A set of key/value pairs that you can send in the request body to check against vouchers requiring **redemption** metadata validation rules to be satisfied. The validation runs against rules that are defined through the <!-- [Create Validation Rules](https://docs.voucherify.io/reference/create-validation-rules) -->[Create Validation Rules](ref:create-validation-rules) endpoint or via the Dashboard; in the _Advanced Rule Builder_ &rarr; _Advanced_ &rarr; _Redemption metadata satisfy_ or _Basic Builder_ &rarr; _Attributes match_ &rarr; _REDEMPTION METADATA_. [Read more](https://support.voucherify.io/article/148-how-to-build-a-rule).")
    __properties = ["reward", "order", "metadata"]

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
    def from_json(cls, json_str: str) -> LoyaltiesMembersRedemptionRedeemRequestBody:
        """Create an instance of LoyaltiesMembersRedemptionRedeemRequestBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # set to None if reward (nullable) is None
        # and __fields_set__ contains the field
        if self.reward is None and "reward" in self.__fields_set__:
            _dict['reward'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltiesMembersRedemptionRedeemRequestBody:
        """Create an instance of LoyaltiesMembersRedemptionRedeemRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesMembersRedemptionRedeemRequestBody.parse_obj(obj)

        _obj = LoyaltiesMembersRedemptionRedeemRequestBody.parse_obj({
            "reward": LoyaltiesMembersRedemptionRedeemRequestBodyReward.from_dict(obj.get("reward")) if obj.get("reward") is not None else None,
            "order": Order.from_dict(obj.get("order")) if obj.get("order") is not None else None,
            "metadata": obj.get("metadata")
        })
        return _obj


