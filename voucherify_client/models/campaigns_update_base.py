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
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from voucherify_client.models.campaign_base_validity_timeframe import CampaignBaseValidityTimeframe

class CampaignsUpdateBase(BaseModel):
    """
    Base body schema for creating a campaign using **PUT** `/campaigns`.  # noqa: E501
    """
    start_date: Optional[datetime] = Field(None, description="Activation timestamp defines when the campaign starts to be active in ISO 8601 format. Campaign is *inactive before* this date. ")
    expiration_date: Optional[datetime] = Field(None, description="Expiration timestamp defines when the campaign expires in ISO 8601 format.  Campaign is *inactive after* this date.")
    validity_timeframe: Optional[CampaignBaseValidityTimeframe] = None
    validity_day_of_week: Optional[conlist(StrictInt)] = Field(None, description="Integer array corresponding to the particular days of the week in which the campaign is valid.  - `0`  Sunday   - `1`  Monday   - `2`  Tuesday   - `3`  Wednesday   - `4`  Thursday   - `5`  Friday   - `6`  Saturday  ")
    description: Optional[StrictStr] = Field(None, description="An optional field to keep any extra textual information about the campaign such as a campaign description and details.")
    category: Optional[StrictStr] = Field(None, description="The category assigned to the campaign. Either pass this parameter OR the `category_id`.")
    metadata: Optional[Dict[str, Any]] = Field(None, description="The metadata object stores all custom attributes assigned to the campaign. A set of key/value pairs that you can attach to a campaign object. It can be useful for storing additional information about the campaign in a structured format.")
    unset_metadata_fields: Optional[conlist(StrictStr)] = Field(None, description="Determine which metadata should be removed from campaign.")
    category_id: Optional[StrictStr] = Field(None, description="Unique category ID that this campaign belongs to. Either pass this parameter OR the `category`.")
    __properties = ["start_date", "expiration_date", "validity_timeframe", "validity_day_of_week", "description", "category", "metadata", "unset_metadata_fields", "category_id"]

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
    def from_json(cls, json_str: str) -> CampaignsUpdateBase:
        """Create an instance of CampaignsUpdateBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of validity_timeframe
        if self.validity_timeframe:
            _dict['validity_timeframe'] = self.validity_timeframe.to_dict()
        # set to None if unset_metadata_fields (nullable) is None
        # and __fields_set__ contains the field
        if self.unset_metadata_fields is None and "unset_metadata_fields" in self.__fields_set__:
            _dict['unset_metadata_fields'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CampaignsUpdateBase:
        """Create an instance of CampaignsUpdateBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CampaignsUpdateBase.parse_obj(obj)

        _obj = CampaignsUpdateBase.parse_obj({
            "start_date": obj.get("start_date"),
            "expiration_date": obj.get("expiration_date"),
            "validity_timeframe": CampaignBaseValidityTimeframe.from_dict(obj.get("validity_timeframe")) if obj.get("validity_timeframe") is not None else None,
            "validity_day_of_week": obj.get("validity_day_of_week"),
            "description": obj.get("description"),
            "category": obj.get("category"),
            "metadata": obj.get("metadata"),
            "unset_metadata_fields": obj.get("unset_metadata_fields"),
            "category_id": obj.get("category_id")
        })
        return _obj


