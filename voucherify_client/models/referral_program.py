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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from voucherify_client.models.referral_program_custom_event import ReferralProgramCustomEvent
from voucherify_client.models.referral_program_referee_reward import ReferralProgramRefereeReward

class ReferralProgram(BaseModel):
    """
    Defines the referee reward and the way a referral is triggered. Context: `REFERRAL_PROGRAM`.  # noqa: E501
    """
    conversion_event_type: Optional[StrictStr] = Field(None, description="Define how a referral is triggered.")
    custom_event: Optional[ReferralProgramCustomEvent] = None
    referee_reward: Optional[ReferralProgramRefereeReward] = None
    __properties = ["conversion_event_type", "custom_event", "referee_reward"]

    @validator('conversion_event_type')
    def conversion_event_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('redemption', 'custom_event',):
            raise ValueError("must be one of enum values ('redemption', 'custom_event')")
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
    def from_json(cls, json_str: str) -> ReferralProgram:
        """Create an instance of ReferralProgram from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of referee_reward
        if self.referee_reward:
            _dict['referee_reward'] = self.referee_reward.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReferralProgram:
        """Create an instance of ReferralProgram from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReferralProgram.parse_obj(obj)

        _obj = ReferralProgram.parse_obj({
            "conversion_event_type": obj.get("conversion_event_type"),
            "custom_event": ReferralProgramCustomEvent.from_dict(obj.get("custom_event")) if obj.get("custom_event") is not None else None,
            "referee_reward": ReferralProgramRefereeReward.from_dict(obj.get("referee_reward")) if obj.get("referee_reward") is not None else None
        })
        return _obj


