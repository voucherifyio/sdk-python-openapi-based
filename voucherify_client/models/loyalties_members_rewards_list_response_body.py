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


from typing import List
from pydantic import BaseModel, Field, StrictStr, conint, conlist, validator
from voucherify_client.models.loyalties_members_rewards_list_response_body_data_item import LoyaltiesMembersRewardsListResponseBodyDataItem

class LoyaltiesMembersRewardsListResponseBody(BaseModel):
    """
    Response body schema for **GET** `/loyalties/members/{memberId}/rewards`  # noqa: E501
    """
    object: StrictStr = Field(..., description="The type of object represented by JSON.")
    data_ref: StrictStr = Field(..., description="Identifies the name of the attribute that contains the array of loyalty reward objects.")
    data: conlist(LoyaltiesMembersRewardsListResponseBodyDataItem) = Field(..., description="Contains array of loyalty reward objects.")
    total: conint(strict=True, ge=0) = Field(..., description="Total number of loyalty reward objects.")
    __properties = ["object", "data_ref", "data", "total"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('list',):
            raise ValueError("must be one of enum values ('list')")
        return value

    @validator('data_ref')
    def data_ref_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('data',):
            raise ValueError("must be one of enum values ('data')")
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
    def from_json(cls, json_str: str) -> LoyaltiesMembersRewardsListResponseBody:
        """Create an instance of LoyaltiesMembersRewardsListResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltiesMembersRewardsListResponseBody:
        """Create an instance of LoyaltiesMembersRewardsListResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesMembersRewardsListResponseBody.parse_obj(obj)

        _obj = LoyaltiesMembersRewardsListResponseBody.parse_obj({
            "object": obj.get("object") if obj.get("object") is not None else 'list',
            "data_ref": obj.get("data_ref") if obj.get("data_ref") is not None else 'data',
            "data": [LoyaltiesMembersRewardsListResponseBodyDataItem.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None,
            "total": obj.get("total")
        })
        return _obj


