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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint, conlist, validator
from voucherify_client.models.earning_rule_base_custom_event import EarningRuleBaseCustomEvent
from voucherify_client.models.earning_rule_base_loyalty import EarningRuleBaseLoyalty
from voucherify_client.models.earning_rule_base_segment import EarningRuleBaseSegment
from voucherify_client.models.earning_rule_base_source import EarningRuleBaseSource
from voucherify_client.models.earning_rule_base_validity_timeframe import EarningRuleBaseValidityTimeframe
from voucherify_client.models.earning_rule_event import EarningRuleEvent

class LoyaltiesEarningRulesDisableResponseBody(BaseModel):
    """
    Response body schema for **POST** `/loyalties/{campaignId}/earning-rules/{earningRuleId}/disable`  # noqa: E501
    """
    id: StrictStr = Field(..., description="Assigned by the Voucherify API, identifies the earning rule object.")
    created_at: datetime = Field(..., description="Timestamp representing the date and time when the earning rule was created in ISO 8601 format.")
    loyalty: EarningRuleBaseLoyalty = Field(...)
    event: Optional[EarningRuleEvent] = None
    custom_event: Optional[EarningRuleBaseCustomEvent] = None
    segment: Optional[EarningRuleBaseSegment] = None
    source: EarningRuleBaseSource = Field(...)
    object: StrictStr = Field(..., description="The type of object represented by JSON. Default is earning_rule.")
    automation_id: StrictStr = Field(..., description="For internal use by Voucherify.")
    start_date: Optional[StrictStr] = Field(None, description="Start date defines when the earning rule starts to be active. Activation timestamp in ISO 8601 format. Earning rule is inactive before this date. If you don't define the start date for an earning rule, it'll inherit the campaign start date by default.")
    expiration_date: Optional[StrictStr] = Field(None, description="Expiration date defines when the earning rule expires. Expiration timestamp in ISO 8601 format. Earning rule is inactive after this date.If you don't define the expiration date for an earning rule, it'll inherit the campaign expiration date by default.")
    validity_timeframe: Optional[EarningRuleBaseValidityTimeframe] = None
    validity_day_of_week: Optional[conlist(conint(strict=True, le=6, ge=0))] = Field(None, description="Integer array corresponding to the particular days of the week in which the earning rule is valid.  - `0` Sunday - `1` Monday - `2` Tuesday - `3` Wednesday - `4` Thursday - `5` Friday - `6` Saturday")
    metadata: Dict[str, Any] = Field(..., description="The metadata object stores all custom attributes assigned to the earning rule. A set of key/value pairs that you can attach to an earning rule object. It can be useful for storing additional information about the earning rule in a structured format.")
    updated_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the earning rule was last updated in ISO 8601 format.")
    active: StrictBool = Field(..., description="A flag to toggle the earning rule on or off. You can disable an earning rule even though it's within the active period defined by the start_date and expiration_date of the campaign or the earning rule's own start_date and expiration_date.")
    __properties = ["id", "created_at", "loyalty", "event", "custom_event", "segment", "source", "object", "automation_id", "start_date", "expiration_date", "validity_timeframe", "validity_day_of_week", "metadata", "updated_at", "active"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('earning_rule',):
            raise ValueError("must be one of enum values ('earning_rule')")
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
    def from_json(cls, json_str: str) -> LoyaltiesEarningRulesDisableResponseBody:
        """Create an instance of LoyaltiesEarningRulesDisableResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of loyalty
        if self.loyalty:
            _dict['loyalty'] = self.loyalty.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_event
        if self.custom_event:
            _dict['custom_event'] = self.custom_event.to_dict()
        # override the default output from pydantic by calling `to_dict()` of segment
        if self.segment:
            _dict['segment'] = self.segment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of validity_timeframe
        if self.validity_timeframe:
            _dict['validity_timeframe'] = self.validity_timeframe.to_dict()
        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltiesEarningRulesDisableResponseBody:
        """Create an instance of LoyaltiesEarningRulesDisableResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesEarningRulesDisableResponseBody.parse_obj(obj)

        _obj = LoyaltiesEarningRulesDisableResponseBody.parse_obj({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "loyalty": EarningRuleBaseLoyalty.from_dict(obj.get("loyalty")) if obj.get("loyalty") is not None else None,
            "event": obj.get("event"),
            "custom_event": EarningRuleBaseCustomEvent.from_dict(obj.get("custom_event")) if obj.get("custom_event") is not None else None,
            "segment": EarningRuleBaseSegment.from_dict(obj.get("segment")) if obj.get("segment") is not None else None,
            "source": EarningRuleBaseSource.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "object": obj.get("object") if obj.get("object") is not None else 'earning_rule',
            "automation_id": obj.get("automation_id"),
            "start_date": obj.get("start_date"),
            "expiration_date": obj.get("expiration_date"),
            "validity_timeframe": EarningRuleBaseValidityTimeframe.from_dict(obj.get("validity_timeframe")) if obj.get("validity_timeframe") is not None else None,
            "validity_day_of_week": obj.get("validity_day_of_week"),
            "metadata": obj.get("metadata"),
            "updated_at": obj.get("updated_at"),
            "active": obj.get("active") if obj.get("active") is not None else False
        })
        return _obj


