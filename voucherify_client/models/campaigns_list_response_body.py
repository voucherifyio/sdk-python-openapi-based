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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from voucherify_client.models.campaign_base import CampaignBase

class CampaignsListResponseBody(BaseModel):
    """
    Schema model for **GET** `/campaigns`.  # noqa: E501
    """
    object: Optional[StrictStr] = Field('list', description="The type of object represented by JSON. This object stores information about campaigns in a dictionary.")
    data_ref: Optional[StrictStr] = Field('campaigns', description="Identifies the name of the attribute that contains the array of campaign objects.")
    campaigns: Optional[conlist(CampaignBase)] = Field(None, description="Contains array of campaign objects.")
    total: Optional[StrictInt] = Field(None, description="Total number of campaigns.")
    __properties = ["object", "data_ref", "campaigns", "total"]

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
    def from_json(cls, json_str: str) -> CampaignsListResponseBody:
        """Create an instance of CampaignsListResponseBody from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CampaignsListResponseBody:
        """Create an instance of CampaignsListResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CampaignsListResponseBody.parse_obj(obj)

        _obj = CampaignsListResponseBody.parse_obj({
            "object": obj.get("object") if obj.get("object") is not None else 'list',
            "data_ref": obj.get("data_ref") if obj.get("data_ref") is not None else 'campaigns',
            "campaigns": [CampaignBase.from_dict(_item) for _item in obj.get("campaigns")] if obj.get("campaigns") is not None else None,
            "total": obj.get("total")
        })
        return _obj

