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



from pydantic import BaseModel, Field
from voucherify_client.models.earning_rule_proportional_order_amount_order_amount import EarningRuleProportionalOrderAmountOrderAmount

class EarningRuleProportionalOrderTotalAmountOrder(BaseModel):
    """
    EarningRuleProportionalOrderTotalAmountOrder
    """
    total_amount: EarningRuleProportionalOrderAmountOrderAmount = Field(...)
    __properties = ["total_amount"]

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
    def from_json(cls, json_str: str) -> EarningRuleProportionalOrderTotalAmountOrder:
        """Create an instance of EarningRuleProportionalOrderTotalAmountOrder from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of total_amount
        if self.total_amount:
            _dict['total_amount'] = self.total_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EarningRuleProportionalOrderTotalAmountOrder:
        """Create an instance of EarningRuleProportionalOrderTotalAmountOrder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EarningRuleProportionalOrderTotalAmountOrder.parse_obj(obj)

        _obj = EarningRuleProportionalOrderTotalAmountOrder.parse_obj({
            "total_amount": EarningRuleProportionalOrderAmountOrderAmount.from_dict(obj.get("total_amount")) if obj.get("total_amount") is not None else None
        })
        return _obj


