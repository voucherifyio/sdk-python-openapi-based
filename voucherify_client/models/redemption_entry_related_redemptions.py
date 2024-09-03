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
from pydantic import BaseModel, conlist
from voucherify_client.models.redemption_entry_related_redemptions_redemptions_item import RedemptionEntryRelatedRedemptionsRedemptionsItem
from voucherify_client.models.redemption_entry_related_redemptions_rollbacks_item import RedemptionEntryRelatedRedemptionsRollbacksItem

class RedemptionEntryRelatedRedemptions(BaseModel):
    """
    RedemptionEntryRelatedRedemptions
    """
    rollbacks: Optional[conlist(RedemptionEntryRelatedRedemptionsRollbacksItem)] = None
    redemptions: Optional[conlist(RedemptionEntryRelatedRedemptionsRedemptionsItem)] = None
    __properties = ["rollbacks", "redemptions"]

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
    def from_json(cls, json_str: str) -> RedemptionEntryRelatedRedemptions:
        """Create an instance of RedemptionEntryRelatedRedemptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in rollbacks (list)
        _items = []
        if self.rollbacks:
            for _item in self.rollbacks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rollbacks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in redemptions (list)
        _items = []
        if self.redemptions:
            for _item in self.redemptions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['redemptions'] = _items
        # set to None if rollbacks (nullable) is None
        # and __fields_set__ contains the field
        if self.rollbacks is None and "rollbacks" in self.__fields_set__:
            _dict['rollbacks'] = None

        # set to None if redemptions (nullable) is None
        # and __fields_set__ contains the field
        if self.redemptions is None and "redemptions" in self.__fields_set__:
            _dict['redemptions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RedemptionEntryRelatedRedemptions:
        """Create an instance of RedemptionEntryRelatedRedemptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RedemptionEntryRelatedRedemptions.parse_obj(obj)

        _obj = RedemptionEntryRelatedRedemptions.parse_obj({
            "rollbacks": [RedemptionEntryRelatedRedemptionsRollbacksItem.from_dict(_item) for _item in obj.get("rollbacks")] if obj.get("rollbacks") is not None else None,
            "redemptions": [RedemptionEntryRelatedRedemptionsRedemptionsItem.from_dict(_item) for _item in obj.get("redemptions")] if obj.get("redemptions") is not None else None
        })
        return _obj

