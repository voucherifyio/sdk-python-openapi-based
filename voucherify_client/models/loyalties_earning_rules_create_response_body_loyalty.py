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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator
from voucherify_client.models.loyalties_earning_rules_create_response_body_loyalty_custom_event import LoyaltiesEarningRulesCreateResponseBodyLoyaltyCustomEvent
from voucherify_client.models.loyalties_earning_rules_create_response_body_loyalty_customer import LoyaltiesEarningRulesCreateResponseBodyLoyaltyCustomer
from voucherify_client.models.loyalties_earning_rules_create_response_body_loyalty_order import LoyaltiesEarningRulesCreateResponseBodyLoyaltyOrder
from voucherify_client.models.loyalties_earning_rules_create_response_body_loyalty_order_items import LoyaltiesEarningRulesCreateResponseBodyLoyaltyOrderItems

class LoyaltiesEarningRulesCreateResponseBodyLoyalty(BaseModel):
    """
    LoyaltiesEarningRulesCreateResponseBodyLoyalty
    """
    type: Optional[StrictStr] = None
    calculation_type: Optional[StrictStr] = None
    order: Optional[LoyaltiesEarningRulesCreateResponseBodyLoyaltyOrder] = None
    order_items: Optional[LoyaltiesEarningRulesCreateResponseBodyLoyaltyOrderItems] = None
    customer: Optional[LoyaltiesEarningRulesCreateResponseBodyLoyaltyCustomer] = None
    custom_event: Optional[LoyaltiesEarningRulesCreateResponseBodyLoyaltyCustomEvent] = None
    points: Optional[StrictInt] = Field(None, description="Defines how the points will be added to the loyalty card. FIXED adds a fixed number of points.")
    __properties = ["type", "calculation_type", "order", "order_items", "customer", "custom_event", "points"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PROPORTIONAL', 'FIXED',):
            raise ValueError("must be one of enum values ('PROPORTIONAL', 'FIXED')")
        return value

    @validator('calculation_type')
    def calculation_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ORDER_AMOUNT', 'ORDER_TOTAL_AMOUNT', 'ORDER_METADATA', 'ORDER_ITEMS_QUANTITY', 'ORDER_ITEMS_AMOUNT', 'ORDER_ITEMS_SUBTOTAL_AMOUNT', 'CUSTOMER_METADATA', 'CUSTOM_EVENT_METADATA',):
            raise ValueError("must be one of enum values ('ORDER_AMOUNT', 'ORDER_TOTAL_AMOUNT', 'ORDER_METADATA', 'ORDER_ITEMS_QUANTITY', 'ORDER_ITEMS_AMOUNT', 'ORDER_ITEMS_SUBTOTAL_AMOUNT', 'CUSTOMER_METADATA', 'CUSTOM_EVENT_METADATA')")
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
    def from_json(cls, json_str: str) -> LoyaltiesEarningRulesCreateResponseBodyLoyalty:
        """Create an instance of LoyaltiesEarningRulesCreateResponseBodyLoyalty from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order_items
        if self.order_items:
            _dict['order_items'] = self.order_items.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_event
        if self.custom_event:
            _dict['custom_event'] = self.custom_event.to_dict()
        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if calculation_type (nullable) is None
        # and __fields_set__ contains the field
        if self.calculation_type is None and "calculation_type" in self.__fields_set__:
            _dict['calculation_type'] = None

        # set to None if order (nullable) is None
        # and __fields_set__ contains the field
        if self.order is None and "order" in self.__fields_set__:
            _dict['order'] = None

        # set to None if order_items (nullable) is None
        # and __fields_set__ contains the field
        if self.order_items is None and "order_items" in self.__fields_set__:
            _dict['order_items'] = None

        # set to None if customer (nullable) is None
        # and __fields_set__ contains the field
        if self.customer is None and "customer" in self.__fields_set__:
            _dict['customer'] = None

        # set to None if custom_event (nullable) is None
        # and __fields_set__ contains the field
        if self.custom_event is None and "custom_event" in self.__fields_set__:
            _dict['custom_event'] = None

        # set to None if points (nullable) is None
        # and __fields_set__ contains the field
        if self.points is None and "points" in self.__fields_set__:
            _dict['points'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltiesEarningRulesCreateResponseBodyLoyalty:
        """Create an instance of LoyaltiesEarningRulesCreateResponseBodyLoyalty from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesEarningRulesCreateResponseBodyLoyalty.parse_obj(obj)

        _obj = LoyaltiesEarningRulesCreateResponseBodyLoyalty.parse_obj({
            "type": obj.get("type"),
            "calculation_type": obj.get("calculation_type"),
            "order": LoyaltiesEarningRulesCreateResponseBodyLoyaltyOrder.from_dict(obj.get("order")) if obj.get("order") is not None else None,
            "order_items": LoyaltiesEarningRulesCreateResponseBodyLoyaltyOrderItems.from_dict(obj.get("order_items")) if obj.get("order_items") is not None else None,
            "customer": LoyaltiesEarningRulesCreateResponseBodyLoyaltyCustomer.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "custom_event": LoyaltiesEarningRulesCreateResponseBodyLoyaltyCustomEvent.from_dict(obj.get("custom_event")) if obj.get("custom_event") is not None else None,
            "points": obj.get("points")
        })
        return _obj


