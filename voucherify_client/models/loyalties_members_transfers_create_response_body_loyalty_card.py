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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class LoyaltiesMembersTransfersCreateResponseBodyLoyaltyCard(BaseModel):
    """
    Object representing loyalty card parameters. Child attributes are present only if type is LOYALTY_CARD.  # noqa: E501
    """
    points: StrictInt = Field(..., description="Total points incurred over lifespan of loyalty card.")
    balance: StrictInt = Field(..., description="Points available for reward redemption.")
    next_expiration_date: Optional[StrictStr] = Field(None, description="The next closest date when the next set of points are due to expire.")
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
    def from_json(cls, json_str: str) -> LoyaltiesMembersTransfersCreateResponseBodyLoyaltyCard:
        """Create an instance of LoyaltiesMembersTransfersCreateResponseBodyLoyaltyCard from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltiesMembersTransfersCreateResponseBodyLoyaltyCard:
        """Create an instance of LoyaltiesMembersTransfersCreateResponseBodyLoyaltyCard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesMembersTransfersCreateResponseBodyLoyaltyCard.parse_obj(obj)

        _obj = LoyaltiesMembersTransfersCreateResponseBodyLoyaltyCard.parse_obj({
            "points": obj.get("points"),
            "balance": obj.get("balance"),
            "next_expiration_date": obj.get("next_expiration_date"),
            "next_expiration_points": obj.get("next_expiration_points")
        })
        return _obj


