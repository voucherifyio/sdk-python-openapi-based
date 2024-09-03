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
from voucherify_client.models.skus_list_for_product import SkusListForProduct

class ProductsUpdateResponseBody(BaseModel):
    """
    Response body schema for **PUT** `v1/products/{productId}`.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="Unique product ID assigned by Voucherify.")
    source_id: Optional[StrictStr] = Field(None, description="Unique product source ID.")
    name: Optional[StrictStr] = Field(None, description="Unique user-defined product name.")
    price: Optional[StrictInt] = Field(None, description="Unit price. It is represented by a value multiplied by 100 to accurately reflect 2 decimal places, such as `$100.00` being expressed as `10000`.")
    attributes: Optional[conlist(StrictStr)] = Field(None, description="A list of product attributes whose values you can customize for given SKUs: `[\"color\",\"size\",\"ranking\"]`. Each child SKU can have a unique value for a given attribute.")
    metadata: Optional[Dict[str, Any]] = Field(None, description="The metadata object stores all custom attributes assigned to the product. A set of key/value pairs that you can attach to a product object. It can be useful for storing additional information about the product in a structured format.")
    image_url: Optional[StrictStr] = Field(None, description="The HTTPS URL pointing to the .png or .jpg file that will be used to render the product image.")
    created_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the product was created. The value is shown in the ISO 8601 format.")
    updated_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the product was updated. The value is shown in the ISO 8601 format.")
    object: Optional[StrictStr] = Field('product', description="The type of the object represented by JSON. This object stores information about the product.")
    skus: Optional[SkusListForProduct] = None
    __properties = ["id", "source_id", "name", "price", "attributes", "metadata", "image_url", "created_at", "updated_at", "object", "skus"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('product',):
            raise ValueError("must be one of enum values ('product')")
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
    def from_json(cls, json_str: str) -> ProductsUpdateResponseBody:
        """Create an instance of ProductsUpdateResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of skus
        if self.skus:
            _dict['skus'] = self.skus.to_dict()
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if source_id (nullable) is None
        # and __fields_set__ contains the field
        if self.source_id is None and "source_id" in self.__fields_set__:
            _dict['source_id'] = None

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

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        # set to None if image_url (nullable) is None
        # and __fields_set__ contains the field
        if self.image_url is None and "image_url" in self.__fields_set__:
            _dict['image_url'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        # set to None if object (nullable) is None
        # and __fields_set__ contains the field
        if self.object is None and "object" in self.__fields_set__:
            _dict['object'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductsUpdateResponseBody:
        """Create an instance of ProductsUpdateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProductsUpdateResponseBody.parse_obj(obj)

        _obj = ProductsUpdateResponseBody.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("source_id"),
            "name": obj.get("name"),
            "price": obj.get("price"),
            "attributes": obj.get("attributes"),
            "metadata": obj.get("metadata"),
            "image_url": obj.get("image_url"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "object": obj.get("object") if obj.get("object") is not None else 'product',
            "skus": SkusListForProduct.from_dict(obj.get("skus")) if obj.get("skus") is not None else None
        })
        return _obj


