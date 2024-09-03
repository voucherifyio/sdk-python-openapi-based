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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator
from voucherify_client.models.product_collections_item import ProductCollectionsItem

class ProductCollectionsListResponseBody(BaseModel):
    """
    Response body schema for **GET** `v1/product-collections`.  # noqa: E501
    """
    object: Optional[StrictStr] = Field('list', description="The type of the object represented by JSON. This object stores information about product collections.")
    data_ref: Optional[StrictStr] = Field('data', description="Identifies the name of the JSON property that contains the array of product collections.")
    data: Optional[conlist(ProductCollectionsItem)] = Field(None, description="A dictionary that contains an array of product collections and their details.")
    total: Optional[StrictInt] = Field(None, description="Total number of product collections.")
    __properties = ["object", "data_ref", "data", "total"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('list',):
            raise ValueError("must be one of enum values ('list')")
        return value

    @validator('data_ref')
    def data_ref_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('data',):
            raise ValueError("must be one of enum values ('data')")
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
    def from_json(cls, json_str: str) -> ProductCollectionsListResponseBody:
        """Create an instance of ProductCollectionsListResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        # set to None if object (nullable) is None
        # and __fields_set__ contains the field
        if self.object is None and "object" in self.__fields_set__:
            _dict['object'] = None

        # set to None if data_ref (nullable) is None
        # and __fields_set__ contains the field
        if self.data_ref is None and "data_ref" in self.__fields_set__:
            _dict['data_ref'] = None

        # set to None if data (nullable) is None
        # and __fields_set__ contains the field
        if self.data is None and "data" in self.__fields_set__:
            _dict['data'] = None

        # set to None if total (nullable) is None
        # and __fields_set__ contains the field
        if self.total is None and "total" in self.__fields_set__:
            _dict['total'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductCollectionsListResponseBody:
        """Create an instance of ProductCollectionsListResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProductCollectionsListResponseBody.parse_obj(obj)

        _obj = ProductCollectionsListResponseBody.parse_obj({
            "object": obj.get("object") if obj.get("object") is not None else 'list',
            "data_ref": obj.get("data_ref") if obj.get("data_ref") is not None else 'data',
            "data": [ProductCollectionsItem.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None,
            "total": obj.get("total")
        })
        return _obj


