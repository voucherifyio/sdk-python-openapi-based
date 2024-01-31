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
from voucherify_client.models.campaign_base_validity_timeframe import CampaignBaseValidityTimeframe
from voucherify_client.models.campaign_voucher import CampaignVoucher
from voucherify_client.models.category import Category
from voucherify_client.models.loyalty_tiers_expiration_all import LoyaltyTiersExpirationAll
from voucherify_client.models.promotion_tiers_list import PromotionTiersList
from voucherify_client.models.referral_program import ReferralProgram
from voucherify_client.models.validation_rules_assignments_list import ValidationRulesAssignmentsList

class CampaignsCreateResponseBody(BaseModel):
    """
    Response body schema for **POST** `/campaigns/{campaignId}`.  # noqa: E501
    """
    id: StrictStr = Field(..., description="Unique campaign ID, assigned by Voucherify.")
    name: StrictStr = Field(..., description="Campaign name.")
    description: Optional[StrictStr] = Field(None, description="An optional field to keep any extra textual information about the campaign such as a campaign description and details.")
    campaign_type: StrictStr = Field(..., description="Type of campaign.")
    type: StrictStr = Field(..., description="Defines whether the campaign can be updated with new vouchers after campaign creation.      - `AUTO_UPDATE`: the campaign is dynamic, i.e. vouchers will generate based on set criteria     -  `STATIC`: vouchers need to be manually published")
    voucher: Optional[CampaignVoucher] = None
    auto_join: StrictBool = Field(..., description="Indicates whether customers will be able to auto-join a loyalty campaign if any earning rule is fulfilled.")
    join_once: StrictBool = Field(..., description="If this value is set to `true`, customers will be able to join the campaign only once.")
    use_voucher_metadata_schema: StrictBool = Field(..., description="Flag indicating whether the campaign is to use the voucher's metadata schema instead of the campaign metadata schema.")
    validity_timeframe: Optional[CampaignBaseValidityTimeframe] = None
    validity_day_of_week: Optional[conlist(StrictInt)] = Field(None, description="Integer array corresponding to the particular days of the week in which the campaign is valid.  - `0`  Sunday   - `1`  Monday   - `2`  Tuesday   - `3`  Wednesday   - `4`  Thursday   - `5`  Friday   - `6`  Saturday  ")
    activity_duration_after_publishing: Optional[StrictStr] = Field(None, description="Defines the amount of time the campaign will be active in ISO 8601 format after publishing. For example, a campaign with a `duration` of `P24D` will be valid for a duration of 24 days.")
    vouchers_count: Optional[StrictInt] = Field(None, description="Total number of unique vouchers in campaign.")
    start_date: Optional[datetime] = Field(None, description="Activation timestamp defines when the campaign starts to be active in ISO 8601 format. Campaign is *inactive before* this date. ")
    expiration_date: Optional[datetime] = Field(None, description="Expiration timestamp defines when the campaign expires in ISO 8601 format.  Campaign is *inactive after* this date.")
    active: Optional[StrictBool] = Field(None, description="A flag to toggle the campaign on or off. You can disable a campaign even though it's within the active period defined by the `start_date` and `expiration_date`.    - `true` indicates an *active* campaign - `false` indicates an *inactive* campaign")
    metadata: Optional[Dict[str, Any]] = Field(None, description="The metadata object stores all custom attributes assigned to the campaign. A set of key/value pairs that you can attach to a campaign object. It can be useful for storing additional information about the campaign in a structured format.")
    created_at: datetime = Field(..., description="Timestamp representing the date and time when the campaign was created in ISO 8601 format.")
    updated_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the voucher was updated in ISO 8601 format.")
    category: Optional[StrictStr] = Field(None, description="Unique category name.")
    creation_status: StrictStr = Field(..., description="Indicates the status of the campaign creation.")
    vouchers_generation_status: StrictStr = Field(..., description="Indicates the status of the campaign's vouchers.")
    protected: StrictBool = Field(..., description="Indicates whether the resource can be deleted.")
    category_id: Optional[StrictStr] = Field(None, description="Unique category ID that this campaign belongs to.")
    categories: conlist(Category) = Field(..., description="Contains details about the category.")
    object: StrictStr = Field(..., description="The type of object represented by JSON. This object stores information about the campaign.")
    referral_program: Optional[ReferralProgram] = None
    loyalty_tiers_expiration: Optional[LoyaltyTiersExpirationAll] = None
    promotion: Optional[PromotionTiersList] = None
    validation_rules_assignments: Optional[ValidationRulesAssignmentsList] = None
    __properties = ["id", "name", "description", "campaign_type", "type", "voucher", "auto_join", "join_once", "use_voucher_metadata_schema", "validity_timeframe", "validity_day_of_week", "activity_duration_after_publishing", "vouchers_count", "start_date", "expiration_date", "active", "metadata", "created_at", "updated_at", "category", "creation_status", "vouchers_generation_status", "protected", "category_id", "categories", "object", "referral_program", "loyalty_tiers_expiration", "promotion", "validation_rules_assignments"]

    @validator('campaign_type')
    def campaign_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('LOYALTY_PROGRAM', 'GIFT_VOUCHERS', 'DISCOUNT_COUPONS', 'PROMOTION', 'REFERRAL_PROGRAM', 'LUCKY_DRAW',):
            raise ValueError("must be one of enum values ('LOYALTY_PROGRAM', 'GIFT_VOUCHERS', 'DISCOUNT_COUPONS', 'PROMOTION', 'REFERRAL_PROGRAM', 'LUCKY_DRAW')")
        return value

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('AUTO_UPDATE', 'STATIC',):
            raise ValueError("must be one of enum values ('AUTO_UPDATE', 'STATIC')")
        return value

    @validator('creation_status')
    def creation_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('DONE', 'IN_PROGRESS', 'FAILED', 'DRAFT', 'MODIFYING',):
            raise ValueError("must be one of enum values ('DONE', 'IN_PROGRESS', 'FAILED', 'DRAFT', 'MODIFYING')")
        return value

    @validator('vouchers_generation_status')
    def vouchers_generation_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('DONE', 'IN_PROGRESS', 'FAILED', 'DRAFT', 'MODIFYING',):
            raise ValueError("must be one of enum values ('DONE', 'IN_PROGRESS', 'FAILED', 'DRAFT', 'MODIFYING')")
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
    def from_json(cls, json_str: str) -> CampaignsCreateResponseBody:
        """Create an instance of CampaignsCreateResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of voucher
        if self.voucher:
            _dict['voucher'] = self.voucher.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_timeframe
        if self.validity_timeframe:
            _dict['validity_timeframe'] = self.validity_timeframe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item in self.categories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['categories'] = _items
        # override the default output from pydantic by calling `to_dict()` of referral_program
        if self.referral_program:
            _dict['referral_program'] = self.referral_program.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loyalty_tiers_expiration
        if self.loyalty_tiers_expiration:
            _dict['loyalty_tiers_expiration'] = self.loyalty_tiers_expiration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of promotion
        if self.promotion:
            _dict['promotion'] = self.promotion.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validation_rules_assignments
        if self.validation_rules_assignments:
            _dict['validation_rules_assignments'] = self.validation_rules_assignments.to_dict()
        # set to None if category_id (nullable) is None
        # and __fields_set__ contains the field
        if self.category_id is None and "category_id" in self.__fields_set__:
            _dict['category_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CampaignsCreateResponseBody:
        """Create an instance of CampaignsCreateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CampaignsCreateResponseBody.parse_obj(obj)

        _obj = CampaignsCreateResponseBody.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "campaign_type": obj.get("campaign_type"),
            "type": obj.get("type"),
            "voucher": CampaignVoucher.from_dict(obj.get("voucher")) if obj.get("voucher") is not None else None,
            "auto_join": obj.get("auto_join"),
            "join_once": obj.get("join_once"),
            "use_voucher_metadata_schema": obj.get("use_voucher_metadata_schema"),
            "validity_timeframe": CampaignBaseValidityTimeframe.from_dict(obj.get("validity_timeframe")) if obj.get("validity_timeframe") is not None else None,
            "validity_day_of_week": obj.get("validity_day_of_week"),
            "activity_duration_after_publishing": obj.get("activity_duration_after_publishing"),
            "vouchers_count": obj.get("vouchers_count"),
            "start_date": obj.get("start_date"),
            "expiration_date": obj.get("expiration_date"),
            "active": obj.get("active"),
            "metadata": obj.get("metadata"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "category": obj.get("category"),
            "creation_status": obj.get("creation_status"),
            "vouchers_generation_status": obj.get("vouchers_generation_status"),
            "protected": obj.get("protected"),
            "category_id": obj.get("category_id"),
            "categories": [Category.from_dict(_item) for _item in obj.get("categories")] if obj.get("categories") is not None else None,
            "object": obj.get("object") if obj.get("object") is not None else 'campaign',
            "referral_program": ReferralProgram.from_dict(obj.get("referral_program")) if obj.get("referral_program") is not None else None,
            "loyalty_tiers_expiration": LoyaltyTiersExpirationAll.from_dict(obj.get("loyalty_tiers_expiration")) if obj.get("loyalty_tiers_expiration") is not None else None,
            "promotion": PromotionTiersList.from_dict(obj.get("promotion")) if obj.get("promotion") is not None else None,
            "validation_rules_assignments": ValidationRulesAssignmentsList.from_dict(obj.get("validation_rules_assignments")) if obj.get("validation_rules_assignments") is not None else None
        })
        return _obj


