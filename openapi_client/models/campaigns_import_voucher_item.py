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
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator
from openapi_client.models.campaign_base_validity_timeframe import CampaignBaseValidityTimeframe
from openapi_client.models.campaigns_import_voucher_item_redemption import CampaignsImportVoucherItemRedemption
from openapi_client.models.campaigns_import_voucher_loyalty_card import CampaignsImportVoucherLoyaltyCard
from openapi_client.models.discount import Discount
from openapi_client.models.gift import Gift

class CampaignsImportVoucherItem(BaseModel):
    """
    Import Vouchers to Campaign  # noqa: E501
    """
    code: StrictStr = Field(..., description="Unique custom voucher code.")
    type: Optional[StrictStr] = Field(None, description="Type of voucher.")
    redemption: Optional[CampaignsImportVoucherItemRedemption] = None
    active: Optional[StrictBool] = Field(None, description="A flag to toggle the voucher on or off. You can disable a voucher even though it's within the active period defined by the `start_date` and `expiration_date`.    - `true` indicates an *active* voucher - `false` indicates an *inactive* voucher")
    metadata: Optional[Dict[str, Any]] = Field(None, description="The metadata object stores all custom attributes assigned to the voucher. A set of key/value pairs that you can attach to a voucher object. It can be useful for storing additional information about the voucher in a structured format.")
    category: Optional[StrictStr] = Field(None, description="The category assigned to the campaign. Either pass this parameter OR the `category_id`.")
    start_date: Optional[datetime] = Field(None, description="Activation timestamp defines when the campaign starts to be active in ISO 8601 format. Campaign is *inactive before* this date. ")
    validity_timeframe: Optional[CampaignBaseValidityTimeframe] = None
    validity_day_of_week: Optional[conlist(StrictInt)] = Field(None, description="Integer array corresponding to the particular days of the week in which the campaign is valid.  - `0`  Sunday   - `1`  Monday   - `2`  Tuesday   - `3`  Wednesday   - `4`  Thursday   - `5`  Friday   - `6`  Saturday  ")
    additional_info: Optional[StrictStr] = Field(None, description="An optional field to keep any extra textual information about the code such as a code description and details.")
    discount: Optional[Discount] = None
    gift: Optional[Gift] = None
    loyalty_card: Optional[CampaignsImportVoucherLoyaltyCard] = None
    __properties = ["code", "type", "redemption", "active", "metadata", "category", "start_date", "validity_timeframe", "validity_day_of_week", "additional_info", "discount", "gift", "loyalty_card"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('DISCOUNT_VOUCHER', 'GIFT_VOUCHER', 'LOYALTY_CARD', 'LUCKY_DRAW_CODE',):
            raise ValueError("must be one of enum values ('DISCOUNT_VOUCHER', 'GIFT_VOUCHER', 'LOYALTY_CARD', 'LUCKY_DRAW_CODE')")
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
    def from_json(cls, json_str: str) -> CampaignsImportVoucherItem:
        """Create an instance of CampaignsImportVoucherItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of redemption
        if self.redemption:
            _dict['redemption'] = self.redemption.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_timeframe
        if self.validity_timeframe:
            _dict['validity_timeframe'] = self.validity_timeframe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discount
        if self.discount:
            _dict['discount'] = self.discount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gift
        if self.gift:
            _dict['gift'] = self.gift.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loyalty_card
        if self.loyalty_card:
            _dict['loyalty_card'] = self.loyalty_card.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CampaignsImportVoucherItem:
        """Create an instance of CampaignsImportVoucherItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CampaignsImportVoucherItem.parse_obj(obj)

        _obj = CampaignsImportVoucherItem.parse_obj({
            "code": obj.get("code"),
            "type": obj.get("type"),
            "redemption": CampaignsImportVoucherItemRedemption.from_dict(obj.get("redemption")) if obj.get("redemption") is not None else None,
            "active": obj.get("active"),
            "metadata": obj.get("metadata"),
            "category": obj.get("category"),
            "start_date": obj.get("start_date"),
            "validity_timeframe": CampaignBaseValidityTimeframe.from_dict(obj.get("validity_timeframe")) if obj.get("validity_timeframe") is not None else None,
            "validity_day_of_week": obj.get("validity_day_of_week"),
            "additional_info": obj.get("additional_info"),
            "discount": Discount.from_dict(obj.get("discount")) if obj.get("discount") is not None else None,
            "gift": Gift.from_dict(obj.get("gift")) if obj.get("gift") is not None else None,
            "loyalty_card": CampaignsImportVoucherLoyaltyCard.from_dict(obj.get("loyalty_card")) if obj.get("loyalty_card") is not None else None
        })
        return _obj


