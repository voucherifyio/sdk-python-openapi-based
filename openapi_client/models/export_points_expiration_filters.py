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
from openapi_client.models.field_conditions import FieldConditions
from openapi_client.models.junction import Junction

class ExportPointsExpirationFilters(BaseModel):
    """
    ExportPointsExpirationFilters
    """
    junction: Optional[Junction] = None
    id: Optional[FieldConditions] = None
    campaign_id: Optional[FieldConditions] = None
    voucher_id: Optional[FieldConditions] = None
    points: Optional[FieldConditions] = None
    status: Optional[FieldConditions] = None
    expires_at: Optional[FieldConditions] = None
    __properties = ["junction", "id", "campaign_id", "voucher_id", "points", "status", "expires_at"]

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
    def from_json(cls, json_str: str) -> ExportPointsExpirationFilters:
        """Create an instance of ExportPointsExpirationFilters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaign_id
        if self.campaign_id:
            _dict['campaign_id'] = self.campaign_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of voucher_id
        if self.voucher_id:
            _dict['voucher_id'] = self.voucher_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of points
        if self.points:
            _dict['points'] = self.points.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of expires_at
        if self.expires_at:
            _dict['expires_at'] = self.expires_at.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExportPointsExpirationFilters:
        """Create an instance of ExportPointsExpirationFilters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExportPointsExpirationFilters.parse_obj(obj)

        _obj = ExportPointsExpirationFilters.parse_obj({
            "junction": obj.get("junction"),
            "id": FieldConditions.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "campaign_id": FieldConditions.from_dict(obj.get("campaign_id")) if obj.get("campaign_id") is not None else None,
            "voucher_id": FieldConditions.from_dict(obj.get("voucher_id")) if obj.get("voucher_id") is not None else None,
            "points": FieldConditions.from_dict(obj.get("points")) if obj.get("points") is not None else None,
            "status": FieldConditions.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "expires_at": FieldConditions.from_dict(obj.get("expires_at")) if obj.get("expires_at") is not None else None
        })
        return _obj


