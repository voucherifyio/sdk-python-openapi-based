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
from openapi_client.models.redeemable_result_promotion_tier_discount import RedeemableResultPromotionTierDiscount

class RedeemableResultVoucherCode(BaseModel):
    """
    This is a `result` object representing the results for a coupon code.  # noqa: E501
    """
    discount: Optional[RedeemableResultPromotionTierDiscount] = None
    __properties = ["discount"]

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
    def from_json(cls, json_str: str) -> RedeemableResultVoucherCode:
        """Create an instance of RedeemableResultVoucherCode from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of discount
        if self.discount:
            _dict['discount'] = self.discount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RedeemableResultVoucherCode:
        """Create an instance of RedeemableResultVoucherCode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RedeemableResultVoucherCode.parse_obj(obj)

        _obj = RedeemableResultVoucherCode.parse_obj({
            "discount": RedeemableResultPromotionTierDiscount.from_dict(obj.get("discount")) if obj.get("discount") is not None else None
        })
        return _obj


