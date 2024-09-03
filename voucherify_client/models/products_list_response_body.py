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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from voucherify_client.models.product import Product

class ProductsListResponseBody(BaseModel):
    """
    Response body schema for **GET** `v1/products`.  # noqa: E501
    """
    object: Optional[StrictStr] = Field('list', description="The type of the object represented by JSON. This object stores information about products in a dictionary.")
    data_ref: Optional[StrictStr] = Field('products', description="Identifies the name of the attribute that contains the array of product objects.")
    products: Optional[conlist(Product)] = Field(None, description="Contains array of product objects.")
    total: Optional[StrictInt] = Field(None, description="Total number of product objects.")
    __properties = ["object", "data_ref", "products", "total"]

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
    def from_json(cls, json_str: str) -> ProductsListResponseBody:
        """Create an instance of ProductsListResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in products (list)
        _items = []
        if self.products:
            for _item in self.products:
                if _item:
                    _items.append(_item.to_dict())
            _dict['products'] = _items
        # set to None if object (nullable) is None
        # and __fields_set__ contains the field
        if self.object is None and "object" in self.__fields_set__:
            _dict['object'] = None

        # set to None if data_ref (nullable) is None
        # and __fields_set__ contains the field
        if self.data_ref is None and "data_ref" in self.__fields_set__:
            _dict['data_ref'] = None

        # set to None if products (nullable) is None
        # and __fields_set__ contains the field
        if self.products is None and "products" in self.__fields_set__:
            _dict['products'] = None

        # set to None if total (nullable) is None
        # and __fields_set__ contains the field
        if self.total is None and "total" in self.__fields_set__:
            _dict['total'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductsListResponseBody:
        """Create an instance of ProductsListResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProductsListResponseBody.parse_obj(obj)

        _obj = ProductsListResponseBody.parse_obj({
            "object": obj.get("object") if obj.get("object") is not None else 'list',
            "data_ref": obj.get("data_ref") if obj.get("data_ref") is not None else 'products',
            "products": [Product.from_dict(_item) for _item in obj.get("products")] if obj.get("products") is not None else None,
            "total": obj.get("total")
        })
        return _obj


