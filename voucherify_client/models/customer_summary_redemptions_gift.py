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

class CustomerSummaryRedemptionsGift(BaseModel):
    """
    Summary of gift card credits.  # noqa: E501
    """
    redeemed_amount: Optional[StrictInt] = Field(0, description="Total amount of gift card credits redeemed by customer. Value is multiplied by 100 to precisely represent 2 decimal places. For example `10000 cents` for `$100.00`.")
    amount_to_go: Optional[StrictInt] = Field(0, description="Remaining gift card balance across all gift cards. Value is multiplied by 100 to precisely represent 2 decimal places. For example `10000 cents` for `$100.00`.")
    __properties = ["redeemed_amount", "amount_to_go"]

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
    def from_json(cls, json_str: str) -> CustomerSummaryRedemptionsGift:
        """Create an instance of CustomerSummaryRedemptionsGift from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if redeemed_amount (nullable) is None
        # and __fields_set__ contains the field
        if self.redeemed_amount is None and "redeemed_amount" in self.__fields_set__:
            _dict['redeemed_amount'] = None

        # set to None if amount_to_go (nullable) is None
        # and __fields_set__ contains the field
        if self.amount_to_go is None and "amount_to_go" in self.__fields_set__:
            _dict['amount_to_go'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomerSummaryRedemptionsGift:
        """Create an instance of CustomerSummaryRedemptionsGift from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomerSummaryRedemptionsGift.parse_obj(obj)

        _obj = CustomerSummaryRedemptionsGift.parse_obj({
            "redeemed_amount": obj.get("redeemed_amount") if obj.get("redeemed_amount") is not None else 0,
            "amount_to_go": obj.get("amount_to_go") if obj.get("amount_to_go") is not None else 0
        })
        return _obj


