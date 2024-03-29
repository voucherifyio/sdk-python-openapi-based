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



from pydantic import BaseModel, Field, StrictInt, constr, validator
from voucherify_client.models.voucher_transaction_details_balance_related_object import VoucherTransactionDetailsBalanceRelatedObject

class VoucherTransactionDetailsBalance(BaseModel):
    """
    Contains information on how the balance was affected by the transaction.  # noqa: E501
    """
    type: constr(strict=True) = Field(..., description="The type of voucher whose balance is being adjusted due to the transaction.")
    total: StrictInt = Field(..., description="The available points prior to the transaction.")
    object: constr(strict=True) = Field(..., description="The type of object represented by the JSON.")
    points: StrictInt = Field(..., description="The amount of points being used up in the transaction.")
    balance: StrictInt = Field(..., description="The points balance on the loyalty card after the points in the transaction are subtracted from the loyalty card.")
    related_object: VoucherTransactionDetailsBalanceRelatedObject = Field(...)
    __properties = ["type", "total", "object", "points", "balance", "related_object"]

    @validator('type')
    def type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"loyalty_card", value):
            raise ValueError(r"must validate the regular expression /loyalty_card/")
        return value

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('loyalty_card',):
            raise ValueError("must be one of enum values ('loyalty_card')")
        return value

    @validator('object')
    def object_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"balance", value):
            raise ValueError(r"must validate the regular expression /balance/")
        return value

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('balance',):
            raise ValueError("must be one of enum values ('balance')")
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
    def from_json(cls, json_str: str) -> VoucherTransactionDetailsBalance:
        """Create an instance of VoucherTransactionDetailsBalance from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VoucherTransactionDetailsBalance:
        """Create an instance of VoucherTransactionDetailsBalance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VoucherTransactionDetailsBalance.parse_obj(obj)

        _obj = VoucherTransactionDetailsBalance.parse_obj({
            "type": obj.get("type") if obj.get("type") is not None else 'loyalty_card',
            "total": obj.get("total"),
            "object": obj.get("object") if obj.get("object") is not None else 'balance',
            "points": obj.get("points"),
            "balance": obj.get("balance"),
            "related_object": VoucherTransactionDetailsBalanceRelatedObject.from_dict(obj.get("related_object")) if obj.get("related_object") is not None else None
        })
        return _obj


