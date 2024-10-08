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
from voucherify_client.models.promotion_tier_create_params_action import PromotionTierCreateParamsAction
from voucherify_client.models.validity_hours import ValidityHours
from voucherify_client.models.validity_timeframe import ValidityTimeframe

class PromotionTierCreateParams(BaseModel):
    """
    This is an object representing a promotion tier create params. Promotion tiers are always assigned to a campaign and cannot be used standalone.  # noqa: E501
    """
    name: Optional[StrictStr] = Field(None, description="Name of the promotion tier.")
    banner: Optional[StrictStr] = Field(None, description="Text to be displayed to your customers on your website.")
    action: Optional[PromotionTierCreateParamsAction] = None
    metadata: Optional[Dict[str, Any]] = Field(None, description="The metadata object stores all custom attributes assigned to the promotion tier. A set of key/value pairs that you can attach to a promotion tier object. It can be useful for storing additional information about the promotion tier in a structured format.")
    validation_rules: Optional[conlist(StrictStr)] = Field(None, description="Array containing the ID of the validation rule associated with the promotion tier.")
    active: Optional[StrictBool] = Field(None, description="A flag to toggle the promotion tier on or off. You can disable a promotion tier even though it's within the active period defined by the `start_date` and `expiration_date`.    - `true` indicates an *active* promotion tier - `false` indicates an *inactive* promotion tier")
    hierarchy: Optional[StrictInt] = Field(None, description="The promotions hierarchy defines the order in which the discounts from different tiers will be applied to a customer's order. If a customer qualifies for discounts from more than one tier, discounts will be applied in the order defined in the hierarchy.")
    start_date: Optional[datetime] = Field(None, description="Activation timestamp defines when the promotion tier starts to be active in ISO 8601 format. Promotion tier is *inactive before* this date. ")
    expiration_date: Optional[datetime] = Field(None, description="Activation timestamp defines when the promotion tier expires in ISO 8601 format. Promotion tier is *inactive after* this date. ")
    validity_timeframe: Optional[ValidityTimeframe] = None
    validity_day_of_week: Optional[conlist(StrictInt)] = Field(None, description="Integer array corresponding to the particular days of the week in which the voucher is valid.  - `0` Sunday - `1` Monday - `2` Tuesday - `3` Wednesday - `4` Thursday - `5` Friday - `6` Saturday")
    validity_hours: Optional[ValidityHours] = None
    category: Optional[StrictStr] = Field(None, description="Assign category to the promotion tier.")
    category_id: Optional[StrictStr] = Field(None, description="Instead of using the category name, you can alternatively assign a new category to a promotion tier using a unique category ID, i.e. `cat_0c9da30e7116ba6bba`.")
    __properties = ["name", "banner", "action", "metadata", "validation_rules", "active", "hierarchy", "start_date", "expiration_date", "validity_timeframe", "validity_day_of_week", "validity_hours", "category", "category_id"]

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
    def from_json(cls, json_str: str) -> PromotionTierCreateParams:
        """Create an instance of PromotionTierCreateParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of validity_timeframe
        if self.validity_timeframe:
            _dict['validity_timeframe'] = self.validity_timeframe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_hours
        if self.validity_hours:
            _dict['validity_hours'] = self.validity_hours.to_dict()
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

        # set to None if validation_rules (nullable) is None
        # and __fields_set__ contains the field
        if self.validation_rules is None and "validation_rules" in self.__fields_set__:
            _dict['validation_rules'] = None

        # set to None if active (nullable) is None
        # and __fields_set__ contains the field
        if self.active is None and "active" in self.__fields_set__:
            _dict['active'] = None

        # set to None if hierarchy (nullable) is None
        # and __fields_set__ contains the field
        if self.hierarchy is None and "hierarchy" in self.__fields_set__:
            _dict['hierarchy'] = None

        # set to None if start_date (nullable) is None
        # and __fields_set__ contains the field
        if self.start_date is None and "start_date" in self.__fields_set__:
            _dict['start_date'] = None

        # set to None if expiration_date (nullable) is None
        # and __fields_set__ contains the field
        if self.expiration_date is None and "expiration_date" in self.__fields_set__:
            _dict['expiration_date'] = None

        # set to None if category (nullable) is None
        # and __fields_set__ contains the field
        if self.category is None and "category" in self.__fields_set__:
            _dict['category'] = None

        # set to None if category_id (nullable) is None
        # and __fields_set__ contains the field
        if self.category_id is None and "category_id" in self.__fields_set__:
            _dict['category_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PromotionTierCreateParams:
        """Create an instance of PromotionTierCreateParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PromotionTierCreateParams.parse_obj(obj)

        _obj = PromotionTierCreateParams.parse_obj({
            "name": obj.get("name"),
            "banner": obj.get("banner"),
            "action": PromotionTierCreateParamsAction.from_dict(obj.get("action")) if obj.get("action") is not None else None,
            "metadata": obj.get("metadata"),
            "validation_rules": obj.get("validation_rules"),
            "active": obj.get("active"),
            "hierarchy": obj.get("hierarchy"),
            "start_date": obj.get("start_date"),
            "expiration_date": obj.get("expiration_date"),
            "validity_timeframe": ValidityTimeframe.from_dict(obj.get("validity_timeframe")) if obj.get("validity_timeframe") is not None else None,
            "validity_day_of_week": obj.get("validity_day_of_week"),
            "validity_hours": ValidityHours.from_dict(obj.get("validity_hours")) if obj.get("validity_hours") is not None else None,
            "category": obj.get("category"),
            "category_id": obj.get("category_id")
        })
        return _obj


