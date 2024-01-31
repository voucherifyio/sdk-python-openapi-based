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
from pydantic import BaseModel, Field, StrictInt

class PromotionTierSummaryOrders(BaseModel):
    """
    Contains statistics about orders related to the promotion tier.  # noqa: E501
    """
    total_amount: Optional[StrictInt] = Field(None, description="Sum of order totals.")
    total_discount_amount: Optional[StrictInt] = Field(None, description="Sum of total discount applied using the promotion tier.")
    __properties = ["total_amount", "total_discount_amount"]

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
    def from_json(cls, json_str: str) -> PromotionTierSummaryOrders:
        """Create an instance of PromotionTierSummaryOrders from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PromotionTierSummaryOrders:
        """Create an instance of PromotionTierSummaryOrders from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PromotionTierSummaryOrders.parse_obj(obj)

        _obj = PromotionTierSummaryOrders.parse_obj({
            "total_amount": obj.get("total_amount"),
            "total_discount_amount": obj.get("total_discount_amount")
        })
        return _obj


