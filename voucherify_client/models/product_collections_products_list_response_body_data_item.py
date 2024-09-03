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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator
from voucherify_client.models.product_without_skus import ProductWithoutSkus

class ProductCollectionsProductsListResponseBodyDataItem(BaseModel):
    """
    ProductCollectionsProductsListResponseBodyDataItem
    """
    id: Optional[StrictStr] = None
    source_id: Optional[StrictStr] = None
    name: Optional[StrictStr] = Field(None, description="Unique user-defined product name.")
    price: Optional[StrictInt] = Field(None, description="Unit price. It is represented by a value multiplied by 100 to accurately reflect 2 decimal places, such as `$100.00` being expressed as `10000`.")
    attributes: Optional[conlist(StrictStr)] = Field(None, description="A list of product attributes whose values you can customize for given SKUs: `[\"color\",\"size\",\"ranking\"]`. Each child SKU can have a unique value for a given attribute.")
    metadata: Optional[Dict[str, Any]] = None
    image_url: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    object: Optional[StrictStr] = None
    product_id: Optional[StrictStr] = Field(None, description="The parent product's unique ID.")
    sku: Optional[StrictStr] = Field(None, description="Unique user-defined SKU name.")
    currency: Optional[StrictStr] = Field(None, description="SKU price currency.")
    product: Optional[ProductWithoutSkus] = None
    __properties = ["id", "source_id", "name", "price", "attributes", "metadata", "image_url", "created_at", "updated_at", "object", "product_id", "sku", "currency", "product"]

    @validator('object')
    def object_validate_enum(cls, value):
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
    def from_json(cls, json_str: str) -> ProductCollectionsProductsListResponseBodyDataItem:
        """Create an instance of ProductCollectionsProductsListResponseBodyDataItem from a JSON string"""
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
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if price (nullable) is None
        # and __fields_set__ contains the field
        if self.price is None and "price" in self.__fields_set__:
            _dict['price'] = None

        # set to None if attributes (nullable) is None
        # and __fields_set__ contains the field
        if self.attributes is None and "attributes" in self.__fields_set__:
            _dict['attributes'] = None

        # set to None if product_id (nullable) is None
        # and __fields_set__ contains the field
        if self.product_id is None and "product_id" in self.__fields_set__:
            _dict['product_id'] = None

        # set to None if sku (nullable) is None
        # and __fields_set__ contains the field
        if self.sku is None and "sku" in self.__fields_set__:
            _dict['sku'] = None

        # set to None if currency (nullable) is None
        # and __fields_set__ contains the field
        if self.currency is None and "currency" in self.__fields_set__:
            _dict['currency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductCollectionsProductsListResponseBodyDataItem:
        """Create an instance of ProductCollectionsProductsListResponseBodyDataItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProductCollectionsProductsListResponseBodyDataItem.parse_obj(obj)

        _obj = ProductCollectionsProductsListResponseBodyDataItem.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("source_id"),
            "name": obj.get("name"),
            "price": obj.get("price"),
            "attributes": obj.get("attributes"),
            "metadata": obj.get("metadata"),
            "image_url": obj.get("image_url"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "object": obj.get("object"),
            "product_id": obj.get("product_id"),
            "sku": obj.get("sku"),
            "currency": obj.get("currency"),
            "product": ProductWithoutSkus.from_dict(obj.get("product")) if obj.get("product") is not None else None
        })
        return _obj

