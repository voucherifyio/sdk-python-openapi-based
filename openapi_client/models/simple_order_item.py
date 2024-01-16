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

class SimpleOrderItem(BaseModel):
    """
    SimpleOrderItem
    """
    object: Optional[StrictStr] = Field('order_item', description="The type of object represented by JSON. This object stores information about the `order_item`.")
    source_id: Optional[StrictStr] = Field(None, description="The merchant’s product/SKU ID (if it is different from the Voucherify product/SKU ID). It is useful in the integration between multiple systems. It can be an ID from an eCommerce site, a database, or a third-party service.")
    related_object: Optional[StrictStr] = Field(None, description="Used along with the source_id property, can be set to either sku or product.")
    product_id: Optional[StrictStr] = Field(None, description="A unique product ID assigned by Voucherify.")
    sku_id: Optional[StrictStr] = Field(None, description="A unique SKU ID assigned by Voucherify.")
    quantity: Optional[StrictInt] = Field(None, description="The quantity of the particular item in the cart.")
    discount_quantity: Optional[StrictInt] = Field(None, description="Number of dicounted items.")
    amount: Optional[StrictInt] = Field(None, description="The total amount of the order item (price * quantity).")
    discount_amount: Optional[StrictInt] = Field(None, description=" Sum of all order-item-level discounts applied to the order.")
    applied_discount_amount: Optional[StrictInt] = Field(None, description="This field shows the order-level discount applied.")
    price: Optional[StrictInt] = Field(None, description="Unit price of an item. Value is multiplied by 100 to precisely represent 2 decimal places. For example `10000 cents` for `$100.00`.")
    __properties = ["object", "source_id", "related_object", "product_id", "sku_id", "quantity", "discount_quantity", "amount", "discount_amount", "applied_discount_amount", "price"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('order_item',):
            raise ValueError("must be one of enum values ('order_item')")
        return value

    @validator('related_object')
    def related_object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('product', 'sku',):
            raise ValueError("must be one of enum values ('product', 'sku')")
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
    def from_json(cls, json_str: str) -> SimpleOrderItem:
        """Create an instance of SimpleOrderItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SimpleOrderItem:
        """Create an instance of SimpleOrderItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SimpleOrderItem.parse_obj(obj)

        _obj = SimpleOrderItem.parse_obj({
            "object": obj.get("object") if obj.get("object") is not None else 'order_item',
            "source_id": obj.get("source_id"),
            "related_object": obj.get("related_object"),
            "product_id": obj.get("product_id"),
            "sku_id": obj.get("sku_id"),
            "quantity": obj.get("quantity"),
            "discount_quantity": obj.get("discount_quantity"),
            "amount": obj.get("amount"),
            "discount_amount": obj.get("discount_amount"),
            "applied_discount_amount": obj.get("applied_discount_amount"),
            "price": obj.get("price")
        })
        return _obj


