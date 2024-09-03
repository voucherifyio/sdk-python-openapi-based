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

class RewardsCreateRequestBodyParametersCoin(BaseModel):
    """
    Define the ratio by mapping the number of loyalty points in `points_ratio` to a predefined cash amount in `exchange_ratio`.  # noqa: E501
    """
    exchange_ratio: Optional[StrictStr] = Field(None, description="The cash equivalent of the points defined in the `points_ratio` property.")
    points_ratio: Optional[StrictStr] = Field(None, description="The number of loyalty points that will map to the predefined cash amount defined by the `exchange_ratio` property.")
    __properties = ["exchange_ratio", "points_ratio"]

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
    def from_json(cls, json_str: str) -> RewardsCreateRequestBodyParametersCoin:
        """Create an instance of RewardsCreateRequestBodyParametersCoin from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if exchange_ratio (nullable) is None
        # and __fields_set__ contains the field
        if self.exchange_ratio is None and "exchange_ratio" in self.__fields_set__:
            _dict['exchange_ratio'] = None

        # set to None if points_ratio (nullable) is None
        # and __fields_set__ contains the field
        if self.points_ratio is None and "points_ratio" in self.__fields_set__:
            _dict['points_ratio'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RewardsCreateRequestBodyParametersCoin:
        """Create an instance of RewardsCreateRequestBodyParametersCoin from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RewardsCreateRequestBodyParametersCoin.parse_obj(obj)

        _obj = RewardsCreateRequestBodyParametersCoin.parse_obj({
            "exchange_ratio": obj.get("exchange_ratio"),
            "points_ratio": obj.get("points_ratio")
        })
        return _obj


