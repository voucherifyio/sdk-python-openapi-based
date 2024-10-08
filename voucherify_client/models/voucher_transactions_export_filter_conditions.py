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
from voucherify_client.models.voucher_transactions_export_filter_conditions_voucher_id import VoucherTransactionsExportFilterConditionsVoucherId

class VoucherTransactionsExportFilterConditions(BaseModel):
    """
    Filter condition.  # noqa: E501
    """
    voucher_id: Optional[VoucherTransactionsExportFilterConditionsVoucherId] = None
    __properties = ["voucher_id"]

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
    def from_json(cls, json_str: str) -> VoucherTransactionsExportFilterConditions:
        """Create an instance of VoucherTransactionsExportFilterConditions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of voucher_id
        if self.voucher_id:
            _dict['voucher_id'] = self.voucher_id.to_dict()
        # set to None if voucher_id (nullable) is None
        # and __fields_set__ contains the field
        if self.voucher_id is None and "voucher_id" in self.__fields_set__:
            _dict['voucher_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VoucherTransactionsExportFilterConditions:
        """Create an instance of VoucherTransactionsExportFilterConditions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VoucherTransactionsExportFilterConditions.parse_obj(obj)

        _obj = VoucherTransactionsExportFilterConditions.parse_obj({
            "voucher_id": VoucherTransactionsExportFilterConditionsVoucherId.from_dict(obj.get("voucher_id")) if obj.get("voucher_id") is not None else None
        })
        return _obj


