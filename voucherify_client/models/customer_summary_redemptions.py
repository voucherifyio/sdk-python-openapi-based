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
from voucherify_client.models.customer_summary_redemptions_gift import CustomerSummaryRedemptionsGift
from voucherify_client.models.customer_summary_redemptions_loyalty_card import CustomerSummaryRedemptionsLoyaltyCard

class CustomerSummaryRedemptions(BaseModel):
    """
    CustomerSummaryRedemptions
    """
    total_redeemed: Optional[StrictInt] = Field(None, description="Total number of redemptions made by the customer.")
    total_failed: Optional[StrictInt] = Field(None, description="Total number of redemptions that failed.")
    total_succeeded: Optional[StrictInt] = Field(None, description="Total number of redemptions that succeeded.")
    total_rolled_back: Optional[StrictInt] = Field(None, description="Total number of redemptions that were rolled back for the customer.")
    total_rollback_failed: Optional[StrictInt] = Field(None, description="Total number of redemption rollbacks that failed.")
    total_rollback_succeeded: Optional[StrictInt] = Field(None, description="Total number of redemption rollbacks that succeeded.")
    gift: Optional[CustomerSummaryRedemptionsGift] = None
    loyalty_card: Optional[CustomerSummaryRedemptionsLoyaltyCard] = None
    __properties = ["total_redeemed", "total_failed", "total_succeeded", "total_rolled_back", "total_rollback_failed", "total_rollback_succeeded", "gift", "loyalty_card"]

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
    def from_json(cls, json_str: str) -> CustomerSummaryRedemptions:
        """Create an instance of CustomerSummaryRedemptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of gift
        if self.gift:
            _dict['gift'] = self.gift.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loyalty_card
        if self.loyalty_card:
            _dict['loyalty_card'] = self.loyalty_card.to_dict()
        # set to None if total_redeemed (nullable) is None
        # and __fields_set__ contains the field
        if self.total_redeemed is None and "total_redeemed" in self.__fields_set__:
            _dict['total_redeemed'] = None

        # set to None if total_failed (nullable) is None
        # and __fields_set__ contains the field
        if self.total_failed is None and "total_failed" in self.__fields_set__:
            _dict['total_failed'] = None

        # set to None if total_succeeded (nullable) is None
        # and __fields_set__ contains the field
        if self.total_succeeded is None and "total_succeeded" in self.__fields_set__:
            _dict['total_succeeded'] = None

        # set to None if total_rolled_back (nullable) is None
        # and __fields_set__ contains the field
        if self.total_rolled_back is None and "total_rolled_back" in self.__fields_set__:
            _dict['total_rolled_back'] = None

        # set to None if total_rollback_failed (nullable) is None
        # and __fields_set__ contains the field
        if self.total_rollback_failed is None and "total_rollback_failed" in self.__fields_set__:
            _dict['total_rollback_failed'] = None

        # set to None if total_rollback_succeeded (nullable) is None
        # and __fields_set__ contains the field
        if self.total_rollback_succeeded is None and "total_rollback_succeeded" in self.__fields_set__:
            _dict['total_rollback_succeeded'] = None

        # set to None if gift (nullable) is None
        # and __fields_set__ contains the field
        if self.gift is None and "gift" in self.__fields_set__:
            _dict['gift'] = None

        # set to None if loyalty_card (nullable) is None
        # and __fields_set__ contains the field
        if self.loyalty_card is None and "loyalty_card" in self.__fields_set__:
            _dict['loyalty_card'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomerSummaryRedemptions:
        """Create an instance of CustomerSummaryRedemptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomerSummaryRedemptions.parse_obj(obj)

        _obj = CustomerSummaryRedemptions.parse_obj({
            "total_redeemed": obj.get("total_redeemed"),
            "total_failed": obj.get("total_failed"),
            "total_succeeded": obj.get("total_succeeded"),
            "total_rolled_back": obj.get("total_rolled_back"),
            "total_rollback_failed": obj.get("total_rollback_failed"),
            "total_rollback_succeeded": obj.get("total_rollback_succeeded"),
            "gift": CustomerSummaryRedemptionsGift.from_dict(obj.get("gift")) if obj.get("gift") is not None else None,
            "loyalty_card": CustomerSummaryRedemptionsLoyaltyCard.from_dict(obj.get("loyalty_card")) if obj.get("loyalty_card") is not None else None
        })
        return _obj


