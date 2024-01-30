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


from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class OrderItemProduct(BaseModel):
    """
    An object containing details of the related product.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="A unique identifier that represents the product and is assigned by Voucherify.")
    source_id: Optional[StrictStr] = Field(None, description="The merchant’s product ID (if it is different than Voucherify's product ID). It is really useful in case of integration between multiple systems. It can be an ID from an eCommerce site, a database or a 3rd party service.")
    override: Optional[StrictBool] = Field(None, description="The override set to `true` is used to store the product information in the system. If the product does not exist, it will be created with a source_id; if it does exist, the provided values for the name, price, and metadata will replace those already stored in the system.")
    name: Optional[StrictStr] = Field(None, description="Product name.")
    metadata: Optional[Dict[str, Any]] = Field(None, description="A set of custom key/value pairs that you can attach to a product. It can be useful for storing additional information about the product in a structured format.")
    price: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Product price. A positive integer in the smallest currency unit (e.g. 100 cents for $1.00).")
    __properties = ["id", "source_id", "override", "name", "metadata", "price"]

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
    def from_json(cls, json_str: str) -> OrderItemProduct:
        """Create an instance of OrderItemProduct from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrderItemProduct:
        """Create an instance of OrderItemProduct from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrderItemProduct.parse_obj(obj)

        _obj = OrderItemProduct.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("source_id"),
            "override": obj.get("override"),
            "name": obj.get("name"),
            "metadata": obj.get("metadata"),
            "price": obj.get("price")
        })
        return _obj

