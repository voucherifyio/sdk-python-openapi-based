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

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, validator
from openapi_client.models.loyalty_tier_all_of_config import LoyaltyTierAllOfConfig
from openapi_client.models.loyalty_tier_base_points import LoyaltyTierBasePoints
from openapi_client.models.loyalty_tier_expiration import LoyaltyTierExpiration

class LoyaltyTier(BaseModel):
    """
    LoyaltyTier
    """
    name: StrictStr = Field(..., description="Loyalty Tier name.")
    earning_rules: Optional[Dict[str, Any]] = Field(None, description="Contains a list of earning rule IDs and their points mapping for the given earning rule.")
    rewards: Optional[Dict[str, Any]] = Field(None, description="Contains a list of reward IDs and their points mapping for the given reward.")
    points: LoyaltyTierBasePoints = Field(...)
    id: StrictStr = Field(..., description="Unique loyalty tier ID.")
    campaign_id: StrictStr = Field(..., description="Unique parent campaign ID.")
    metadata: Optional[Dict[str, Any]] = Field(None, description="The metadata object stores all custom attributes assigned to the loyalty tier. A set of key/value pairs that you can attach to a loyalty tier object. It can be useful for storing additional information about the loyalty tier in a structured format.")
    created_at: datetime = Field(..., description="Timestamp representing the date and time when the loyalty tier was created in ISO 8601 format.")
    updated_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the loyalty tier was updated in ISO 8601 format.")
    config: LoyaltyTierAllOfConfig = Field(...)
    expiration: Optional[LoyaltyTierExpiration] = None
    object: StrictStr = Field(..., description="The type of object represented by JSON. This object stores information about the loyalty.")
    __properties = ["name", "earning_rules", "rewards", "points", "id", "campaign_id", "metadata", "created_at", "updated_at", "config", "expiration", "object"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('loyalty_tier',):
            raise ValueError("must be one of enum values ('loyalty_tier')")
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
    def from_json(cls, json_str: str) -> LoyaltyTier:
        """Create an instance of LoyaltyTier from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of expiration
        if self.expiration:
            _dict['expiration'] = self.expiration.to_dict()
        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltyTier:
        """Create an instance of LoyaltyTier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltyTier.parse_obj(obj)

        _obj = LoyaltyTier.parse_obj({
            "name": obj.get("name"),
            "earning_rules": obj.get("earning_rules"),
            "rewards": obj.get("rewards"),
            "points": LoyaltyTierBasePoints.from_dict(obj.get("points")) if obj.get("points") is not None else None,
            "id": obj.get("id"),
            "campaign_id": obj.get("campaign_id"),
            "metadata": obj.get("metadata"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "config": LoyaltyTierAllOfConfig.from_dict(obj.get("config")) if obj.get("config") is not None else None,
            "expiration": LoyaltyTierExpiration.from_dict(obj.get("expiration")) if obj.get("expiration") is not None else None,
            "object": obj.get("object") if obj.get("object") is not None else 'loyalty_tier'
        })
        return _obj


