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



from pydantic import BaseModel, Field, StrictStr, validator
from voucherify_client.models.earning_rule_proportional_order_items_subtotal_amount_order_items import EarningRuleProportionalOrderItemsSubtotalAmountOrderItems

class EarningRuleProportionalOrderItemsSubtotalAmount(BaseModel):
    """
    EarningRuleProportionalOrderItemsSubtotalAmount
    """
    type: StrictStr = Field(..., description="Defines how the points will be added to the loyalty card.PROPORTIONAL adds points based on a pre-defined ratio.")
    calculation_type: StrictStr = Field(..., description="ORDER_ITEMS_SUBTOTAL_AMOUNT; Amount spent on items defined in the order_items.subtotal_amount.object & .id (X points for every Y spent on items including discounts)")
    order_items: EarningRuleProportionalOrderItemsSubtotalAmountOrderItems = Field(...)
    __properties = ["type", "calculation_type", "order_items"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('PROPORTIONAL',):
            raise ValueError("must be one of enum values ('PROPORTIONAL')")
        return value

    @validator('calculation_type')
    def calculation_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ORDER_ITEMS_SUBTOTAL_AMOUNT',):
            raise ValueError("must be one of enum values ('ORDER_ITEMS_SUBTOTAL_AMOUNT')")
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
    def from_json(cls, json_str: str) -> EarningRuleProportionalOrderItemsSubtotalAmount:
        """Create an instance of EarningRuleProportionalOrderItemsSubtotalAmount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of order_items
        if self.order_items:
            _dict['order_items'] = self.order_items.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EarningRuleProportionalOrderItemsSubtotalAmount:
        """Create an instance of EarningRuleProportionalOrderItemsSubtotalAmount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EarningRuleProportionalOrderItemsSubtotalAmount.parse_obj(obj)

        _obj = EarningRuleProportionalOrderItemsSubtotalAmount.parse_obj({
            "type": obj.get("type") if obj.get("type") is not None else 'PROPORTIONAL',
            "calculation_type": obj.get("calculation_type") if obj.get("calculation_type") is not None else 'ORDER_ITEMS_SUBTOTAL_AMOUNT',
            "order_items": EarningRuleProportionalOrderItemsSubtotalAmountOrderItems.from_dict(obj.get("order_items")) if obj.get("order_items") is not None else None
        })
        return _obj


