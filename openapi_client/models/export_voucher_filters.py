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
from openapi_client.models.field_conditions import FieldConditions
from openapi_client.models.junction import Junction

class ExportVoucherFilters(BaseModel):
    """
    ExportVoucherFilters
    """
    junction: Optional[Junction] = None
    code: Optional[FieldConditions] = None
    voucher_type: Optional[FieldConditions] = None
    value: Optional[FieldConditions] = None
    discount_type: Optional[FieldConditions] = None
    campaign: Optional[FieldConditions] = None
    category: Optional[FieldConditions] = None
    start_date: Optional[FieldConditions] = None
    expiration_date: Optional[FieldConditions] = None
    gift_balance: Optional[FieldConditions] = None
    loyalty_balance: Optional[FieldConditions] = None
    redemption_quantity: Optional[FieldConditions] = None
    redemption_count: Optional[FieldConditions] = None
    active: Optional[FieldConditions] = None
    qr_code: Optional[FieldConditions] = None
    bar_code: Optional[FieldConditions] = None
    metadata: Optional[FieldConditions] = None
    id: Optional[FieldConditions] = None
    is_referral_code: Optional[FieldConditions] = None
    created_at: Optional[FieldConditions] = None
    updated_at: Optional[FieldConditions] = None
    validity_timeframe_interval: Optional[FieldConditions] = None
    validity_timeframe_duration: Optional[FieldConditions] = None
    validity_day_of_week: Optional[FieldConditions] = None
    discount_amount_limit: Optional[FieldConditions] = None
    campaign_id: Optional[FieldConditions] = None
    additional_info: Optional[FieldConditions] = None
    customer_id: Optional[FieldConditions] = None
    discount_unit_type: Optional[FieldConditions] = None
    discount_unit_effect: Optional[FieldConditions] = None
    customer_source_id: Optional[FieldConditions] = None
    __properties = ["junction", "code", "voucher_type", "value", "discount_type", "campaign", "category", "start_date", "expiration_date", "gift_balance", "loyalty_balance", "redemption_quantity", "redemption_count", "active", "qr_code", "bar_code", "metadata", "id", "is_referral_code", "created_at", "updated_at", "validity_timeframe_interval", "validity_timeframe_duration", "validity_day_of_week", "discount_amount_limit", "campaign_id", "additional_info", "customer_id", "discount_unit_type", "discount_unit_effect", "customer_source_id"]

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
    def from_json(cls, json_str: str) -> ExportVoucherFilters:
        """Create an instance of ExportVoucherFilters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of code
        if self.code:
            _dict['code'] = self.code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of voucher_type
        if self.voucher_type:
            _dict['voucher_type'] = self.voucher_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discount_type
        if self.discount_type:
            _dict['discount_type'] = self.discount_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaign
        if self.campaign:
            _dict['campaign'] = self.campaign.to_dict()
        # override the default output from pydantic by calling `to_dict()` of category
        if self.category:
            _dict['category'] = self.category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of start_date
        if self.start_date:
            _dict['start_date'] = self.start_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of expiration_date
        if self.expiration_date:
            _dict['expiration_date'] = self.expiration_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gift_balance
        if self.gift_balance:
            _dict['gift_balance'] = self.gift_balance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loyalty_balance
        if self.loyalty_balance:
            _dict['loyalty_balance'] = self.loyalty_balance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redemption_quantity
        if self.redemption_quantity:
            _dict['redemption_quantity'] = self.redemption_quantity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redemption_count
        if self.redemption_count:
            _dict['redemption_count'] = self.redemption_count.to_dict()
        # override the default output from pydantic by calling `to_dict()` of active
        if self.active:
            _dict['active'] = self.active.to_dict()
        # override the default output from pydantic by calling `to_dict()` of qr_code
        if self.qr_code:
            _dict['qr_code'] = self.qr_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bar_code
        if self.bar_code:
            _dict['bar_code'] = self.bar_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of is_referral_code
        if self.is_referral_code:
            _dict['is_referral_code'] = self.is_referral_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_at
        if self.created_at:
            _dict['created_at'] = self.created_at.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_at
        if self.updated_at:
            _dict['updated_at'] = self.updated_at.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_timeframe_interval
        if self.validity_timeframe_interval:
            _dict['validity_timeframe_interval'] = self.validity_timeframe_interval.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_timeframe_duration
        if self.validity_timeframe_duration:
            _dict['validity_timeframe_duration'] = self.validity_timeframe_duration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_day_of_week
        if self.validity_day_of_week:
            _dict['validity_day_of_week'] = self.validity_day_of_week.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discount_amount_limit
        if self.discount_amount_limit:
            _dict['discount_amount_limit'] = self.discount_amount_limit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaign_id
        if self.campaign_id:
            _dict['campaign_id'] = self.campaign_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of additional_info
        if self.additional_info:
            _dict['additional_info'] = self.additional_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer_id
        if self.customer_id:
            _dict['customer_id'] = self.customer_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discount_unit_type
        if self.discount_unit_type:
            _dict['discount_unit_type'] = self.discount_unit_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discount_unit_effect
        if self.discount_unit_effect:
            _dict['discount_unit_effect'] = self.discount_unit_effect.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer_source_id
        if self.customer_source_id:
            _dict['customer_source_id'] = self.customer_source_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExportVoucherFilters:
        """Create an instance of ExportVoucherFilters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExportVoucherFilters.parse_obj(obj)

        _obj = ExportVoucherFilters.parse_obj({
            "junction": obj.get("junction"),
            "code": FieldConditions.from_dict(obj.get("code")) if obj.get("code") is not None else None,
            "voucher_type": FieldConditions.from_dict(obj.get("voucher_type")) if obj.get("voucher_type") is not None else None,
            "value": FieldConditions.from_dict(obj.get("value")) if obj.get("value") is not None else None,
            "discount_type": FieldConditions.from_dict(obj.get("discount_type")) if obj.get("discount_type") is not None else None,
            "campaign": FieldConditions.from_dict(obj.get("campaign")) if obj.get("campaign") is not None else None,
            "category": FieldConditions.from_dict(obj.get("category")) if obj.get("category") is not None else None,
            "start_date": FieldConditions.from_dict(obj.get("start_date")) if obj.get("start_date") is not None else None,
            "expiration_date": FieldConditions.from_dict(obj.get("expiration_date")) if obj.get("expiration_date") is not None else None,
            "gift_balance": FieldConditions.from_dict(obj.get("gift_balance")) if obj.get("gift_balance") is not None else None,
            "loyalty_balance": FieldConditions.from_dict(obj.get("loyalty_balance")) if obj.get("loyalty_balance") is not None else None,
            "redemption_quantity": FieldConditions.from_dict(obj.get("redemption_quantity")) if obj.get("redemption_quantity") is not None else None,
            "redemption_count": FieldConditions.from_dict(obj.get("redemption_count")) if obj.get("redemption_count") is not None else None,
            "active": FieldConditions.from_dict(obj.get("active")) if obj.get("active") is not None else None,
            "qr_code": FieldConditions.from_dict(obj.get("qr_code")) if obj.get("qr_code") is not None else None,
            "bar_code": FieldConditions.from_dict(obj.get("bar_code")) if obj.get("bar_code") is not None else None,
            "metadata": FieldConditions.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "id": FieldConditions.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "is_referral_code": FieldConditions.from_dict(obj.get("is_referral_code")) if obj.get("is_referral_code") is not None else None,
            "created_at": FieldConditions.from_dict(obj.get("created_at")) if obj.get("created_at") is not None else None,
            "updated_at": FieldConditions.from_dict(obj.get("updated_at")) if obj.get("updated_at") is not None else None,
            "validity_timeframe_interval": FieldConditions.from_dict(obj.get("validity_timeframe_interval")) if obj.get("validity_timeframe_interval") is not None else None,
            "validity_timeframe_duration": FieldConditions.from_dict(obj.get("validity_timeframe_duration")) if obj.get("validity_timeframe_duration") is not None else None,
            "validity_day_of_week": FieldConditions.from_dict(obj.get("validity_day_of_week")) if obj.get("validity_day_of_week") is not None else None,
            "discount_amount_limit": FieldConditions.from_dict(obj.get("discount_amount_limit")) if obj.get("discount_amount_limit") is not None else None,
            "campaign_id": FieldConditions.from_dict(obj.get("campaign_id")) if obj.get("campaign_id") is not None else None,
            "additional_info": FieldConditions.from_dict(obj.get("additional_info")) if obj.get("additional_info") is not None else None,
            "customer_id": FieldConditions.from_dict(obj.get("customer_id")) if obj.get("customer_id") is not None else None,
            "discount_unit_type": FieldConditions.from_dict(obj.get("discount_unit_type")) if obj.get("discount_unit_type") is not None else None,
            "discount_unit_effect": FieldConditions.from_dict(obj.get("discount_unit_effect")) if obj.get("discount_unit_effect") is not None else None,
            "customer_source_id": FieldConditions.from_dict(obj.get("customer_source_id")) if obj.get("customer_source_id") is not None else None
        })
        return _obj


