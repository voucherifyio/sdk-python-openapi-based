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
from pydantic import BaseModel, Field, StrictStr, conlist, validator

class RedemptionsRedeemRequestBodyOptions(BaseModel):
    """
    Configure parameters returned in the response.  # noqa: E501
    """
    expand: Optional[conlist(StrictStr)] = Field(None, description="Expand array lets you configure params included in the response. Depending on the strings included in the array, the response will contain different details.   | **Expand Option** | **Response Body** | |:---|:---| | [\"order\"] | - Same response as fallback response (without an options object).<br>- Order data with calculated discounts are listed in each child redeemable object.<br>- Metadata not included for each discount type. | | [\"redeemable\"] | Expands redeemable objects by including `metadata` for each discount type. | | [\"order\", \"redeemable\"] | - Order data with calculated discounts are listed in each child redeemable object.<br>- Includes `metadata` for each discount type. | | [\"redeemable\", \"redemption\", \"category\"] | - Returns each discount type's `metadata` in each child redemption object.<br>- Returns redemption object `metadata`.<br>- Returns an expanded `categories` object, showing details about the category. |")
    __properties = ["expand"]

    @validator('expand')
    def expand_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('order', 'redemption', 'redeemable', 'category',):
                raise ValueError("each list item must be one of ('order', 'redemption', 'redeemable', 'category')")
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
    def from_json(cls, json_str: str) -> RedemptionsRedeemRequestBodyOptions:
        """Create an instance of RedemptionsRedeemRequestBodyOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if expand (nullable) is None
        # and __fields_set__ contains the field
        if self.expand is None and "expand" in self.__fields_set__:
            _dict['expand'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RedemptionsRedeemRequestBodyOptions:
        """Create an instance of RedemptionsRedeemRequestBodyOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RedemptionsRedeemRequestBodyOptions.parse_obj(obj)

        _obj = RedemptionsRedeemRequestBodyOptions.parse_obj({
            "expand": obj.get("expand")
        })
        return _obj


