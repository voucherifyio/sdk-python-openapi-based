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
from pydantic import BaseModel, Field, conlist
from openapi_client.models.order_calculated_no_customer_data import OrderCalculatedNoCustomerData
from openapi_client.models.redemption_rollback import RedemptionRollback

class RedemptionsRollbacksCreateResponseBody(BaseModel):
    """
    Response body schema for POST `/redemptions/{parentRedemptionID}/rollbacks`.  # noqa: E501
    """
    rollbacks: Optional[conlist(RedemptionRollback)] = Field(None, description="Contains the rollback redemption objects of the particular incentives.")
    parent_rollback: Optional[RedemptionRollback] = None
    order: Optional[OrderCalculatedNoCustomerData] = None
    __properties = ["rollbacks", "parent_rollback", "order"]

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
    def from_json(cls, json_str: str) -> RedemptionsRollbacksCreateResponseBody:
        """Create an instance of RedemptionsRollbacksCreateResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in rollbacks (list)
        _items = []
        if self.rollbacks:
            for _item in self.rollbacks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rollbacks'] = _items
        # override the default output from pydantic by calling `to_dict()` of parent_rollback
        if self.parent_rollback:
            _dict['parent_rollback'] = self.parent_rollback.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order
        if self.order:
            _dict['order'] = self.order.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RedemptionsRollbacksCreateResponseBody:
        """Create an instance of RedemptionsRollbacksCreateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RedemptionsRollbacksCreateResponseBody.parse_obj(obj)

        _obj = RedemptionsRollbacksCreateResponseBody.parse_obj({
            "rollbacks": [RedemptionRollback.from_dict(_item) for _item in obj.get("rollbacks")] if obj.get("rollbacks") is not None else None,
            "parent_rollback": RedemptionRollback.from_dict(obj.get("parent_rollback")) if obj.get("parent_rollback") is not None else None,
            "order": OrderCalculatedNoCustomerData.from_dict(obj.get("order")) if obj.get("order") is not None else None
        })
        return _obj


