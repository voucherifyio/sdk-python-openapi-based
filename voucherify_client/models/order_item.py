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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator
from voucherify_client.models.order_item_product import OrderItemProduct
from voucherify_client.models.order_item_sku import OrderItemSku

class OrderItem(BaseModel):
    """
    OrderItem
    """
    sku_id: Optional[StrictStr] = Field(None, description="Unique identifier of the SKU. It is assigned by Voucherify.")
    product_id: Optional[StrictStr] = Field(None, description="Unique identifier of the product. It is assigned by Voucherify.")
    related_object: Optional[StrictStr] = Field(None, description="Used along with the source_id property, can be set to either sku or product.")
    source_id: Optional[StrictStr] = Field(None, description="The merchant's product/SKU ID (if it is different from the Voucherify product/SKU ID). It is useful in the integration between multiple systems. It can be an ID from an eCommerce site, a database, or a third-party service.")
    quantity: Optional[StrictInt] = Field(None, description="The quantity of the particular item in the cart.")
    discount_quantity: Optional[StrictInt] = Field(None, description="Number of dicounted items.")
    initial_quantity: Optional[StrictInt] = Field(None, description="A positive integer in the smallest unit quantity representing the total amount of the order; this is the sum of the order items' quantity.")
    amount: Optional[StrictInt] = Field(None, description="The total amount of the order item (price * quantity).")
    discount_amount: Optional[StrictInt] = Field(None, description="Sum of all order-item-level discounts applied to the order.")
    initial_amount: Optional[StrictInt] = Field(None, description="A positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the total amount of the order. This is the sum of the order items' amounts.")
    price: Optional[StrictInt] = Field(None, description="Unit price of an item. Value is multiplied by 100 to precisely represent 2 decimal places. For example `10000 cents` for `$100.00`.")
    product: Optional[OrderItemProduct] = None
    sku: Optional[OrderItemSku] = None
    metadata: Optional[Dict[str, Any]] = Field(None, description="A set of custom key/value pairs that you can attach to an order item. It can be useful for storing additional information about the order item in a structured format.")
    __properties = ["sku_id", "product_id", "related_object", "source_id", "quantity", "discount_quantity", "initial_quantity", "amount", "discount_amount", "initial_amount", "price", "product", "sku", "metadata"]

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
    def from_json(cls, json_str: str) -> OrderItem:
        """Create an instance of OrderItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of product
        if self.product:
            _dict['product'] = self.product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sku
        if self.sku:
            _dict['sku'] = self.sku.to_dict()
        # set to None if sku_id (nullable) is None
        # and __fields_set__ contains the field
        if self.sku_id is None and "sku_id" in self.__fields_set__:
            _dict['sku_id'] = None

        # set to None if product_id (nullable) is None
        # and __fields_set__ contains the field
        if self.product_id is None and "product_id" in self.__fields_set__:
            _dict['product_id'] = None

        # set to None if related_object (nullable) is None
        # and __fields_set__ contains the field
        if self.related_object is None and "related_object" in self.__fields_set__:
            _dict['related_object'] = None

        # set to None if source_id (nullable) is None
        # and __fields_set__ contains the field
        if self.source_id is None and "source_id" in self.__fields_set__:
            _dict['source_id'] = None

        # set to None if quantity (nullable) is None
        # and __fields_set__ contains the field
        if self.quantity is None and "quantity" in self.__fields_set__:
            _dict['quantity'] = None

        # set to None if discount_quantity (nullable) is None
        # and __fields_set__ contains the field
        if self.discount_quantity is None and "discount_quantity" in self.__fields_set__:
            _dict['discount_quantity'] = None

        # set to None if initial_quantity (nullable) is None
        # and __fields_set__ contains the field
        if self.initial_quantity is None and "initial_quantity" in self.__fields_set__:
            _dict['initial_quantity'] = None

        # set to None if amount (nullable) is None
        # and __fields_set__ contains the field
        if self.amount is None and "amount" in self.__fields_set__:
            _dict['amount'] = None

        # set to None if discount_amount (nullable) is None
        # and __fields_set__ contains the field
        if self.discount_amount is None and "discount_amount" in self.__fields_set__:
            _dict['discount_amount'] = None

        # set to None if initial_amount (nullable) is None
        # and __fields_set__ contains the field
        if self.initial_amount is None and "initial_amount" in self.__fields_set__:
            _dict['initial_amount'] = None

        # set to None if price (nullable) is None
        # and __fields_set__ contains the field
        if self.price is None and "price" in self.__fields_set__:
            _dict['price'] = None

        # set to None if product (nullable) is None
        # and __fields_set__ contains the field
        if self.product is None and "product" in self.__fields_set__:
            _dict['product'] = None

        # set to None if sku (nullable) is None
        # and __fields_set__ contains the field
        if self.sku is None and "sku" in self.__fields_set__:
            _dict['sku'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrderItem:
        """Create an instance of OrderItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrderItem.parse_obj(obj)

        _obj = OrderItem.parse_obj({
            "sku_id": obj.get("sku_id"),
            "product_id": obj.get("product_id"),
            "related_object": obj.get("related_object"),
            "source_id": obj.get("source_id"),
            "quantity": obj.get("quantity"),
            "discount_quantity": obj.get("discount_quantity"),
            "initial_quantity": obj.get("initial_quantity"),
            "amount": obj.get("amount"),
            "discount_amount": obj.get("discount_amount"),
            "initial_amount": obj.get("initial_amount"),
            "price": obj.get("price"),
            "product": OrderItemProduct.from_dict(obj.get("product")) if obj.get("product") is not None else None,
            "sku": OrderItemSku.from_dict(obj.get("sku")) if obj.get("sku") is not None else None,
            "metadata": obj.get("metadata")
        })
        return _obj


