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
from pydantic import BaseModel, Field, StrictStr, conlist, validator

class VoucherTransactionsExportParameters(BaseModel):
    """
    List of available fields and filters that can be exported with a gift card or loyalty card transactions export along with the sorting order of the returned data.  # noqa: E501
    """
    order: Optional[StrictStr] = Field(None, description="How the export is filtered, where the dash `-` preceding a sorting option means sorting in a descending order.")
    fields: Optional[conlist(StrictStr)] = Field(None, description="Array of strings containing the data in the export. These fields define the headers in the CSV file. The array can be a combination of any of the following available fields:  | **Field** | **Definition** | **Example Export** | |:---|:---|:---| | id | Unique transaction ID. | vtx_0cb7811f1c07765800 | | type | Transaction type. | - `CREDITS_REMOVAL` <br> - `CREDITS_ADDITION` <br> - `CREDITS_REFUND` <br> - `CREDITS_REDEMPTION` <br> - `POINTS_ACCRUAL` <br> - `POINTS_REDEMPTION`<br> - `POINTS_REFUND`<br> - `POINTS_ADDITION`<br> - `POINTS_REMOVAL`<br> - `POINTS_EXPIRATION`<br> - `POINTS_TRANSFER_IN`<br> - `POINTS_TRANSFER_OUT` | | source_id | Unique transaction source ID. | 8638 | | reason | Contains the reason for the transaction if one was included originally. |  | | balance | The gift card or loyalty card balance after the transaction. |  | | amount | The amount of gift card or loyalty card credits being allocated during the transaction. This value can either be negative or positive depending on the nature of the transaction. |  | | created_at | Timestamp in ISO 8601 format representing the date and time when the transaction was created. | 2022-03-09T09:16:32.521Z  | | voucher_id | Unique Voucher ID. | v_dky7ksKfPX50Wb2Bxvcoeb1xT20b6tcp | | campaign_id | Parent campaign ID. | camp_FNYR4jhqZBM9xTptxDGgeNBV | | source|  Channel through which the transaction was initiated. | API | | details | More detailed information stored in the form of a JSON. | Provides more details related to the transaction in the form of an object. | | related_transaction_id | Unique transaction ID related to a receiver/donor card in the case of a points transfer from/to another card. | vtx_0c9afe802593b34b80 |")
    __properties = ["order", "fields"]

    @validator('order')
    def order_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('-created_at', 'created_at',):
            raise ValueError("must be one of enum values ('-created_at', 'created_at')")
        return value

    @validator('fields')
    def fields_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('id', 'type', 'source_id', 'reason', 'balance', 'amount', 'created_at', 'voucher_id', 'campaign_id', 'source', 'details', 'related_transaction_id',):
                raise ValueError("each list item must be one of ('id', 'type', 'source_id', 'reason', 'balance', 'amount', 'created_at', 'voucher_id', 'campaign_id', 'source', 'details', 'related_transaction_id')")
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
    def from_json(cls, json_str: str) -> VoucherTransactionsExportParameters:
        """Create an instance of VoucherTransactionsExportParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if order (nullable) is None
        # and __fields_set__ contains the field
        if self.order is None and "order" in self.__fields_set__:
            _dict['order'] = None

        # set to None if fields (nullable) is None
        # and __fields_set__ contains the field
        if self.fields is None and "fields" in self.__fields_set__:
            _dict['fields'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VoucherTransactionsExportParameters:
        """Create an instance of VoucherTransactionsExportParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VoucherTransactionsExportParameters.parse_obj(obj)

        _obj = VoucherTransactionsExportParameters.parse_obj({
            "order": obj.get("order"),
            "fields": obj.get("fields")
        })
        return _obj


