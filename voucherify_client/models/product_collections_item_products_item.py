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
from pydantic import BaseModel, Field, StrictStr, validator

class ProductCollectionsItemProductsItem(BaseModel):
    """
    ProductCollectionsItemProductsItem
    """
    id: StrictStr = Field(..., description="The product ID.")
    product_id: Optional[StrictStr] = Field(None, description="Product ID for SKUs.")
    object: StrictStr = Field(..., description="Denotes the type of the object represented by the ID.")
    __properties = ["id", "product_id", "object"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('sku', 'product',):
            raise ValueError("must be one of enum values ('sku', 'product')")
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
    def from_json(cls, json_str: str) -> ProductCollectionsItemProductsItem:
        """Create an instance of ProductCollectionsItemProductsItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductCollectionsItemProductsItem:
        """Create an instance of ProductCollectionsItemProductsItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProductCollectionsItemProductsItem.parse_obj(obj)

        _obj = ProductCollectionsItemProductsItem.parse_obj({
            "id": obj.get("id"),
            "product_id": obj.get("product_id"),
            "object": obj.get("object")
        })
        return _obj


