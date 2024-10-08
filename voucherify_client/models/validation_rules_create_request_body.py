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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, validator
from voucherify_client.models.validation_rules_create_request_body_applicable_to import ValidationRulesCreateRequestBodyApplicableTo
from voucherify_client.models.validation_rules_create_request_body_error import ValidationRulesCreateRequestBodyError

class ValidationRulesCreateRequestBody(BaseModel):
    """
    Request body schema for **POST** `v1/validation-rules`.  # noqa: E501
    """
    name: Optional[StrictStr] = Field(None, description="Custom, unique name for set of validation rules.")
    rules: Optional[Dict[str, Any]] = Field(None, description="Contains all the rule definitions for the validation rule. It is a set of key value pairs representing the rules and logic between the rules. The keys are numbered consecutively beginning from `1`. The values are objects containing the rule conditions.")
    error: Optional[ValidationRulesCreateRequestBodyError] = None
    applicable_to: Optional[ValidationRulesCreateRequestBodyApplicableTo] = None
    type: Optional[StrictStr] = Field('expression', description="Type of validation rule.")
    context_type: Optional[StrictStr] = Field('global', description="Validation rule context type.    | **Context Type** | **Definition** | |:---|:---| | earning_rule.order.paid |  | | earning_rule.custom_event |  | | earning_rule.customer.segment.entered |  | | campaign.discount_coupons |  | | campaign.discount_coupons.discount.apply_to_order |  | | campaign.discount_coupons.discount.apply_to_items |  | | campaign.discount_coupons.discount.apply_to_items_proportionally |  | | campaign.discount_coupons.discount.apply_to_items_proportionally_by_quantity |  | | campaign.discount_coupons.discount.fixed.apply_to_items |  | | campaign.gift_vouchers |  | | campaign.gift_vouchers.gift.apply_to_order |  | | campaign.gift_vouchers.gift.apply_to_items |  | | campaign.referral_program |  | | campaign.referral_program.discount.apply_to_order |  | | campaign.referral_program.discount.apply_to_items |  | | campaign.referral_program.discount.apply_to_items_proportionally |  | | campaign.referral_program.discount.apply_to_items_proportionally_by_quantity |  | | campaign.referral_program.discount.fixed.apply_to_items |  | | campaign.promotion |  | | campaign.promotion.discount.apply_to_order |  | | campaign.promotion.discount.apply_to_items |  | | campaign.promotion.discount.apply_to_items_proportionally |  | | campaign.promotion.discount.apply_to_items_proportionally_by_quantity |  | | campaign.promotion.discount.fixed.apply_to_items |  | | campaign.loyalty_program |  | | campaign.lucky_draw |  | | voucher.discount_voucher |  | | voucher.discount_voucher.discount.apply_to_order |  | | voucher.discount_voucher.discount.apply_to_items |  | | voucher.discount_voucher.discount.apply_to_items_proportionally |  | | voucher.discount_voucher.discount.apply_to_items_proportionally_by_quantity |  | | voucher.discount_voucher.discount.fixed.apply_to_items |  | | voucher.gift_voucher |  | | voucher.gift_voucher.gift.apply_to_order |  | | voucher.gift_voucher.gift.apply_to_items |  | | voucher.loyalty_card |  | | voucher.lucky_draw_code |  | | distribution.custom_event |  | | reward_assignment.pay_with_points |  | | global |  |")
    __properties = ["name", "rules", "error", "applicable_to", "type", "context_type"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('expression', 'basic', 'advanced', 'complex',):
            raise ValueError("must be one of enum values ('expression', 'basic', 'advanced', 'complex')")
        return value

    @validator('context_type')
    def context_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('earning_rule.order.paid', 'earning_rule.custom_event', 'earning_rule.customer.segment.entered', 'earning_rule.customer.tier.joined', 'earning_rule.customer.tier.left', 'earning_rule.customer.tier.upgraded', 'earning_rule.customer.tier.downgraded', 'earning_rule.customer.tier.prolonged', 'campaign.discount_coupons', 'campaign.discount_coupons.discount.apply_to_order', 'campaign.discount_coupons.discount.apply_to_items', 'campaign.discount_coupons.discount.apply_to_items_proportionally', 'campaign.discount_coupons.discount.apply_to_items_proportionally_by_quantity', 'campaign.discount_coupons.discount.apply_to_items_by_quantity', 'campaign.discount_coupons.discount.fixed.apply_to_items', 'campaign.discount_coupons.discount.percent.apply_to_items', 'campaign.gift_vouchers', 'campaign.gift_vouchers.gift.apply_to_order', 'campaign.gift_vouchers.gift.apply_to_items', 'campaign.referral_program', 'campaign.referral_program.discount.apply_to_order', 'campaign.referral_program.discount.apply_to_items', 'campaign.referral_program.discount.apply_to_items_proportionally', 'campaign.referral_program.discount.apply_to_items_proportionally_by_quantity', 'campaign.referral_program.discount.apply_to_items_by_quantity', 'campaign.referral_program.discount.fixed.apply_to_items', 'campaign.referral_program.discount.percent.apply_to_items', 'campaign.promotion', 'campaign.promotion.discount.apply_to_order', 'campaign.promotion.discount.apply_to_items', 'campaign.promotion.discount.apply_to_items_proportionally', 'campaign.promotion.discount.apply_to_items_proportionally_by_quantity', 'campaign.promotion.discount.apply_to_items_by_quantity', 'campaign.promotion.discount.fixed.apply_to_items', 'campaign.promotion.discount.percent.apply_to_items', 'campaign.loyalty_program', 'campaign.lucky_draw', 'voucher.discount_voucher', 'voucher.discount_voucher.discount.apply_to_order', 'voucher.discount_voucher.discount.apply_to_items', 'voucher.discount_voucher.discount.apply_to_items_proportionally', 'voucher.discount_voucher.discount.apply_to_items_proportionally_by_quantity', 'voucher.discount_voucher.discount.apply_to_items_by_quantity', 'voucher.discount_voucher.discount.fixed.apply_to_items', 'voucher.discount_voucher.discount.percent.apply_to_items', 'voucher.gift_voucher', 'voucher.gift_voucher.gift.apply_to_order', 'voucher.gift_voucher.gift.apply_to_items', 'voucher.loyalty_card', 'voucher.lucky_draw_code', 'distribution.custom_event', 'distribution.order.paid', 'distribution.order.created', 'distribution.order.canceled', 'distribution.order.updated', 'reward_assignment.pay_with_points', 'global',):
            raise ValueError("must be one of enum values ('earning_rule.order.paid', 'earning_rule.custom_event', 'earning_rule.customer.segment.entered', 'earning_rule.customer.tier.joined', 'earning_rule.customer.tier.left', 'earning_rule.customer.tier.upgraded', 'earning_rule.customer.tier.downgraded', 'earning_rule.customer.tier.prolonged', 'campaign.discount_coupons', 'campaign.discount_coupons.discount.apply_to_order', 'campaign.discount_coupons.discount.apply_to_items', 'campaign.discount_coupons.discount.apply_to_items_proportionally', 'campaign.discount_coupons.discount.apply_to_items_proportionally_by_quantity', 'campaign.discount_coupons.discount.apply_to_items_by_quantity', 'campaign.discount_coupons.discount.fixed.apply_to_items', 'campaign.discount_coupons.discount.percent.apply_to_items', 'campaign.gift_vouchers', 'campaign.gift_vouchers.gift.apply_to_order', 'campaign.gift_vouchers.gift.apply_to_items', 'campaign.referral_program', 'campaign.referral_program.discount.apply_to_order', 'campaign.referral_program.discount.apply_to_items', 'campaign.referral_program.discount.apply_to_items_proportionally', 'campaign.referral_program.discount.apply_to_items_proportionally_by_quantity', 'campaign.referral_program.discount.apply_to_items_by_quantity', 'campaign.referral_program.discount.fixed.apply_to_items', 'campaign.referral_program.discount.percent.apply_to_items', 'campaign.promotion', 'campaign.promotion.discount.apply_to_order', 'campaign.promotion.discount.apply_to_items', 'campaign.promotion.discount.apply_to_items_proportionally', 'campaign.promotion.discount.apply_to_items_proportionally_by_quantity', 'campaign.promotion.discount.apply_to_items_by_quantity', 'campaign.promotion.discount.fixed.apply_to_items', 'campaign.promotion.discount.percent.apply_to_items', 'campaign.loyalty_program', 'campaign.lucky_draw', 'voucher.discount_voucher', 'voucher.discount_voucher.discount.apply_to_order', 'voucher.discount_voucher.discount.apply_to_items', 'voucher.discount_voucher.discount.apply_to_items_proportionally', 'voucher.discount_voucher.discount.apply_to_items_proportionally_by_quantity', 'voucher.discount_voucher.discount.apply_to_items_by_quantity', 'voucher.discount_voucher.discount.fixed.apply_to_items', 'voucher.discount_voucher.discount.percent.apply_to_items', 'voucher.gift_voucher', 'voucher.gift_voucher.gift.apply_to_order', 'voucher.gift_voucher.gift.apply_to_items', 'voucher.loyalty_card', 'voucher.lucky_draw_code', 'distribution.custom_event', 'distribution.order.paid', 'distribution.order.created', 'distribution.order.canceled', 'distribution.order.updated', 'reward_assignment.pay_with_points', 'global')")
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
    def from_json(cls, json_str: str) -> ValidationRulesCreateRequestBody:
        """Create an instance of ValidationRulesCreateRequestBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of applicable_to
        if self.applicable_to:
            _dict['applicable_to'] = self.applicable_to.to_dict()
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if error (nullable) is None
        # and __fields_set__ contains the field
        if self.error is None and "error" in self.__fields_set__:
            _dict['error'] = None

        # set to None if applicable_to (nullable) is None
        # and __fields_set__ contains the field
        if self.applicable_to is None and "applicable_to" in self.__fields_set__:
            _dict['applicable_to'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if context_type (nullable) is None
        # and __fields_set__ contains the field
        if self.context_type is None and "context_type" in self.__fields_set__:
            _dict['context_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ValidationRulesCreateRequestBody:
        """Create an instance of ValidationRulesCreateRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ValidationRulesCreateRequestBody.parse_obj(obj)

        _obj = ValidationRulesCreateRequestBody.parse_obj({
            "name": obj.get("name"),
            "rules": obj.get("rules"),
            "error": ValidationRulesCreateRequestBodyError.from_dict(obj.get("error")) if obj.get("error") is not None else None,
            "applicable_to": ValidationRulesCreateRequestBodyApplicableTo.from_dict(obj.get("applicable_to")) if obj.get("applicable_to") is not None else None,
            "type": obj.get("type") if obj.get("type") is not None else 'expression',
            "context_type": obj.get("context_type") if obj.get("context_type") is not None else 'global'
        })
        return _obj


