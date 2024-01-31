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
from pydantic import BaseModel, Field, StrictBool, conlist, constr, validator
from voucherify_client.models.loyalty_card_transaction import LoyaltyCardTransaction

class LoyaltiesMembersTransactionsListResponseBody(BaseModel):
    """
    Response body schema for **GET** `/loyalties/{campaignId}/members/{memberId}/transactions` and `/loyalties/members/{memberId}/transactions`.  # noqa: E501
    """
    object: constr(strict=True) = Field(..., description="The type of object represented by JSON.")
    data_ref: constr(strict=True) = Field(..., description="Identifies the name of the attribute that contains the array of transaction objects.")
    data: conlist(LoyaltyCardTransaction) = Field(..., description="A dictionary that contains an array of transactions. Each entry in the array is a separate transaction object.")
    has_more: StrictBool = Field(..., description="As query results are always limited (by the limit parameter), the has_more flag indicates whether there are more records for given filter parameters. This let's you know if you are able to run another request (with a different page or a different start date filter) to get more records returned in the results.")
    __properties = ["object", "data_ref", "data", "has_more"]

    @validator('object')
    def object_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"list", value):
            raise ValueError(r"must validate the regular expression /list/")
        return value

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('list',):
            raise ValueError("must be one of enum values ('list')")
        return value

    @validator('data_ref')
    def data_ref_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"data", value):
            raise ValueError(r"must validate the regular expression /data/")
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
    def from_json(cls, json_str: str) -> LoyaltiesMembersTransactionsListResponseBody:
        """Create an instance of LoyaltiesMembersTransactionsListResponseBody from a JSON string"""
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
    def from_dict(cls, obj: dict) -> LoyaltiesMembersTransactionsListResponseBody:
        """Create an instance of LoyaltiesMembersTransactionsListResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesMembersTransactionsListResponseBody.parse_obj(obj)

        _obj = LoyaltiesMembersTransactionsListResponseBody.parse_obj({
            "object": obj.get("object") if obj.get("object") is not None else 'list',
            "data_ref": obj.get("data_ref") if obj.get("data_ref") is not None else 'data',
            "data": [LoyaltyCardTransaction.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None,
            "has_more": obj.get("has_more")
        })
        return _obj


