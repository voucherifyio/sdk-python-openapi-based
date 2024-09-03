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
from pydantic import BaseModel
from voucherify_client.models.field_conditions import FieldConditions
from voucherify_client.models.junction import Junction

class ExportsGetResponseBodyParametersFilters(BaseModel):
    """
    ExportsGetResponseBodyParametersFilters
    """
    junction: Optional[Junction] = None
    campaign_id: Optional[FieldConditions] = None
    voucher_id: Optional[FieldConditions] = None
    created_at: Optional[FieldConditions] = None
    __properties = ["junction", "campaign_id", "voucher_id", "created_at"]

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
    def from_json(cls, json_str: str) -> ExportsGetResponseBodyParametersFilters:
        """Create an instance of ExportsGetResponseBodyParametersFilters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of campaign_id
        if self.campaign_id:
            _dict['campaign_id'] = self.campaign_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of voucher_id
        if self.voucher_id:
            _dict['voucher_id'] = self.voucher_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_at
        if self.created_at:
            _dict['created_at'] = self.created_at.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExportsGetResponseBodyParametersFilters:
        """Create an instance of ExportsGetResponseBodyParametersFilters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExportsGetResponseBodyParametersFilters.parse_obj(obj)

        _obj = ExportsGetResponseBodyParametersFilters.parse_obj({
            "junction": obj.get("junction"),
            "campaign_id": FieldConditions.from_dict(obj.get("campaign_id")) if obj.get("campaign_id") is not None else None,
            "voucher_id": FieldConditions.from_dict(obj.get("voucher_id")) if obj.get("voucher_id") is not None else None,
            "created_at": FieldConditions.from_dict(obj.get("created_at")) if obj.get("created_at") is not None else None
        })
        return _obj


