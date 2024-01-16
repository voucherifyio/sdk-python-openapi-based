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
from openapi_client.models.campaign_loyalty_card_expiration_rules import CampaignLoyaltyCardExpirationRules

class CampaignLoyaltyCard(BaseModel):
    """
    Schema model for a campaign loyalty card.  # noqa: E501
    """
    points: StrictInt = Field(..., description="The initial number of points to assign to the loyalty card. This is the current loyalty card score i.e. the number of loyalty points on the card.")
    expiration_rules: Optional[CampaignLoyaltyCardExpirationRules] = None
    __properties = ["points", "expiration_rules"]

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
    def from_json(cls, json_str: str) -> CampaignLoyaltyCard:
        """Create an instance of CampaignLoyaltyCard from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of expiration_rules
        if self.expiration_rules:
            _dict['expiration_rules'] = self.expiration_rules.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CampaignLoyaltyCard:
        """Create an instance of CampaignLoyaltyCard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CampaignLoyaltyCard.parse_obj(obj)

        _obj = CampaignLoyaltyCard.parse_obj({
            "points": obj.get("points"),
            "expiration_rules": CampaignLoyaltyCardExpirationRules.from_dict(obj.get("expiration_rules")) if obj.get("expiration_rules") is not None else None
        })
        return _obj

