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

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, StrictInt

class RedemptionsListResponseBodyRedemptionsItemVoucherLoyaltyCard(BaseModel):
    """
    RedemptionsListResponseBodyRedemptionsItemVoucherLoyaltyCard
    """
    points: Optional[StrictInt] = Field(None, description="Total points incurred over the lifespan of the loyalty card.")
    balance: Optional[StrictInt] = Field(None, description="Points available for reward redemption.")
    next_expiration_date: Optional[date] = Field(None, description="The next closest date when the next set of points are due to expire.")
    next_expiration_points: Optional[StrictInt] = Field(None, description="The amount of points that are set to expire next.")
    __properties = ["points", "balance", "next_expiration_date", "next_expiration_points"]

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
    def from_json(cls, json_str: str) -> RedemptionsListResponseBodyRedemptionsItemVoucherLoyaltyCard:
        """Create an instance of RedemptionsListResponseBodyRedemptionsItemVoucherLoyaltyCard from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if points (nullable) is None
        # and __fields_set__ contains the field
        if self.points is None and "points" in self.__fields_set__:
            _dict['points'] = None

        # set to None if balance (nullable) is None
        # and __fields_set__ contains the field
        if self.balance is None and "balance" in self.__fields_set__:
            _dict['balance'] = None

        # set to None if next_expiration_date (nullable) is None
        # and __fields_set__ contains the field
        if self.next_expiration_date is None and "next_expiration_date" in self.__fields_set__:
            _dict['next_expiration_date'] = None

        # set to None if next_expiration_points (nullable) is None
        # and __fields_set__ contains the field
        if self.next_expiration_points is None and "next_expiration_points" in self.__fields_set__:
            _dict['next_expiration_points'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RedemptionsListResponseBodyRedemptionsItemVoucherLoyaltyCard:
        """Create an instance of RedemptionsListResponseBodyRedemptionsItemVoucherLoyaltyCard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RedemptionsListResponseBodyRedemptionsItemVoucherLoyaltyCard.parse_obj(obj)

        _obj = RedemptionsListResponseBodyRedemptionsItemVoucherLoyaltyCard.parse_obj({
            "points": obj.get("points"),
            "balance": obj.get("balance"),
            "next_expiration_date": obj.get("next_expiration_date"),
            "next_expiration_points": obj.get("next_expiration_points")
        })
        return _obj


