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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator
from voucherify_client.models.customer_id import CustomerId
from voucherify_client.models.order_item_calculated import OrderItemCalculated
from voucherify_client.models.referrer_id import ReferrerId

class OrdersGetResponseBody(BaseModel):
    """
    Response body schema for **GET** `/orders/{orderId}`.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="Unique ID assigned by Voucherify of an existing order that will be linked to the redemption of this request.")
    source_id: Optional[StrictStr] = Field(None, description="Unique source ID of an existing order that will be linked to the redemption of this request.")
    created_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the order was created in ISO 8601 format.")
    updated_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the order was last updated in ISO 8601 format.")
    status: Optional[StrictStr] = Field(None, description="The order status.")
    amount: Optional[StrictInt] = Field(None, description="A positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the total amount of the order. This is the sum of the order items' amounts.")
    initial_amount: Optional[StrictInt] = Field(None, description="A positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the total amount of the order. This is the sum of the order items' amounts.")
    discount_amount: Optional[StrictInt] = Field(None, description="Sum of all order-level discounts applied to the order.")
    items_discount_amount: Optional[StrictInt] = Field(None, description="Sum of all product-specific discounts applied to the order.")
    total_discount_amount: Optional[StrictInt] = Field(None, description="Sum of all order-level AND all product-specific discounts applied to the order.")
    total_amount: Optional[StrictInt] = Field(None, description="Order amount after undoing all the discounts through the rollback redemption.")
    applied_discount_amount: Optional[StrictInt] = Field(None, description="This field shows the order-level discount applied.")
    items_applied_discount_amount: Optional[StrictInt] = Field(None, description="Sum of all product-specific discounts applied in a particular request.   `sum(items, i => i.applied_discount_amount)`")
    total_applied_discount_amount: Optional[StrictInt] = Field(None, description="Sum of all order-level AND all product-specific discounts applied in a particular request.   `total_applied_discount_amount` = `applied_discount_amount` + `items_applied_discount_amount`")
    items: Optional[conlist(OrderItemCalculated)] = Field(None, description="Array of items applied to the order.")
    metadata: Optional[Dict[str, Any]] = Field(None, description="A set of custom key/value pairs that you can attach to an order. It can be useful for storing additional information about the order in a structured format.")
    customer_id: Optional[StrictStr] = Field(None, description="Unique customer ID of the customer making the purchase.")
    referrer_id: Optional[StrictStr] = Field(None, description="Unique referrer ID.")
    object: StrictStr = Field(..., description="The type of object represented by JSON.")
    redemptions: Optional[Dict[str, Any]] = None
    customer: Optional[CustomerId] = None
    referrer: Optional[ReferrerId] = None
    __properties = ["id", "source_id", "created_at", "updated_at", "status", "amount", "initial_amount", "discount_amount", "items_discount_amount", "total_discount_amount", "total_amount", "applied_discount_amount", "items_applied_discount_amount", "total_applied_discount_amount", "items", "metadata", "customer_id", "referrer_id", "object", "redemptions", "customer", "referrer"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('CREATED', 'PAID', 'CANCELED', 'FULFILLED',):
            raise ValueError("must be one of enum values ('CREATED', 'PAID', 'CANCELED', 'FULFILLED')")
        return value

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('order',):
            raise ValueError("must be one of enum values ('order')")
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
    def from_json(cls, json_str: str) -> OrdersGetResponseBody:
        """Create an instance of OrdersGetResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of referrer
        if self.referrer:
            _dict['referrer'] = self.referrer.to_dict()
        # set to None if source_id (nullable) is None
        # and __fields_set__ contains the field
        if self.source_id is None and "source_id" in self.__fields_set__:
            _dict['source_id'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        # set to None if customer_id (nullable) is None
        # and __fields_set__ contains the field
        if self.customer_id is None and "customer_id" in self.__fields_set__:
            _dict['customer_id'] = None

        # set to None if referrer_id (nullable) is None
        # and __fields_set__ contains the field
        if self.referrer_id is None and "referrer_id" in self.__fields_set__:
            _dict['referrer_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrdersGetResponseBody:
        """Create an instance of OrdersGetResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrdersGetResponseBody.parse_obj(obj)

        _obj = OrdersGetResponseBody.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("source_id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "status": obj.get("status"),
            "amount": obj.get("amount"),
            "initial_amount": obj.get("initial_amount"),
            "discount_amount": obj.get("discount_amount"),
            "items_discount_amount": obj.get("items_discount_amount"),
            "total_discount_amount": obj.get("total_discount_amount"),
            "total_amount": obj.get("total_amount"),
            "applied_discount_amount": obj.get("applied_discount_amount"),
            "items_applied_discount_amount": obj.get("items_applied_discount_amount"),
            "total_applied_discount_amount": obj.get("total_applied_discount_amount"),
            "items": [OrderItemCalculated.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None,
            "metadata": obj.get("metadata"),
            "customer_id": obj.get("customer_id"),
            "referrer_id": obj.get("referrer_id"),
            "object": obj.get("object") if obj.get("object") is not None else 'order',
            "redemptions": obj.get("redemptions"),
            "customer": CustomerId.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "referrer": ReferrerId.from_dict(obj.get("referrer")) if obj.get("referrer") is not None else None
        })
        return _obj


