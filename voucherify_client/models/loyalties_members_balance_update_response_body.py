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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conint, constr, validator
from voucherify_client.models.loyalties_members_balance_update_response_body_related_object import LoyaltiesMembersBalanceUpdateResponseBodyRelatedObject

class LoyaltiesMembersBalanceUpdateResponseBody(BaseModel):
    """
    Response schema for **POST** `v1/loyalties/members/{memberId}/balance` and for **POST** `v1/loyalties/{campaignId}/members/{memberId}/balance`.  # noqa: E501
    """
    points: Optional[StrictInt] = Field(None, description="The incremental points removed or added to the current balance on the loyalty card.")
    total: Optional[StrictInt] = Field(None, description="The total of points accrued over the lifetime of the loyalty card.")
    balance: Optional[conint(strict=True, ge=0)] = Field(None, description="The balance after adding/removing points.")
    type: Optional[StrictStr] = Field(None, description="The type of voucher being modified.")
    object: Optional[constr(strict=True)] = Field('balance', description="The type of the object represented by JSON. Default is balance.")
    related_object: Optional[LoyaltiesMembersBalanceUpdateResponseBodyRelatedObject] = None
    operation_type: Optional[StrictStr] = None
    __properties = ["points", "total", "balance", "type", "object", "related_object", "operation_type"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('loyalty_card', 'gift_voucher',):
            raise ValueError("must be one of enum values ('loyalty_card', 'gift_voucher')")
        return value

    @validator('object')
    def object_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"balance", value):
            raise ValueError(r"must validate the regular expression /balance/")
        return value

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('balance',):
            raise ValueError("must be one of enum values ('balance')")
        return value

    @validator('operation_type')
    def operation_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('MANUAL', 'AUTOMATIC',):
            raise ValueError("must be one of enum values ('MANUAL', 'AUTOMATIC')")
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
    def from_json(cls, json_str: str) -> LoyaltiesMembersBalanceUpdateResponseBody:
        """Create an instance of LoyaltiesMembersBalanceUpdateResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of related_object
        if self.related_object:
            _dict['related_object'] = self.related_object.to_dict()
        # set to None if points (nullable) is None
        # and __fields_set__ contains the field
        if self.points is None and "points" in self.__fields_set__:
            _dict['points'] = None

        # set to None if total (nullable) is None
        # and __fields_set__ contains the field
        if self.total is None and "total" in self.__fields_set__:
            _dict['total'] = None

        # set to None if balance (nullable) is None
        # and __fields_set__ contains the field
        if self.balance is None and "balance" in self.__fields_set__:
            _dict['balance'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if object (nullable) is None
        # and __fields_set__ contains the field
        if self.object is None and "object" in self.__fields_set__:
            _dict['object'] = None

        # set to None if related_object (nullable) is None
        # and __fields_set__ contains the field
        if self.related_object is None and "related_object" in self.__fields_set__:
            _dict['related_object'] = None

        # set to None if operation_type (nullable) is None
        # and __fields_set__ contains the field
        if self.operation_type is None and "operation_type" in self.__fields_set__:
            _dict['operation_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltiesMembersBalanceUpdateResponseBody:
        """Create an instance of LoyaltiesMembersBalanceUpdateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesMembersBalanceUpdateResponseBody.parse_obj(obj)

        _obj = LoyaltiesMembersBalanceUpdateResponseBody.parse_obj({
            "points": obj.get("points"),
            "total": obj.get("total"),
            "balance": obj.get("balance"),
            "type": obj.get("type"),
            "object": obj.get("object") if obj.get("object") is not None else 'balance',
            "related_object": LoyaltiesMembersBalanceUpdateResponseBodyRelatedObject.from_dict(obj.get("related_object")) if obj.get("related_object") is not None else None,
            "operation_type": obj.get("operation_type")
        })
        return _obj


