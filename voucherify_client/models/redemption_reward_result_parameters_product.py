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
from pydantic import BaseModel, Field, StrictStr

class RedemptionRewardResultParametersProduct(BaseModel):
    """
    Defines the product redeemed as a reward.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="Unique product ID, assigned by Voucherify. ")
    sku_id: Optional[StrictStr] = Field(None, description="A unique SKU ID assigned by Voucherify.")
    __properties = ["id", "sku_id"]

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
    def from_json(cls, json_str: str) -> RedemptionRewardResultParametersProduct:
        """Create an instance of RedemptionRewardResultParametersProduct from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RedemptionRewardResultParametersProduct:
        """Create an instance of RedemptionRewardResultParametersProduct from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RedemptionRewardResultParametersProduct.parse_obj(obj)

        _obj = RedemptionRewardResultParametersProduct.parse_obj({
            "id": obj.get("id"),
            "sku_id": obj.get("sku_id")
        })
        return _obj

