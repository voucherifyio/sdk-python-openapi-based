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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator
from openapi_client.models.campaign_base_validity_timeframe import CampaignBaseValidityTimeframe

class CampaignsCreateBase(BaseModel):
    """
    Base body schema for creating a campaign using **POST** `/campaigns`.  # noqa: E501
    """
    name: Optional[StrictStr] = Field(None, description="Campaign name.")
    description: Optional[StrictStr] = Field(None, description="An optional field to keep any extra textual information about the campaign such as a campaign description and details.")
    type: Optional[StrictStr] = Field(None, description="Defines whether the campaign can be updated with new vouchers after campaign creation.      - `AUTO_UPDATE`: By choosing the auto update option you will create a campaign that can be enhanced by new vouchers after the time of creation (e.g. by publish vouchers method).     -  `STATIC`: vouchers need to be manually published.")
    join_once: Optional[StrictBool] = Field(None, description="If this value is set to `true`, customers will be able to join the campaign only once.")
    auto_join: Optional[StrictBool] = Field(None, description="Indicates whether customers will be able to auto-join a loyalty campaign if any earning rule is fulfilled.")
    use_voucher_metadata_schema: Optional[StrictBool] = Field(None, description="Flag indicating whether the campaign is to use the voucher's metadata schema instead of the campaign metadata schema.")
    vouchers_count: Optional[StrictInt] = Field(None, description="Total number of unique vouchers in campaign (size of campaign).")
    start_date: Optional[datetime] = Field(None, description="Activation timestamp defines when the campaign starts to be active in ISO 8601 format. Campaign is *inactive before* this date. ")
    expiration_date: Optional[datetime] = Field(None, description="Expiration timestamp defines when the campaign expires in ISO 8601 format.  Campaign is *inactive after* this date.")
    validity_timeframe: Optional[CampaignBaseValidityTimeframe] = None
    validity_day_of_week: Optional[conlist(StrictInt)] = Field(None, description="Integer array corresponding to the particular days of the week in which the campaign is valid.  - `0`  Sunday   - `1`  Monday   - `2`  Tuesday   - `3`  Wednesday   - `4`  Thursday   - `5`  Friday   - `6`  Saturday  ")
    activity_duration_after_publishing: Optional[StrictStr] = Field(None, description="Defines the amount of time the campaign will be active in ISO 8601 format after publishing. For example, a campaign with a `duration` of `P24D` will be valid for a duration of 24 days.")
    validation_rules: Optional[conlist(StrictStr, max_items=1)] = Field(None, description="Array containing the ID of the validation rule associated with the promotion tier.")
    category_id: Optional[StrictStr] = Field(None, description="Unique category ID that this campaign belongs to. Either pass this parameter OR the `category`.")
    category: Optional[StrictStr] = Field(None, description="The category assigned to the campaign. Either pass this parameter OR the `category_id`.")
    metadata: Optional[Dict[str, Any]] = Field(None, description="The metadata object stores all custom attributes assigned to the campaign. A set of key/value pairs that you can attach to a campaign object. It can be useful for storing additional information about the campaign in a structured format.")
    __properties = ["name", "description", "type", "join_once", "auto_join", "use_voucher_metadata_schema", "vouchers_count", "start_date", "expiration_date", "validity_timeframe", "validity_day_of_week", "activity_duration_after_publishing", "validation_rules", "category_id", "category", "metadata"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('AUTO_UPDATE', 'STATIC',):
            raise ValueError("must be one of enum values ('AUTO_UPDATE', 'STATIC')")
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
    def from_json(cls, json_str: str) -> CampaignsCreateBase:
        """Create an instance of CampaignsCreateBase from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CampaignsCreateBase:
        """Create an instance of CampaignsCreateBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CampaignsCreateBase.parse_obj(obj)

        _obj = CampaignsCreateBase.parse_obj({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "type": obj.get("type"),
            "join_once": obj.get("join_once"),
            "auto_join": obj.get("auto_join"),
            "use_voucher_metadata_schema": obj.get("use_voucher_metadata_schema"),
            "vouchers_count": obj.get("vouchers_count"),
            "start_date": obj.get("start_date"),
            "expiration_date": obj.get("expiration_date"),
            "validity_timeframe": CampaignBaseValidityTimeframe.from_dict(obj.get("validity_timeframe")) if obj.get("validity_timeframe") is not None else None,
            "validity_day_of_week": obj.get("validity_day_of_week"),
            "activity_duration_after_publishing": obj.get("activity_duration_after_publishing"),
            "validation_rules": obj.get("validation_rules"),
            "category_id": obj.get("category_id"),
            "category": obj.get("category"),
            "metadata": obj.get("metadata")
        })
        return _obj


