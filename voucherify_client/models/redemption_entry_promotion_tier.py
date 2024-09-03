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
from voucherify_client.models.category import Category
from voucherify_client.models.redemption_entry_promotion_tier_action import RedemptionEntryPromotionTierAction
from voucherify_client.models.redemption_entry_promotion_tier_campaign import RedemptionEntryPromotionTierCampaign
from voucherify_client.models.redemption_entry_promotion_tier_summary import RedemptionEntryPromotionTierSummary
from voucherify_client.models.validation_rule_assignments_list import ValidationRuleAssignmentsList
from voucherify_client.models.validity_hours import ValidityHours
from voucherify_client.models.validity_timeframe import ValidityTimeframe

class RedemptionEntryPromotionTier(BaseModel):
    """
    RedemptionEntryPromotionTier
    """
    id: Optional[StrictStr] = Field(None, description="Unique promotion tier ID.")
    created_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the promotion tier was created. The value is shown in the ISO 8601 format.")
    updated_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the promotion tier was updated. The value is shown in the ISO 8601 format.")
    name: Optional[StrictStr] = Field(None, description="Name of the promotion tier.")
    banner: Optional[StrictStr] = Field(None, description="Text to be displayed to your customers on your website.")
    action: Optional[RedemptionEntryPromotionTierAction] = None
    metadata: Optional[Dict[str, Any]] = None
    hierarchy: Optional[StrictInt] = Field(None, description="The promotions hierarchy defines the order in which the discounts from different tiers will be applied to a customer's order. If a customer qualifies for discounts from more than one tier, discounts will be applied in the order defined in the hierarchy.")
    promotion_id: Optional[StrictStr] = Field(None, description="Promotion unique ID.")
    campaign: Optional[RedemptionEntryPromotionTierCampaign] = None
    campaign_id: Optional[StrictStr] = Field(None, description="Promotion tier's parent campaign's unique ID.")
    active: Optional[StrictBool] = Field(None, description="A flag to toggle the promotion tier on or off. You can disable a promotion tier even though it's within the active period defined by the `start_date` and `expiration_date`.    - `true` indicates an *active* promotion tier - `false` indicates an *inactive* promotion tier")
    start_date: Optional[datetime] = Field(None, description="Activation timestamp defines when the promotion tier starts to be active in ISO 8601 format. Promotion tier is *inactive before* this date. ")
    expiration_date: Optional[datetime] = Field(None, description="Activation timestamp defines when the promotion tier expires in ISO 8601 format. Promotion tier is *inactive after* this date. ")
    validity_timeframe: Optional[ValidityTimeframe] = None
    validity_day_of_week: Optional[conlist(StrictInt)] = Field(None, description="Integer array corresponding to the particular days of the week in which the voucher is valid.  - `0` Sunday - `1` Monday - `2` Tuesday - `3` Wednesday - `4` Thursday - `5` Friday - `6` Saturday")
    validity_hours: Optional[ValidityHours] = None
    summary: Optional[RedemptionEntryPromotionTierSummary] = None
    object: Optional[StrictStr] = Field('promotion_tier', description="The type of the object represented by JSON. This object stores information about the promotion tier.")
    validation_rule_assignments: Optional[ValidationRuleAssignmentsList] = None
    category_id: Optional[StrictStr] = Field(None, description="Promotion tier category ID.")
    categories: Optional[conlist(Category)] = None
    __properties = ["id", "created_at", "updated_at", "name", "banner", "action", "metadata", "hierarchy", "promotion_id", "campaign", "campaign_id", "active", "start_date", "expiration_date", "validity_timeframe", "validity_day_of_week", "validity_hours", "summary", "object", "validation_rule_assignments", "category_id", "categories"]

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
    def from_json(cls, json_str: str) -> RedemptionEntryPromotionTier:
        """Create an instance of RedemptionEntryPromotionTier from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of action
        if self.action:
            _dict['action'] = self.action.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaign
        if self.campaign:
            _dict['campaign'] = self.campaign.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_timeframe
        if self.validity_timeframe:
            _dict['validity_timeframe'] = self.validity_timeframe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_hours
        if self.validity_hours:
            _dict['validity_hours'] = self.validity_hours.to_dict()
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validation_rule_assignments
        if self.validation_rule_assignments:
            _dict['validation_rule_assignments'] = self.validation_rule_assignments.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item in self.categories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['categories'] = _items
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if banner (nullable) is None
        # and __fields_set__ contains the field
        if self.banner is None and "banner" in self.__fields_set__:
            _dict['banner'] = None

        # set to None if action (nullable) is None
        # and __fields_set__ contains the field
        if self.action is None and "action" in self.__fields_set__:
            _dict['action'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        # set to None if hierarchy (nullable) is None
        # and __fields_set__ contains the field
        if self.hierarchy is None and "hierarchy" in self.__fields_set__:
            _dict['hierarchy'] = None

        # set to None if promotion_id (nullable) is None
        # and __fields_set__ contains the field
        if self.promotion_id is None and "promotion_id" in self.__fields_set__:
            _dict['promotion_id'] = None

        # set to None if campaign (nullable) is None
        # and __fields_set__ contains the field
        if self.campaign is None and "campaign" in self.__fields_set__:
            _dict['campaign'] = None

        # set to None if campaign_id (nullable) is None
        # and __fields_set__ contains the field
        if self.campaign_id is None and "campaign_id" in self.__fields_set__:
            _dict['campaign_id'] = None

        # set to None if active (nullable) is None
        # and __fields_set__ contains the field
        if self.active is None and "active" in self.__fields_set__:
            _dict['active'] = None

        # set to None if start_date (nullable) is None
        # and __fields_set__ contains the field
        if self.start_date is None and "start_date" in self.__fields_set__:
            _dict['start_date'] = None

        # set to None if expiration_date (nullable) is None
        # and __fields_set__ contains the field
        if self.expiration_date is None and "expiration_date" in self.__fields_set__:
            _dict['expiration_date'] = None

        # set to None if summary (nullable) is None
        # and __fields_set__ contains the field
        if self.summary is None and "summary" in self.__fields_set__:
            _dict['summary'] = None

        # set to None if object (nullable) is None
        # and __fields_set__ contains the field
        if self.object is None and "object" in self.__fields_set__:
            _dict['object'] = None

        # set to None if category_id (nullable) is None
        # and __fields_set__ contains the field
        if self.category_id is None and "category_id" in self.__fields_set__:
            _dict['category_id'] = None

        # set to None if categories (nullable) is None
        # and __fields_set__ contains the field
        if self.categories is None and "categories" in self.__fields_set__:
            _dict['categories'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RedemptionEntryPromotionTier:
        """Create an instance of RedemptionEntryPromotionTier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RedemptionEntryPromotionTier.parse_obj(obj)

        _obj = RedemptionEntryPromotionTier.parse_obj({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "name": obj.get("name"),
            "banner": obj.get("banner"),
            "action": RedemptionEntryPromotionTierAction.from_dict(obj.get("action")) if obj.get("action") is not None else None,
            "metadata": obj.get("metadata"),
            "hierarchy": obj.get("hierarchy"),
            "promotion_id": obj.get("promotion_id"),
            "campaign": RedemptionEntryPromotionTierCampaign.from_dict(obj.get("campaign")) if obj.get("campaign") is not None else None,
            "campaign_id": obj.get("campaign_id"),
            "active": obj.get("active"),
            "start_date": obj.get("start_date"),
            "expiration_date": obj.get("expiration_date"),
            "validity_timeframe": ValidityTimeframe.from_dict(obj.get("validity_timeframe")) if obj.get("validity_timeframe") is not None else None,
            "validity_day_of_week": obj.get("validity_day_of_week"),
            "validity_hours": ValidityHours.from_dict(obj.get("validity_hours")) if obj.get("validity_hours") is not None else None,
            "summary": RedemptionEntryPromotionTierSummary.from_dict(obj.get("summary")) if obj.get("summary") is not None else None,
            "object": obj.get("object") if obj.get("object") is not None else 'promotion_tier',
            "validation_rule_assignments": ValidationRuleAssignmentsList.from_dict(obj.get("validation_rule_assignments")) if obj.get("validation_rule_assignments") is not None else None,
            "category_id": obj.get("category_id"),
            "categories": [Category.from_dict(_item) for _item in obj.get("categories")] if obj.get("categories") is not None else None
        })
        return _obj

