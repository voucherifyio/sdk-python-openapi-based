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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class OrderCalculatedItemSku(BaseModel):
    """
    An object containing details of the related SKU.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="A unique identifier that represents the SKU and is assigned by Voucherify.")
    source_id: Optional[StrictStr] = Field(None, description="The merchant's SKU ID (if it is different than Voucherify's SKU ID). It is really useful in case of integration between multiple systems. It can be an ID from an eCommerce site, a database or a 3rd party service.")
    override: Optional[StrictBool] = Field(None, description="The override set to `true` is used to store the product information in the system. If the product does not exist, it will be created with a source_id; if it does exist, the provided values for the name, price, and metadata will replace those already stored in the system.")
    sku: Optional[StrictStr] = Field(None, description="The SKU name.")
    price: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="SKU price. A positive integer in the smallest currency unit (e.g. 100 cents for $1.00).")
    __properties = ["id", "source_id", "override", "sku", "price"]

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
    def from_json(cls, json_str: str) -> OrderCalculatedItemSku:
        """Create an instance of OrderCalculatedItemSku from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if source_id (nullable) is None
        # and __fields_set__ contains the field
        if self.source_id is None and "source_id" in self.__fields_set__:
            _dict['source_id'] = None

        # set to None if override (nullable) is None
        # and __fields_set__ contains the field
        if self.override is None and "override" in self.__fields_set__:
            _dict['override'] = None

        # set to None if sku (nullable) is None
        # and __fields_set__ contains the field
        if self.sku is None and "sku" in self.__fields_set__:
            _dict['sku'] = None

        # set to None if price (nullable) is None
        # and __fields_set__ contains the field
        if self.price is None and "price" in self.__fields_set__:
            _dict['price'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrderCalculatedItemSku:
        """Create an instance of OrderCalculatedItemSku from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrderCalculatedItemSku.parse_obj(obj)

        _obj = OrderCalculatedItemSku.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("source_id"),
            "override": obj.get("override"),
            "sku": obj.get("sku"),
            "price": obj.get("price")
        })
        return _obj


