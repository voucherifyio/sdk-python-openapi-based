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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, validator
from openapi_client.models.order_calculated import OrderCalculated
from openapi_client.models.session import Session
from openapi_client.models.validations_validate_all_response_body_redeemables_item import ValidationsValidateAllResponseBodyRedeemablesItem

class ValidationsValidateAllResponseBody(BaseModel):
    """
    Response body schema for POST `/validations` where all promotion must be valid  # noqa: E501
    """
    valid: StrictBool = Field(..., description="The result of the validation. It takes all of the redeemables into account and returns a `false` if at least one redeemable is inapplicable. Returns `true` if all redeemables are applicable.")
    redeemables: conlist(ValidationsValidateAllResponseBodyRedeemablesItem) = Field(..., description="Lists validation results of each redeemable. If a redeemable can be applied, the API returns `\"status\": \"APPLICABLE\"`.")
    order: Optional[OrderCalculated] = None
    tracking_id: Optional[StrictStr] = Field(None, description="Hashed customer source ID.")
    session: Optional[Session] = None
    application_mode: StrictStr = Field(...)
    __properties = ["valid", "redeemables", "order", "tracking_id", "session", "application_mode"]

    @validator('application_mode')
    def application_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ALL',):
            raise ValueError("must be one of enum values ('ALL')")
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
    def from_json(cls, json_str: str) -> ValidationsValidateAllResponseBody:
        """Create an instance of ValidationsValidateAllResponseBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of session
        if self.session:
            _dict['session'] = self.session.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ValidationsValidateAllResponseBody:
        """Create an instance of ValidationsValidateAllResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ValidationsValidateAllResponseBody.parse_obj(obj)

        _obj = ValidationsValidateAllResponseBody.parse_obj({
            "valid": obj.get("valid"),
            "redeemables": [ValidationsValidateAllResponseBodyRedeemablesItem.from_dict(_item) for _item in obj.get("redeemables")] if obj.get("redeemables") is not None else None,
            "order": OrderCalculated.from_dict(obj.get("order")) if obj.get("order") is not None else None,
            "tracking_id": obj.get("tracking_id"),
            "session": Session.from_dict(obj.get("session")) if obj.get("session") is not None else None,
            "application_mode": obj.get("application_mode") if obj.get("application_mode") is not None else 'ALL'
        })
        return _obj


