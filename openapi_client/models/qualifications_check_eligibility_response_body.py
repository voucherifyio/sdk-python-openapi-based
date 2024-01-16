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
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.order_calculated import OrderCalculated
from openapi_client.models.qualifications_redeemables import QualificationsRedeemables
from openapi_client.models.qualifications_stacking_rules import QualificationsStackingRules

class QualificationsCheckEligibilityResponseBody(BaseModel):
    """
    Response body schema for **POST** `/qualifications`.  # noqa: E501
    """
    redeemables: Optional[QualificationsRedeemables] = None
    tracking_id: Optional[StrictStr] = Field(None, description="This identifier is generated during voucher qualification based on your internal id (e.g., email, database ID). This is a hashed customer source ID.")
    order: Optional[OrderCalculated] = None
    stacking_rules: Optional[QualificationsStackingRules] = None
    __properties = ["redeemables", "tracking_id", "order", "stacking_rules"]

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
    def from_json(cls, json_str: str) -> QualificationsCheckEligibilityResponseBody:
        """Create an instance of QualificationsCheckEligibilityResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of redeemables
        if self.redeemables:
            _dict['redeemables'] = self.redeemables.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stacking_rules
        if self.stacking_rules:
            _dict['stacking_rules'] = self.stacking_rules.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QualificationsCheckEligibilityResponseBody:
        """Create an instance of QualificationsCheckEligibilityResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return QualificationsCheckEligibilityResponseBody.parse_obj(obj)

        _obj = QualificationsCheckEligibilityResponseBody.parse_obj({
            "redeemables": QualificationsRedeemables.from_dict(obj.get("redeemables")) if obj.get("redeemables") is not None else None,
            "tracking_id": obj.get("tracking_id"),
            "order": OrderCalculated.from_dict(obj.get("order")) if obj.get("order") is not None else None,
            "stacking_rules": QualificationsStackingRules.from_dict(obj.get("stacking_rules")) if obj.get("stacking_rules") is not None else None
        })
        return _obj


