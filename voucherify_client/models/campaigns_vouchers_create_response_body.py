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
from voucherify_client.models.campaigns_vouchers_create_response_body_gift import CampaignsVouchersCreateResponseBodyGift
from voucherify_client.models.campaigns_vouchers_create_response_body_loyalty_card import CampaignsVouchersCreateResponseBodyLoyaltyCard
from voucherify_client.models.campaigns_vouchers_create_response_body_publish import CampaignsVouchersCreateResponseBodyPublish
from voucherify_client.models.campaigns_vouchers_create_response_body_redemption import CampaignsVouchersCreateResponseBodyRedemption
from voucherify_client.models.category import Category
from voucherify_client.models.discount import Discount
from voucherify_client.models.validation_rules_assignments_list import ValidationRulesAssignmentsList
from voucherify_client.models.validity_hours import ValidityHours
from voucherify_client.models.validity_timeframe import ValidityTimeframe
from voucherify_client.models.voucher_assets import VoucherAssets

class CampaignsVouchersCreateResponseBody(BaseModel):
    """
    Response body schema for **POST** `v1/campaigns/{campaignId}/vouchers/{code}` and **POST** `v1/campaigns/{campaignId}/vouchers`.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="Assigned by the Voucherify API, identifies the voucher.")
    code: Optional[StrictStr] = Field(None, description="A code that identifies a voucher. Pattern can use all letters of the English alphabet, Arabic numerals, and special characters.")
    campaign: Optional[StrictStr] = Field(None, description="A unique campaign name, identifies the voucher's parent campaign.")
    campaign_id: Optional[StrictStr] = Field(None, description="Assigned by the Voucherify API, identifies the voucher's parent campaign.")
    category: Optional[StrictStr] = Field(None, description="Tag defining the category that this voucher belongs to. Useful when listing vouchers using the List Vouchers endpoint.")
    category_id: Optional[StrictStr] = Field(None, description="Unique category ID assigned by Voucherify.")
    type: Optional[StrictStr] = Field(None, description="Defines the type of the voucher. ")
    discount: Optional[Discount] = None
    gift: Optional[CampaignsVouchersCreateResponseBodyGift] = None
    loyalty_card: Optional[CampaignsVouchersCreateResponseBodyLoyaltyCard] = None
    start_date: Optional[datetime] = Field(None, description="Activation timestamp defines when the code starts to be active in ISO 8601 format. Voucher is *inactive before* this date. ")
    expiration_date: Optional[datetime] = Field(None, description="Expiration timestamp defines when the code expires in ISO 8601 format.  Voucher is *inactive after* this date.")
    validity_timeframe: Optional[ValidityTimeframe] = None
    validity_day_of_week: Optional[conlist(StrictInt)] = Field(None, description="Integer array corresponding to the particular days of the week in which the voucher is valid.  - `0` Sunday - `1` Monday - `2` Tuesday - `3` Wednesday - `4` Thursday - `5` Friday - `6` Saturday")
    validity_hours: Optional[ValidityHours] = None
    active: Optional[StrictBool] = Field(None, description="A flag to toggle the voucher on or off. You can disable a voucher even though it's within the active period defined by the `start_date` and `expiration_date`.    - `true` indicates an *active* voucher - `false` indicates an *inactive* voucher")
    additional_info: Optional[StrictStr] = Field(None, description="An optional field to keep any extra textual information about the code such as a code description and details.")
    metadata: Optional[Dict[str, Any]] = Field(None, description="The metadata object stores all custom attributes assigned to the code. A set of key/value pairs that you can attach to a voucher object. It can be useful for storing additional information about the voucher in a structured format.")
    assets: Optional[VoucherAssets] = None
    is_referral_code: Optional[StrictBool] = Field(None, description="Flag indicating whether this voucher is a referral code; `true` for campaign type `REFERRAL_PROGRAM`.")
    created_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the voucher was created. The value is shown in the ISO 8601 format.")
    updated_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the voucher was last updated in ISO 8601 format.")
    holder_id: Optional[StrictStr] = Field(None, description="Unique customer identifier of the redeemable holder. It equals to the customer ID assigned by Voucherify.")
    referrer_id: Optional[StrictStr] = Field(None, description="Unique identifier of the referring person.")
    object: Optional[StrictStr] = Field('voucher', description="The type of the object represented by JSON. Default is `voucher`.")
    publish: Optional[CampaignsVouchersCreateResponseBodyPublish] = None
    redemption: Optional[CampaignsVouchersCreateResponseBodyRedemption] = None
    categories: Optional[conlist(Category)] = Field(None, description="Contains details about the category.")
    validation_rules_assignments: Optional[ValidationRulesAssignmentsList] = None
    __properties = ["id", "code", "campaign", "campaign_id", "category", "category_id", "type", "discount", "gift", "loyalty_card", "start_date", "expiration_date", "validity_timeframe", "validity_day_of_week", "validity_hours", "active", "additional_info", "metadata", "assets", "is_referral_code", "created_at", "updated_at", "holder_id", "referrer_id", "object", "publish", "redemption", "categories", "validation_rules_assignments"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('GIFT_VOUCHER', 'DISCOUNT_VOUCHER', 'LOYALTY_CARD',):
            raise ValueError("must be one of enum values ('GIFT_VOUCHER', 'DISCOUNT_VOUCHER', 'LOYALTY_CARD')")
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
    def from_json(cls, json_str: str) -> CampaignsVouchersCreateResponseBody:
        """Create an instance of CampaignsVouchersCreateResponseBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of gift
        if self.gift:
            _dict['gift'] = self.gift.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loyalty_card
        if self.loyalty_card:
            _dict['loyalty_card'] = self.loyalty_card.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_timeframe
        if self.validity_timeframe:
            _dict['validity_timeframe'] = self.validity_timeframe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_hours
        if self.validity_hours:
            _dict['validity_hours'] = self.validity_hours.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of publish
        if self.publish:
            _dict['publish'] = self.publish.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redemption
        if self.redemption:
            _dict['redemption'] = self.redemption.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item in self.categories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['categories'] = _items
        # override the default output from pydantic by calling `to_dict()` of validation_rules_assignments
        if self.validation_rules_assignments:
            _dict['validation_rules_assignments'] = self.validation_rules_assignments.to_dict()
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if code (nullable) is None
        # and __fields_set__ contains the field
        if self.code is None and "code" in self.__fields_set__:
            _dict['code'] = None

        # set to None if campaign (nullable) is None
        # and __fields_set__ contains the field
        if self.campaign is None and "campaign" in self.__fields_set__:
            _dict['campaign'] = None

        # set to None if campaign_id (nullable) is None
        # and __fields_set__ contains the field
        if self.campaign_id is None and "campaign_id" in self.__fields_set__:
            _dict['campaign_id'] = None

        # set to None if category (nullable) is None
        # and __fields_set__ contains the field
        if self.category is None and "category" in self.__fields_set__:
            _dict['category'] = None

        # set to None if category_id (nullable) is None
        # and __fields_set__ contains the field
        if self.category_id is None and "category_id" in self.__fields_set__:
            _dict['category_id'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if gift (nullable) is None
        # and __fields_set__ contains the field
        if self.gift is None and "gift" in self.__fields_set__:
            _dict['gift'] = None

        # set to None if loyalty_card (nullable) is None
        # and __fields_set__ contains the field
        if self.loyalty_card is None and "loyalty_card" in self.__fields_set__:
            _dict['loyalty_card'] = None

        # set to None if start_date (nullable) is None
        # and __fields_set__ contains the field
        if self.start_date is None and "start_date" in self.__fields_set__:
            _dict['start_date'] = None

        # set to None if expiration_date (nullable) is None
        # and __fields_set__ contains the field
        if self.expiration_date is None and "expiration_date" in self.__fields_set__:
            _dict['expiration_date'] = None

        # set to None if active (nullable) is None
        # and __fields_set__ contains the field
        if self.active is None and "active" in self.__fields_set__:
            _dict['active'] = None

        # set to None if additional_info (nullable) is None
        # and __fields_set__ contains the field
        if self.additional_info is None and "additional_info" in self.__fields_set__:
            _dict['additional_info'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        # set to None if is_referral_code (nullable) is None
        # and __fields_set__ contains the field
        if self.is_referral_code is None and "is_referral_code" in self.__fields_set__:
            _dict['is_referral_code'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        # set to None if holder_id (nullable) is None
        # and __fields_set__ contains the field
        if self.holder_id is None and "holder_id" in self.__fields_set__:
            _dict['holder_id'] = None

        # set to None if referrer_id (nullable) is None
        # and __fields_set__ contains the field
        if self.referrer_id is None and "referrer_id" in self.__fields_set__:
            _dict['referrer_id'] = None

        # set to None if object (nullable) is None
        # and __fields_set__ contains the field
        if self.object is None and "object" in self.__fields_set__:
            _dict['object'] = None

        # set to None if publish (nullable) is None
        # and __fields_set__ contains the field
        if self.publish is None and "publish" in self.__fields_set__:
            _dict['publish'] = None

        # set to None if redemption (nullable) is None
        # and __fields_set__ contains the field
        if self.redemption is None and "redemption" in self.__fields_set__:
            _dict['redemption'] = None

        # set to None if categories (nullable) is None
        # and __fields_set__ contains the field
        if self.categories is None and "categories" in self.__fields_set__:
            _dict['categories'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CampaignsVouchersCreateResponseBody:
        """Create an instance of CampaignsVouchersCreateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CampaignsVouchersCreateResponseBody.parse_obj(obj)

        _obj = CampaignsVouchersCreateResponseBody.parse_obj({
            "id": obj.get("id"),
            "code": obj.get("code"),
            "campaign": obj.get("campaign"),
            "campaign_id": obj.get("campaign_id"),
            "category": obj.get("category"),
            "category_id": obj.get("category_id"),
            "type": obj.get("type"),
            "discount": Discount.from_dict(obj.get("discount")) if obj.get("discount") is not None else None,
            "gift": CampaignsVouchersCreateResponseBodyGift.from_dict(obj.get("gift")) if obj.get("gift") is not None else None,
            "loyalty_card": CampaignsVouchersCreateResponseBodyLoyaltyCard.from_dict(obj.get("loyalty_card")) if obj.get("loyalty_card") is not None else None,
            "start_date": obj.get("start_date"),
            "expiration_date": obj.get("expiration_date"),
            "validity_timeframe": ValidityTimeframe.from_dict(obj.get("validity_timeframe")) if obj.get("validity_timeframe") is not None else None,
            "validity_day_of_week": obj.get("validity_day_of_week"),
            "validity_hours": ValidityHours.from_dict(obj.get("validity_hours")) if obj.get("validity_hours") is not None else None,
            "active": obj.get("active"),
            "additional_info": obj.get("additional_info"),
            "metadata": obj.get("metadata"),
            "assets": VoucherAssets.from_dict(obj.get("assets")) if obj.get("assets") is not None else None,
            "is_referral_code": obj.get("is_referral_code"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "holder_id": obj.get("holder_id"),
            "referrer_id": obj.get("referrer_id"),
            "object": obj.get("object") if obj.get("object") is not None else 'voucher',
            "publish": CampaignsVouchersCreateResponseBodyPublish.from_dict(obj.get("publish")) if obj.get("publish") is not None else None,
            "redemption": CampaignsVouchersCreateResponseBodyRedemption.from_dict(obj.get("redemption")) if obj.get("redemption") is not None else None,
            "categories": [Category.from_dict(_item) for _item in obj.get("categories")] if obj.get("categories") is not None else None,
            "validation_rules_assignments": ValidationRulesAssignmentsList.from_dict(obj.get("validation_rules_assignments")) if obj.get("validation_rules_assignments") is not None else None
        })
        return _obj


