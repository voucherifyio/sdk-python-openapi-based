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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, conlist
from voucherify_client.models.customer_referrals_campaigns_item import CustomerReferralsCampaignsItem

class CustomerReferrals(BaseModel):
    """
    Summary of customer's referrals, in this case, the customer being the referee, i.e. information about the source of referrals and number of times the customer was referred by other customers.  # noqa: E501
    """
    total: Optional[StrictInt] = Field(None, description="Total number of times this customer received a referral, i.e. was referred by another customer.")
    campaigns: Optional[conlist(CustomerReferralsCampaignsItem)] = Field(None, description="Contains an array of campaigns that served as the source of a referral for the customer.")
    __properties = ["total", "campaigns"]

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
    def from_json(cls, json_str: str) -> CustomerReferrals:
        """Create an instance of CustomerReferrals from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in campaigns (list)
        _items = []
        if self.campaigns:
            for _item in self.campaigns:
                if _item:
                    _items.append(_item.to_dict())
            _dict['campaigns'] = _items
        # set to None if total (nullable) is None
        # and __fields_set__ contains the field
        if self.total is None and "total" in self.__fields_set__:
            _dict['total'] = None

        # set to None if campaigns (nullable) is None
        # and __fields_set__ contains the field
        if self.campaigns is None and "campaigns" in self.__fields_set__:
            _dict['campaigns'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomerReferrals:
        """Create an instance of CustomerReferrals from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomerReferrals.parse_obj(obj)

        _obj = CustomerReferrals.parse_obj({
            "total": obj.get("total"),
            "campaigns": [CustomerReferralsCampaignsItem.from_dict(_item) for _item in obj.get("campaigns")] if obj.get("campaigns") is not None else None
        })
        return _obj


