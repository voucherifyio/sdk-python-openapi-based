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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, conlist
from openapi_client.models.loyalties_transfer_points import LoyaltiesTransferPoints

class RedeemableLoyaltyCard(BaseModel):
    """
    Redeemable loyalty card object response  # noqa: E501
    """
    points: Optional[StrictInt] = Field(None, description="Total points incurred over lifespan of loyalty card.")
    balance: Optional[StrictInt] = Field(None, description="Points available for reward redemption.")
    exchange_ratio: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The cash equivalent of the points defined in the points_ratio property.")
    points_ratio: Optional[StrictInt] = Field(None, description="The number of loyalty points that will map to the predefined cash amount defined by the exchange_ratio property.")
    transfers: Optional[conlist(LoyaltiesTransferPoints)] = None
    __properties = ["points", "balance", "exchange_ratio", "points_ratio", "transfers"]

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
    def from_json(cls, json_str: str) -> RedeemableLoyaltyCard:
        """Create an instance of RedeemableLoyaltyCard from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in transfers (list)
        _items = []
        if self.transfers:
            for _item in self.transfers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transfers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RedeemableLoyaltyCard:
        """Create an instance of RedeemableLoyaltyCard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RedeemableLoyaltyCard.parse_obj(obj)

        _obj = RedeemableLoyaltyCard.parse_obj({
            "points": obj.get("points"),
            "balance": obj.get("balance"),
            "exchange_ratio": obj.get("exchange_ratio"),
            "points_ratio": obj.get("points_ratio"),
            "transfers": [LoyaltiesTransferPoints.from_dict(_item) for _item in obj.get("transfers")] if obj.get("transfers") is not None else None
        })
        return _obj


