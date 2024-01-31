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
from pydantic import BaseModel, Field, StrictStr, constr

class LuckyDraw(BaseModel):
    """
    Object for defining detailed information about lucky draw should be applied  # noqa: E501
    """
    winners_count: Optional[constr(strict=True)] = Field(None, description="It represents the total number of winners in a lucky draw.")
    unique_winners_per_draw: Optional[StrictStr] = Field(None, description="It indicates whether each winner in a draw is unique or not.")
    unique_winners: Optional[StrictStr] = Field(None, description="Specifies whether each participant can win only once across multiple draws.")
    __properties = ["winners_count", "unique_winners_per_draw", "unique_winners"]

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
    def from_json(cls, json_str: str) -> LuckyDraw:
        """Create an instance of LuckyDraw from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LuckyDraw:
        """Create an instance of LuckyDraw from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LuckyDraw.parse_obj(obj)

        _obj = LuckyDraw.parse_obj({
            "winners_count": obj.get("winners_count"),
            "unique_winners_per_draw": obj.get("unique_winners_per_draw"),
            "unique_winners": obj.get("unique_winners")
        })
        return _obj


