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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from voucherify_client.models.validations_redeemable_applicable import ValidationsRedeemableApplicable
from voucherify_client.models.validations_redeemable_inapplicable import ValidationsRedeemableInapplicable
from voucherify_client.models.validations_redeemable_skipped import ValidationsRedeemableSkipped

class ValidationEntity(BaseModel):
    """
    ValidationEntity
    """
    id: Optional[StrictStr] = Field(None, description="Unique validation id.")
    session_id: Optional[StrictStr] = Field(None, description="Unique session id.")
    status: Optional[StrictStr] = Field(None, description="The validation status")
    created_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the validation was created in ISO 8601 format.")
    customer_id: Optional[StrictStr] = Field(None, description="Unique customer ID of the customer making the purchase.")
    redeemables: Optional[conlist(ValidationsRedeemableApplicable)] = Field(None, description="Lists validation results of each redeemable.")
    skipped_redeemables: Optional[conlist(ValidationsRedeemableInapplicable)] = Field(None, description="Lists validation results of each redeemable.")
    inapplicable_redeemables: Optional[conlist(ValidationsRedeemableSkipped)] = Field(None, description="Lists validation results of each redeemable.")
    __properties = ["id", "session_id", "status", "created_at", "customer_id", "redeemables", "skipped_redeemables", "inapplicable_redeemables"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('VALID', 'INVALID',):
            raise ValueError("must be one of enum values ('VALID', 'INVALID')")
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
    def from_json(cls, json_str: str) -> ValidationEntity:
        """Create an instance of ValidationEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in redeemables (list)
        _items = []
        if self.redeemables:
            for _item in self.redeemables:
                if _item:
                    _items.append(_item.to_dict())
            _dict['redeemables'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in skipped_redeemables (list)
        _items = []
        if self.skipped_redeemables:
            for _item in self.skipped_redeemables:
                if _item:
                    _items.append(_item.to_dict())
            _dict['skipped_redeemables'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in inapplicable_redeemables (list)
        _items = []
        if self.inapplicable_redeemables:
            for _item in self.inapplicable_redeemables:
                if _item:
                    _items.append(_item.to_dict())
            _dict['inapplicable_redeemables'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ValidationEntity:
        """Create an instance of ValidationEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ValidationEntity.parse_obj(obj)

        _obj = ValidationEntity.parse_obj({
            "id": obj.get("id"),
            "session_id": obj.get("session_id"),
            "status": obj.get("status"),
            "created_at": obj.get("created_at"),
            "customer_id": obj.get("customer_id"),
            "redeemables": [ValidationsRedeemableApplicable.from_dict(_item) for _item in obj.get("redeemables")] if obj.get("redeemables") is not None else None,
            "skipped_redeemables": [ValidationsRedeemableInapplicable.from_dict(_item) for _item in obj.get("skipped_redeemables")] if obj.get("skipped_redeemables") is not None else None,
            "inapplicable_redeemables": [ValidationsRedeemableSkipped.from_dict(_item) for _item in obj.get("inapplicable_redeemables")] if obj.get("inapplicable_redeemables") is not None else None
        })
        return _obj


