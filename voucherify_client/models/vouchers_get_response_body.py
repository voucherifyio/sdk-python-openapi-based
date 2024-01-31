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
from voucherify_client.models.discount import Discount
from voucherify_client.models.simple_customer import SimpleCustomer
from voucherify_client.models.validation_rules_assignments_list import ValidationRulesAssignmentsList
from voucherify_client.models.voucher_assets import VoucherAssets
from voucherify_client.models.voucher_gift import VoucherGift
from voucherify_client.models.voucher_loyalty_card import VoucherLoyaltyCard
from voucherify_client.models.voucher_publish import VoucherPublish
from voucherify_client.models.voucher_redemption import VoucherRedemption
from voucherify_client.models.voucher_validity_timeframe import VoucherValidityTimeframe

class VouchersGetResponseBody(BaseModel):
    """
    Response body schema for **GET** `/vouchers/{code}`.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="Assigned by the Voucherify API, identifies the voucher.")
    code: Optional[StrictStr] = Field(None, description="A code that identifies a voucher. Pattern can use all letters of the English alphabet, Arabic numerals, and special characters.")
    campaign: Optional[StrictStr] = Field(None, description="A unique campaign name, identifies the voucher's parent campaign.")
    campaign_id: Optional[StrictStr] = Field(None, description="Assigned by the Voucherify API, identifies the voucher's parent campaign.")
    category: Optional[StrictStr] = Field(None, description="Tag defining the category that this voucher belongs to. Useful when listing vouchers using the List Vouchers endpoint.")
    category_id: Optional[StrictStr] = Field(None, description="Unique category ID assigned by Voucherify.")
    categories: Optional[conlist(Category)] = Field(None, description="Contains details about the category.")
    type: Optional[StrictStr] = Field(None, description="Defines the type of the voucher. ")
    discount: Optional[Discount] = None
    gift: Optional[VoucherGift] = None
    loyalty_card: Optional[VoucherLoyaltyCard] = None
    start_date: Optional[datetime] = Field(None, description="Activation timestamp defines when the code starts to be active in ISO 8601 format. Voucher is *inactive before* this date. ")
    expiration_date: Optional[datetime] = Field(None, description="Expiration timestamp defines when the code expires in ISO 8601 format.  Voucher is *inactive after* this date.")
    validity_timeframe: Optional[VoucherValidityTimeframe] = None
    validity_day_of_week: Optional[conlist(StrictInt)] = Field(None, description="Integer array corresponding to the particular days of the week in which the voucher is valid.  - `0`  Sunday   - `1`  Monday   - `2`  Tuesday   - `3`  Wednesday   - `4`  Thursday   - `5`  Friday   - `6`  Saturday  ")
    active: Optional[StrictBool] = Field(None, description="A flag to toggle the voucher on or off. You can disable a voucher even though it's within the active period defined by the `start_date` and `expiration_date`.    - `true` indicates an *active* voucher - `false` indicates an *inactive* voucher")
    additional_info: Optional[StrictStr] = Field(None, description="An optional field to keep any extra textual information about the code such as a code description and details.")
    metadata: Optional[Dict[str, Any]] = Field(None, description="The metadata object stores all custom attributes assigned to the code. A set of key/value pairs that you can attach to a voucher object. It can be useful for storing additional information about the voucher in a structured format.")
    assets: Optional[VoucherAssets] = None
    is_referral_code: Optional[StrictBool] = Field(None, description="Flag indicating whether this voucher is a referral code; `true` for campaign type `REFERRAL_PROGRAM`.")
    created_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the voucher was created in ISO 8601 format.")
    updated_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the voucher was last updated in ISO 8601 format.")
    holder_id: Optional[StrictStr] = Field(None, description="Unique customer ID of voucher owner.")
    holder: Optional[SimpleCustomer] = None
    object: Optional[StrictStr] = Field('voucher', description="The type of object represented by JSON. Default is `voucher`.")
    distributions: Optional[conlist(Dict[str, Any])] = None
    deleted: Optional[StrictBool] = Field(None, description="Flag indicating whether this voucher is deleted.")
    validation_rules_assignments: Optional[ValidationRulesAssignmentsList] = None
    publish: Optional[VoucherPublish] = None
    redemption: Optional[VoucherRedemption] = None
    __properties = ["id", "code", "campaign", "campaign_id", "category", "category_id", "categories", "type", "discount", "gift", "loyalty_card", "start_date", "expiration_date", "validity_timeframe", "validity_day_of_week", "active", "additional_info", "metadata", "assets", "is_referral_code", "created_at", "updated_at", "holder_id", "holder", "object", "distributions", "deleted", "validation_rules_assignments", "publish", "redemption"]

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
    def from_json(cls, json_str: str) -> VouchersGetResponseBody:
        """Create an instance of VouchersGetResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item in self.categories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['categories'] = _items
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
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of holder
        if self.holder:
            _dict['holder'] = self.holder.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validation_rules_assignments
        if self.validation_rules_assignments:
            _dict['validation_rules_assignments'] = self.validation_rules_assignments.to_dict()
        # override the default output from pydantic by calling `to_dict()` of publish
        if self.publish:
            _dict['publish'] = self.publish.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redemption
        if self.redemption:
            _dict['redemption'] = self.redemption.to_dict()
        # set to None if active (nullable) is None
        # and __fields_set__ contains the field
        if self.active is None and "active" in self.__fields_set__:
            _dict['active'] = None

        # set to None if is_referral_code (nullable) is None
        # and __fields_set__ contains the field
        if self.is_referral_code is None and "is_referral_code" in self.__fields_set__:
            _dict['is_referral_code'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VouchersGetResponseBody:
        """Create an instance of VouchersGetResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VouchersGetResponseBody.parse_obj(obj)

        _obj = VouchersGetResponseBody.parse_obj({
            "id": obj.get("id"),
            "code": obj.get("code"),
            "campaign": obj.get("campaign"),
            "campaign_id": obj.get("campaign_id"),
            "category": obj.get("category"),
            "category_id": obj.get("category_id"),
            "categories": [Category.from_dict(_item) for _item in obj.get("categories")] if obj.get("categories") is not None else None,
            "type": obj.get("type"),
            "discount": Discount.from_dict(obj.get("discount")) if obj.get("discount") is not None else None,
            "gift": VoucherGift.from_dict(obj.get("gift")) if obj.get("gift") is not None else None,
            "loyalty_card": VoucherLoyaltyCard.from_dict(obj.get("loyalty_card")) if obj.get("loyalty_card") is not None else None,
            "start_date": obj.get("start_date"),
            "expiration_date": obj.get("expiration_date"),
            "validity_timeframe": VoucherValidityTimeframe.from_dict(obj.get("validity_timeframe")) if obj.get("validity_timeframe") is not None else None,
            "validity_day_of_week": obj.get("validity_day_of_week"),
            "active": obj.get("active"),
            "additional_info": obj.get("additional_info"),
            "metadata": obj.get("metadata"),
            "assets": VoucherAssets.from_dict(obj.get("assets")) if obj.get("assets") is not None else None,
            "is_referral_code": obj.get("is_referral_code"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "holder_id": obj.get("holder_id"),
            "holder": SimpleCustomer.from_dict(obj.get("holder")) if obj.get("holder") is not None else None,
            "object": obj.get("object") if obj.get("object") is not None else 'voucher',
            "distributions": obj.get("distributions"),
            "deleted": obj.get("deleted"),
            "validation_rules_assignments": ValidationRulesAssignmentsList.from_dict(obj.get("validation_rules_assignments")) if obj.get("validation_rules_assignments") is not None else None,
            "publish": VoucherPublish.from_dict(obj.get("publish")) if obj.get("publish") is not None else None,
            "redemption": VoucherRedemption.from_dict(obj.get("redemption")) if obj.get("redemption") is not None else None
        })
        return _obj


