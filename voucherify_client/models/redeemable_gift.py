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
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class RedeemableGift(BaseModel):
    """
    Contains current gift card balance information.  # noqa: E501
    """
    balance: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="Available funds. Value is multiplied by 100 to precisely represent 2 decimal places. For example, $100 amount is written as 10000.")
    credits: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The number of credits that the user wants to use from the gift card to fulfil the order. The value of credits cannot be higher than the current balance on the gift card. If the user gives more points than he has on the gift card, the application will return an error code in response. Value is multiplied by 100 to precisely represent 2 decimal places. For example `10000 cents` for `$100.00`.")
    __properties = ["balance", "credits"]

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
    def from_json(cls, json_str: str) -> RedeemableGift:
        """Create an instance of RedeemableGift from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if balance (nullable) is None
        # and __fields_set__ contains the field
        if self.balance is None and "balance" in self.__fields_set__:
            _dict['balance'] = None

        # set to None if credits (nullable) is None
        # and __fields_set__ contains the field
        if self.credits is None and "credits" in self.__fields_set__:
            _dict['credits'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RedeemableGift:
        """Create an instance of RedeemableGift from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RedeemableGift.parse_obj(obj)

        _obj = RedeemableGift.parse_obj({
            "balance": obj.get("balance"),
            "credits": obj.get("credits")
        })
        return _obj


