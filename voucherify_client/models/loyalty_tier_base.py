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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from voucherify_client.models.loyalty_tier_base_points import LoyaltyTierBasePoints

class LoyaltyTierBase(BaseModel):
    """
    LoyaltyTierBase
    """
    name: Optional[StrictStr] = Field(None, description="Loyalty Tier name.")
    earning_rules: Optional[Dict[str, Any]] = Field(None, description="Contains a list of earning rule IDs and their points mapping for the given earning rule.")
    rewards: Optional[Dict[str, Any]] = Field(None, description="Contains a list of reward IDs and their points mapping for the given reward.")
    points: Optional[LoyaltyTierBasePoints] = None
    __properties = ["name", "earning_rules", "rewards", "points"]

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
    def from_json(cls, json_str: str) -> LoyaltyTierBase:
        """Create an instance of LoyaltyTierBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of points
        if self.points:
            _dict['points'] = self.points.to_dict()
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if earning_rules (nullable) is None
        # and __fields_set__ contains the field
        if self.earning_rules is None and "earning_rules" in self.__fields_set__:
            _dict['earning_rules'] = None

        # set to None if rewards (nullable) is None
        # and __fields_set__ contains the field
        if self.rewards is None and "rewards" in self.__fields_set__:
            _dict['rewards'] = None

        # set to None if points (nullable) is None
        # and __fields_set__ contains the field
        if self.points is None and "points" in self.__fields_set__:
            _dict['points'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltyTierBase:
        """Create an instance of LoyaltyTierBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltyTierBase.parse_obj(obj)

        _obj = LoyaltyTierBase.parse_obj({
            "name": obj.get("name"),
            "earning_rules": obj.get("earning_rules"),
            "rewards": obj.get("rewards"),
            "points": LoyaltyTierBasePoints.from_dict(obj.get("points")) if obj.get("points") is not None else None
        })
        return _obj


