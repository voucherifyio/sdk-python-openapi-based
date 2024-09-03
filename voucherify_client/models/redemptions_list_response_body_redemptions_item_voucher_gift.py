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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class RedemptionsListResponseBodyRedemptionsItemVoucherGift(BaseModel):
    """
    RedemptionsListResponseBodyRedemptionsItemVoucherGift
    """
    amount: Optional[StrictInt] = Field(None, description="Total gift card income over the lifetime of the card. Value is multiplied by 100 to precisely represent 2 decimal places. For example, $100 amount is written as 10000.")
    balance: Optional[StrictInt] = Field(None, description="Available funds. Value is multiplied by 100 to precisely represent 2 decimal places. For example, $100 amount is written as 10000.")
    effect: Optional[StrictStr] = Field(None, description="Defines how the credits are applied to the customer's order.")
    __properties = ["amount", "balance", "effect"]

    @validator('effect')
    def effect_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('APPLY_TO_ORDER', 'APPLY_TO_ITEMS',):
            raise ValueError("must be one of enum values ('APPLY_TO_ORDER', 'APPLY_TO_ITEMS')")
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
    def from_json(cls, json_str: str) -> RedemptionsListResponseBodyRedemptionsItemVoucherGift:
        """Create an instance of RedemptionsListResponseBodyRedemptionsItemVoucherGift from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if amount (nullable) is None
        # and __fields_set__ contains the field
        if self.amount is None and "amount" in self.__fields_set__:
            _dict['amount'] = None

        # set to None if balance (nullable) is None
        # and __fields_set__ contains the field
        if self.balance is None and "balance" in self.__fields_set__:
            _dict['balance'] = None

        # set to None if effect (nullable) is None
        # and __fields_set__ contains the field
        if self.effect is None and "effect" in self.__fields_set__:
            _dict['effect'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RedemptionsListResponseBodyRedemptionsItemVoucherGift:
        """Create an instance of RedemptionsListResponseBodyRedemptionsItemVoucherGift from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RedemptionsListResponseBodyRedemptionsItemVoucherGift.parse_obj(obj)

        _obj = RedemptionsListResponseBodyRedemptionsItemVoucherGift.parse_obj({
            "amount": obj.get("amount"),
            "balance": obj.get("balance"),
            "effect": obj.get("effect")
        })
        return _obj


