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


from typing import Any, Dict, List
from pydantic import BaseModel, Field, StrictStr, conlist

class ProductsMetadataUpdateInBulkRequestBody(BaseModel):
    """
    Request schema for **POST** `/products/metadata/async`.  # noqa: E501
    """
    source_ids: conlist(StrictStr) = Field(..., description="Array of unique product source IDs.")
    metadata: Dict[str, Any] = Field(..., description="The metadata object stores all custom attributes assigned to the product. A set of key/value pairs that you can attach to a product object. It can be useful for storing additional information about the product in a structured format.")
    __properties = ["source_ids", "metadata"]

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
    def from_json(cls, json_str: str) -> ProductsMetadataUpdateInBulkRequestBody:
        """Create an instance of ProductsMetadataUpdateInBulkRequestBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductsMetadataUpdateInBulkRequestBody:
        """Create an instance of ProductsMetadataUpdateInBulkRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProductsMetadataUpdateInBulkRequestBody.parse_obj(obj)

        _obj = ProductsMetadataUpdateInBulkRequestBody.parse_obj({
            "source_ids": obj.get("source_ids"),
            "metadata": obj.get("metadata")
        })
        return _obj


