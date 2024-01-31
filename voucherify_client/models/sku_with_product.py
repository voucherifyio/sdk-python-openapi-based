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
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator
from voucherify_client.models.product_without_skus import ProductWithoutSkus

class SkuWithProduct(BaseModel):
    """
    SkuWithProduct
    """
    id: StrictStr = Field(..., description="A unique identifier that represents the SKU and is assigned by Voucherify.")
    source_id: Optional[StrictStr] = Field(None, description="A unique SKU identifier from your inventory system.")
    product_id: StrictStr = Field(..., description="The parent product's unique ID.")
    sku: Optional[StrictStr] = Field(None, description="Unique user-defined SKU name.")
    price: Optional[StrictInt] = Field(None, description="Unit price. It is represented by a value multiplied by 100 to accurately reflect 2 decimal places, such as `$100.00` being expressed as `10000`.")
    currency: Optional[StrictStr] = Field(None, description="SKU price currency.")
    attributes: Dict[str, Any] = Field(..., description="The attributes object stores values for all custom attributes inherited by the SKU from the parent product. A set of key/value pairs that are attached to a SKU object and are unique to each SKU within a product family.")
    image_url: Optional[StrictStr] = Field(None, description="The HTTPS URL pointing to the .png or .jpg file that will be used to render the SKU image.")
    metadata: Dict[str, Any] = Field(..., description="The metadata object stores all custom attributes assigned to the SKU. A set of key/value pairs that you can attach to a SKU object. It can be useful for storing additional information about the SKU in a structured format.")
    created_at: datetime = Field(..., description="Timestamp representing the date and time when the SKU was created in ISO 8601 format.")
    updated_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the SKU was updated in ISO 8601 format.")
    object: StrictStr = Field(..., description="The type of object represented by JSON. This object stores information about the `SKU`.")
    product: Optional[ProductWithoutSkus] = None
    __properties = ["id", "source_id", "product_id", "sku", "price", "currency", "attributes", "image_url", "metadata", "created_at", "updated_at", "object", "product"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('sku',):
            raise ValueError("must be one of enum values ('sku')")
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
    def from_json(cls, json_str: str) -> SkuWithProduct:
        """Create an instance of SkuWithProduct from a JSON string"""
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
        # set to None if source_id (nullable) is None
        # and __fields_set__ contains the field
        if self.source_id is None and "source_id" in self.__fields_set__:
            _dict['source_id'] = None

        # set to None if sku (nullable) is None
        # and __fields_set__ contains the field
        if self.sku is None and "sku" in self.__fields_set__:
            _dict['sku'] = None

        # set to None if price (nullable) is None
        # and __fields_set__ contains the field
        if self.price is None and "price" in self.__fields_set__:
            _dict['price'] = None

        # set to None if currency (nullable) is None
        # and __fields_set__ contains the field
        if self.currency is None and "currency" in self.__fields_set__:
            _dict['currency'] = None

        # set to None if image_url (nullable) is None
        # and __fields_set__ contains the field
        if self.image_url is None and "image_url" in self.__fields_set__:
            _dict['image_url'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SkuWithProduct:
        """Create an instance of SkuWithProduct from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SkuWithProduct.parse_obj(obj)

        _obj = SkuWithProduct.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("source_id"),
            "product_id": obj.get("product_id"),
            "sku": obj.get("sku"),
            "price": obj.get("price"),
            "currency": obj.get("currency"),
            "attributes": obj.get("attributes"),
            "image_url": obj.get("image_url"),
            "metadata": obj.get("metadata"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "object": obj.get("object") if obj.get("object") is not None else 'sku',
            "product": ProductWithoutSkus.from_dict(obj.get("product")) if obj.get("product") is not None else None
        })
        return _obj


