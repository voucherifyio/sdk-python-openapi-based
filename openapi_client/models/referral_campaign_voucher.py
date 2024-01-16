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
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator
from openapi_client.models.campaign_loyalty_voucher_redemption import CampaignLoyaltyVoucherRedemption
from openapi_client.models.code_config import CodeConfig
from openapi_client.models.discount import Discount

class ReferralCampaignVoucher(BaseModel):
    """
    ReferralCampaignVoucher
    """
    type: StrictStr = Field(..., description="Type of voucher.")
    discount: Discount = Field(...)
    code_config: Optional[CodeConfig] = None
    redemption: Optional[CampaignLoyaltyVoucherRedemption] = None
    is_referral_code: StrictBool = Field(..., description="Flag indicating whether this voucher is a referral code; `true` for campaign type `REFERRAL_PROGRAM`.")
    __properties = ["type", "discount", "code_config", "redemption", "is_referral_code"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('DISCOUNT_VOUCHER',):
            raise ValueError("must be one of enum values ('DISCOUNT_VOUCHER')")
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
    def from_json(cls, json_str: str) -> ReferralCampaignVoucher:
        """Create an instance of ReferralCampaignVoucher from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of code_config
        if self.code_config:
            _dict['code_config'] = self.code_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redemption
        if self.redemption:
            _dict['redemption'] = self.redemption.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReferralCampaignVoucher:
        """Create an instance of ReferralCampaignVoucher from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReferralCampaignVoucher.parse_obj(obj)

        _obj = ReferralCampaignVoucher.parse_obj({
            "type": obj.get("type") if obj.get("type") is not None else 'DISCOUNT_VOUCHER',
            "discount": Discount.from_dict(obj.get("discount")) if obj.get("discount") is not None else None,
            "code_config": CodeConfig.from_dict(obj.get("code_config")) if obj.get("code_config") is not None else None,
            "redemption": CampaignLoyaltyVoucherRedemption.from_dict(obj.get("redemption")) if obj.get("redemption") is not None else None,
            "is_referral_code": obj.get("is_referral_code")
        })
        return _obj


