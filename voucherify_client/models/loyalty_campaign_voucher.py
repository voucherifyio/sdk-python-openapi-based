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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator
from voucherify_client.models.campaign_loyalty_card import CampaignLoyaltyCard
from voucherify_client.models.code_config import CodeConfig
from voucherify_client.models.loyalty_campaign_voucher_redemption import LoyaltyCampaignVoucherRedemption
from voucherify_client.models.validity_hours import ValidityHours
from voucherify_client.models.validity_timeframe import ValidityTimeframe

class LoyaltyCampaignVoucher(BaseModel):
    """
    Schema model for a campaign voucher.  # noqa: E501
    """
    type: Optional[StrictStr] = Field('LOYALTY_CARD', description="Type of voucher.")
    loyalty_card: Optional[CampaignLoyaltyCard] = None
    redemption: Optional[LoyaltyCampaignVoucherRedemption] = None
    code_config: CodeConfig = Field(...)
    is_referral_code: Optional[StrictBool] = Field(None, description="Always `false` for a loyalty card voucher")
    start_date: Optional[datetime] = Field(None, description="Activation timestamp defines when the campaign starts to be active in ISO 8601 format. Campaign is *inactive before* this date. ")
    expiration_date: Optional[datetime] = Field(None, description="Expiration timestamp defines when the campaign expires in ISO 8601 format.  Campaign is *inactive after* this date.")
    validity_timeframe: Optional[ValidityTimeframe] = None
    validity_day_of_week: Optional[conlist(StrictInt)] = Field(None, description="Integer array corresponding to the particular days of the week in which the voucher is valid.  - `0` Sunday - `1` Monday - `2` Tuesday - `3` Wednesday - `4` Thursday - `5` Friday - `6` Saturday")
    validity_hours: Optional[ValidityHours] = None
    __properties = ["type", "loyalty_card", "redemption", "code_config", "is_referral_code", "start_date", "expiration_date", "validity_timeframe", "validity_day_of_week", "validity_hours"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('LOYALTY_CARD',):
            raise ValueError("must be one of enum values ('LOYALTY_CARD')")
        return value

    @validator('validity_day_of_week')
    def validity_day_of_week_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in (0, 1, 2, 3, 4, 5, 6,):
                raise ValueError("each list item must be one of (0, 1, 2, 3, 4, 5, 6)")
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
    def from_json(cls, json_str: str) -> LoyaltyCampaignVoucher:
        """Create an instance of LoyaltyCampaignVoucher from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of loyalty_card
        if self.loyalty_card:
            _dict['loyalty_card'] = self.loyalty_card.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redemption
        if self.redemption:
            _dict['redemption'] = self.redemption.to_dict()
        # override the default output from pydantic by calling `to_dict()` of code_config
        if self.code_config:
            _dict['code_config'] = self.code_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_timeframe
        if self.validity_timeframe:
            _dict['validity_timeframe'] = self.validity_timeframe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_hours
        if self.validity_hours:
            _dict['validity_hours'] = self.validity_hours.to_dict()
        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if redemption (nullable) is None
        # and __fields_set__ contains the field
        if self.redemption is None and "redemption" in self.__fields_set__:
            _dict['redemption'] = None

        # set to None if is_referral_code (nullable) is None
        # and __fields_set__ contains the field
        if self.is_referral_code is None and "is_referral_code" in self.__fields_set__:
            _dict['is_referral_code'] = None

        # set to None if start_date (nullable) is None
        # and __fields_set__ contains the field
        if self.start_date is None and "start_date" in self.__fields_set__:
            _dict['start_date'] = None

        # set to None if expiration_date (nullable) is None
        # and __fields_set__ contains the field
        if self.expiration_date is None and "expiration_date" in self.__fields_set__:
            _dict['expiration_date'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltyCampaignVoucher:
        """Create an instance of LoyaltyCampaignVoucher from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltyCampaignVoucher.parse_obj(obj)

        _obj = LoyaltyCampaignVoucher.parse_obj({
            "type": obj.get("type") if obj.get("type") is not None else 'LOYALTY_CARD',
            "loyalty_card": CampaignLoyaltyCard.from_dict(obj.get("loyalty_card")) if obj.get("loyalty_card") is not None else None,
            "redemption": LoyaltyCampaignVoucherRedemption.from_dict(obj.get("redemption")) if obj.get("redemption") is not None else None,
            "code_config": CodeConfig.from_dict(obj.get("code_config")) if obj.get("code_config") is not None else None,
            "is_referral_code": obj.get("is_referral_code"),
            "start_date": obj.get("start_date"),
            "expiration_date": obj.get("expiration_date"),
            "validity_timeframe": ValidityTimeframe.from_dict(obj.get("validity_timeframe")) if obj.get("validity_timeframe") is not None else None,
            "validity_day_of_week": obj.get("validity_day_of_week"),
            "validity_hours": ValidityHours.from_dict(obj.get("validity_hours")) if obj.get("validity_hours") is not None else None
        })
        return _obj

