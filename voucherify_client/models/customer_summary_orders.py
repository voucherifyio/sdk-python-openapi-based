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
from typing import Optional
from pydantic import BaseModel, Field, StrictInt

class CustomerSummaryOrders(BaseModel):
    """
    CustomerSummaryOrders
    """
    total_amount: Optional[StrictInt] = Field(None, description="The total amount spent by the customer. Value is multiplied by 100 to precisely represent 2 decimal places. For example `10000 cents` for `$100.00`.")
    total_count: Optional[StrictInt] = Field(None, description="Total number of orders made by the customer.")
    average_amount: Optional[StrictInt] = Field(None, description="Average amount spent on orders. `total_amount` &divide; `total_count`. Value is multiplied by 100 to precisely represent 2 decimal places. For example `10000 cents` for `$100.00`.")
    last_order_amount: Optional[StrictInt] = Field(None, description="Amount spent on last order. Value is multiplied by 100 to precisely represent 2 decimal places. For example `10000 cents` for `$100.00`.")
    last_order_date: Optional[datetime] = Field(None, description="Timestamp representing the date and time of the customer's last order in ISO 8601 format.")
    __properties = ["total_amount", "total_count", "average_amount", "last_order_amount", "last_order_date"]

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
    def from_json(cls, json_str: str) -> CustomerSummaryOrders:
        """Create an instance of CustomerSummaryOrders from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if total_amount (nullable) is None
        # and __fields_set__ contains the field
        if self.total_amount is None and "total_amount" in self.__fields_set__:
            _dict['total_amount'] = None

        # set to None if total_count (nullable) is None
        # and __fields_set__ contains the field
        if self.total_count is None and "total_count" in self.__fields_set__:
            _dict['total_count'] = None

        # set to None if average_amount (nullable) is None
        # and __fields_set__ contains the field
        if self.average_amount is None and "average_amount" in self.__fields_set__:
            _dict['average_amount'] = None

        # set to None if last_order_amount (nullable) is None
        # and __fields_set__ contains the field
        if self.last_order_amount is None and "last_order_amount" in self.__fields_set__:
            _dict['last_order_amount'] = None

        # set to None if last_order_date (nullable) is None
        # and __fields_set__ contains the field
        if self.last_order_date is None and "last_order_date" in self.__fields_set__:
            _dict['last_order_date'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomerSummaryOrders:
        """Create an instance of CustomerSummaryOrders from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomerSummaryOrders.parse_obj(obj)

        _obj = CustomerSummaryOrders.parse_obj({
            "total_amount": obj.get("total_amount"),
            "total_count": obj.get("total_count"),
            "average_amount": obj.get("average_amount"),
            "last_order_amount": obj.get("last_order_amount"),
            "last_order_date": obj.get("last_order_date")
        })
        return _obj


