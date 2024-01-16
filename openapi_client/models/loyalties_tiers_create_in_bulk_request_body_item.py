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
from openapi_client.models.loyalty_tier_base_points import LoyaltyTierBasePoints

class LoyaltiesTiersCreateInBulkRequestBodyItem(BaseModel):
    """
    LoyaltiesTiersCreateInBulkRequestBodyItem
    """
    name: StrictStr = Field(..., description="Loyalty Tier name.")
    earning_rules: Optional[Dict[str, Any]] = Field(None, description="Contains a list of earning rule IDs and their points mapping for the given earning rule.")
    rewards: Optional[Dict[str, Any]] = Field(None, description="Contains a list of reward IDs and their points mapping for the given reward.")
    points: LoyaltyTierBasePoints = Field(...)
    metadata: Optional[Dict[str, Any]] = Field(None, description="The metadata object stores all custom attributes assigned to the loyalty tier. A set of key/value pairs that you can attach to a loyalty tier object. It can be useful for storing additional information about the loyalty tier in a structured format.")
    __properties = ["name", "earning_rules", "rewards", "points", "metadata"]

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
    def from_json(cls, json_str: str) -> LoyaltiesTiersCreateInBulkRequestBodyItem:
        """Create an instance of LoyaltiesTiersCreateInBulkRequestBodyItem from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltiesTiersCreateInBulkRequestBodyItem:
        """Create an instance of LoyaltiesTiersCreateInBulkRequestBodyItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesTiersCreateInBulkRequestBodyItem.parse_obj(obj)

        _obj = LoyaltiesTiersCreateInBulkRequestBodyItem.parse_obj({
            "name": obj.get("name"),
            "earning_rules": obj.get("earning_rules"),
            "rewards": obj.get("rewards"),
            "points": LoyaltyTierBasePoints.from_dict(obj.get("points")) if obj.get("points") is not None else None,
            "metadata": obj.get("metadata")
        })
        return _obj


