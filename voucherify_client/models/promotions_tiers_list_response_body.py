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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from voucherify_client.models.promotion_tier import PromotionTier

class PromotionsTiersListResponseBody(BaseModel):
    """
    Response body schema for **GET** `v1/promotions/{campaignId}/tiers` and **GET** `v1/promotions/tiers`.  # noqa: E501
    """
    object: Optional[StrictStr] = Field('list', description="The type of the object represented by JSON. This object stores information about promotion tiers in a dictionary.")
    data_ref: Optional[StrictStr] = Field('tiers', description="Identifies the name of the attribute that contains the array of promotion tier objects.")
    tiers: Optional[conlist(PromotionTier)] = Field(None, description="Contains array of promotion tier objects.")
    total: Optional[StrictInt] = Field(None, description="Total number of promotion tiers.")
    has_more: Optional[StrictBool] = Field(None, description="As query results are always limited (by the limit parameter), the `has_more` flag indicates if there are more records for given filter parameters. This lets you know if you can run another request (with a different page or a different start date filter) to get more records returned in the results.")
    __properties = ["object", "data_ref", "tiers", "total", "has_more"]

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
    def from_json(cls, json_str: str) -> PromotionsTiersListResponseBody:
        """Create an instance of PromotionsTiersListResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in tiers (list)
        _items = []
        if self.tiers:
            for _item in self.tiers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tiers'] = _items
        # set to None if object (nullable) is None
        # and __fields_set__ contains the field
        if self.object is None and "object" in self.__fields_set__:
            _dict['object'] = None

        # set to None if data_ref (nullable) is None
        # and __fields_set__ contains the field
        if self.data_ref is None and "data_ref" in self.__fields_set__:
            _dict['data_ref'] = None

        # set to None if tiers (nullable) is None
        # and __fields_set__ contains the field
        if self.tiers is None and "tiers" in self.__fields_set__:
            _dict['tiers'] = None

        # set to None if total (nullable) is None
        # and __fields_set__ contains the field
        if self.total is None and "total" in self.__fields_set__:
            _dict['total'] = None

        # set to None if has_more (nullable) is None
        # and __fields_set__ contains the field
        if self.has_more is None and "has_more" in self.__fields_set__:
            _dict['has_more'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PromotionsTiersListResponseBody:
        """Create an instance of PromotionsTiersListResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PromotionsTiersListResponseBody.parse_obj(obj)

        _obj = PromotionsTiersListResponseBody.parse_obj({
            "object": obj.get("object") if obj.get("object") is not None else 'list',
            "data_ref": obj.get("data_ref") if obj.get("data_ref") is not None else 'tiers',
            "tiers": [PromotionTier.from_dict(_item) for _item in obj.get("tiers")] if obj.get("tiers") is not None else None,
            "total": obj.get("total"),
            "has_more": obj.get("has_more")
        })
        return _obj


