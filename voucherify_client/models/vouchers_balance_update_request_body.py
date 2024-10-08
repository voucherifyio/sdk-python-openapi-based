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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class VouchersBalanceUpdateRequestBody(BaseModel):
    """
    Request body schema for `vouchers/{code}/balance`.  # noqa: E501
    """
    amount: Optional[StrictInt] = Field(None, description="The incremental amount to be added to or removed from the current balance on the gift card or loyalty card. Value is multiplied by 100 to precisely represent 2 decimal places. For example, $100 amount is written as 10000. To remove balance, simply add a minus sign before the value, i.e. to remove $20, use -2000.")
    source_id: Optional[StrictStr] = Field(None, description="The merchant's transaction ID if it is different from the Voucherify transaction ID. It is really useful in case of an integration between multiple systems. It can be a transaction ID from a CRM system, database or 3rd-party service.")
    reason: Optional[StrictStr] = Field(None, description="Reason why the transaction occurred.")
    __properties = ["amount", "source_id", "reason"]

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
    def from_json(cls, json_str: str) -> VouchersBalanceUpdateRequestBody:
        """Create an instance of VouchersBalanceUpdateRequestBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if amount (nullable) is None
        # and __fields_set__ contains the field
        if self.amount is None and "amount" in self.__fields_set__:
            _dict['amount'] = None

        # set to None if source_id (nullable) is None
        # and __fields_set__ contains the field
        if self.source_id is None and "source_id" in self.__fields_set__:
            _dict['source_id'] = None

        # set to None if reason (nullable) is None
        # and __fields_set__ contains the field
        if self.reason is None and "reason" in self.__fields_set__:
            _dict['reason'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VouchersBalanceUpdateRequestBody:
        """Create an instance of VouchersBalanceUpdateRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VouchersBalanceUpdateRequestBody.parse_obj(obj)

        _obj = VouchersBalanceUpdateRequestBody.parse_obj({
            "amount": obj.get("amount"),
            "source_id": obj.get("source_id"),
            "reason": obj.get("reason")
        })
        return _obj


