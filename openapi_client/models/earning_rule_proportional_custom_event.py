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



from pydantic import BaseModel, Field, StrictStr, validator
from openapi_client.models.earning_rule_proportional_custom_event_custom_event import EarningRuleProportionalCustomEventCustomEvent

class EarningRuleProportionalCustomEvent(BaseModel):
    """
    EarningRuleProportionalCustomEvent
    """
    type: StrictStr = Field(..., description="Defines how the points will be added to the loyalty card.PROPORTIONAL adds points based on a pre-defined ratio.")
    calculation_type: StrictStr = Field(..., description="CUSTOM_EVENT_METADATA: Custom event metadata (X points for every Y in metadata attribute).")
    custom_event: EarningRuleProportionalCustomEventCustomEvent = Field(...)
    __properties = ["type", "calculation_type", "custom_event"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('PROPORTIONAL',):
            raise ValueError("must be one of enum values ('PROPORTIONAL')")
        return value

    @validator('calculation_type')
    def calculation_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('CUSTOM_EVENT_METADATA',):
            raise ValueError("must be one of enum values ('CUSTOM_EVENT_METADATA')")
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
    def from_json(cls, json_str: str) -> EarningRuleProportionalCustomEvent:
        """Create an instance of EarningRuleProportionalCustomEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of custom_event
        if self.custom_event:
            _dict['custom_event'] = self.custom_event.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EarningRuleProportionalCustomEvent:
        """Create an instance of EarningRuleProportionalCustomEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EarningRuleProportionalCustomEvent.parse_obj(obj)

        _obj = EarningRuleProportionalCustomEvent.parse_obj({
            "type": obj.get("type") if obj.get("type") is not None else 'PROPORTIONAL',
            "calculation_type": obj.get("calculation_type") if obj.get("calculation_type") is not None else 'CUSTOM_EVENT_METADATA',
            "custom_event": EarningRuleProportionalCustomEventCustomEvent.from_dict(obj.get("custom_event")) if obj.get("custom_event") is not None else None
        })
        return _obj

