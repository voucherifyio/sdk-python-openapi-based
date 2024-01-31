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
from pydantic import BaseModel, Field
from voucherify_client.models.field_conditions import FieldConditions
from voucherify_client.models.junction import Junction

class ProductCollectionsCreateDynamicRequestBodyFilter(BaseModel):
    """
    Defines a set of criteria and boundary conditions for an `AUTO_UPDATE` product collection type.  # noqa: E501
    """
    junction: Junction = Field(...)
    id: Optional[FieldConditions] = None
    product_id: Optional[FieldConditions] = None
    source_id: Optional[FieldConditions] = None
    name: Optional[FieldConditions] = None
    price: Optional[FieldConditions] = None
    object: Optional[FieldConditions] = None
    attributes: Optional[FieldConditions] = None
    metadata: Optional[FieldConditions] = None
    image_url: Optional[FieldConditions] = None
    skus: Optional[FieldConditions] = None
    created_at: Optional[FieldConditions] = None
    updated_at: Optional[FieldConditions] = None
    __properties = ["junction", "id", "product_id", "source_id", "name", "price", "object", "attributes", "metadata", "image_url", "skus", "created_at", "updated_at"]

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
    def from_json(cls, json_str: str) -> ProductCollectionsCreateDynamicRequestBodyFilter:
        """Create an instance of ProductCollectionsCreateDynamicRequestBodyFilter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product_id
        if self.product_id:
            _dict['product_id'] = self.product_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source_id
        if self.source_id:
            _dict['source_id'] = self.source_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of name
        if self.name:
            _dict['name'] = self.name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of object
        if self.object:
            _dict['object'] = self.object.to_dict()
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict['attributes'] = self.attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of image_url
        if self.image_url:
            _dict['image_url'] = self.image_url.to_dict()
        # override the default output from pydantic by calling `to_dict()` of skus
        if self.skus:
            _dict['skus'] = self.skus.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_at
        if self.created_at:
            _dict['created_at'] = self.created_at.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_at
        if self.updated_at:
            _dict['updated_at'] = self.updated_at.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductCollectionsCreateDynamicRequestBodyFilter:
        """Create an instance of ProductCollectionsCreateDynamicRequestBodyFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProductCollectionsCreateDynamicRequestBodyFilter.parse_obj(obj)

        _obj = ProductCollectionsCreateDynamicRequestBodyFilter.parse_obj({
            "junction": obj.get("junction"),
            "id": FieldConditions.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "product_id": FieldConditions.from_dict(obj.get("product_id")) if obj.get("product_id") is not None else None,
            "source_id": FieldConditions.from_dict(obj.get("source_id")) if obj.get("source_id") is not None else None,
            "name": FieldConditions.from_dict(obj.get("name")) if obj.get("name") is not None else None,
            "price": FieldConditions.from_dict(obj.get("price")) if obj.get("price") is not None else None,
            "object": FieldConditions.from_dict(obj.get("object")) if obj.get("object") is not None else None,
            "attributes": FieldConditions.from_dict(obj.get("attributes")) if obj.get("attributes") is not None else None,
            "metadata": FieldConditions.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "image_url": FieldConditions.from_dict(obj.get("image_url")) if obj.get("image_url") is not None else None,
            "skus": FieldConditions.from_dict(obj.get("skus")) if obj.get("skus") is not None else None,
            "created_at": FieldConditions.from_dict(obj.get("created_at")) if obj.get("created_at") is not None else None,
            "updated_at": FieldConditions.from_dict(obj.get("updated_at")) if obj.get("updated_at") is not None else None
        })
        return _obj


