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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from voucherify_client.models.client_redemptions_redeem_request_body_all_of_options import ClientRedemptionsRedeemRequestBodyAllOfOptions
from voucherify_client.models.customer import Customer
from voucherify_client.models.order import Order
from voucherify_client.models.session import Session
from voucherify_client.models.stackable_validate_redeem_base_redeemables_item import StackableValidateRedeemBaseRedeemablesItem

class ClientRedemptionsRedeemRequestBody(BaseModel):
    """
    Response body schema for **POST** `/redemptions`.  # noqa: E501
    """
    redeemables: conlist(StackableValidateRedeemBaseRedeemablesItem, max_items=5, min_items=1) = Field(..., description="An array of redeemables. You can combine `voucher`(s) and `promotion_tier`(s). Alternatively, send one unique`promotion_stack` in the array.")
    order: Optional[Order] = None
    customer: Optional[Customer] = None
    session: Optional[Session] = None
    tracking_id: Optional[StrictStr] = Field(None, description="Is correspondent to Customer's source_id")
    metadata: Optional[Dict[str, Any]] = Field(None, description="A set of key/value pairs that you can attach to a redemption object. It can be useful for storing additional information about the redemption in a structured format.")
    options: Optional[ClientRedemptionsRedeemRequestBodyAllOfOptions] = None
    __properties = ["redeemables", "order", "customer", "session", "tracking_id", "metadata", "options"]

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
    def from_json(cls, json_str: str) -> ClientRedemptionsRedeemRequestBody:
        """Create an instance of ClientRedemptionsRedeemRequestBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of session
        if self.session:
            _dict['session'] = self.session.to_dict()
        # override the default output from pydantic by calling `to_dict()` of options
        if self.options:
            _dict['options'] = self.options.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClientRedemptionsRedeemRequestBody:
        """Create an instance of ClientRedemptionsRedeemRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClientRedemptionsRedeemRequestBody.parse_obj(obj)

        _obj = ClientRedemptionsRedeemRequestBody.parse_obj({
            "redeemables": [StackableValidateRedeemBaseRedeemablesItem.from_dict(_item) for _item in obj.get("redeemables")] if obj.get("redeemables") is not None else None,
            "order": Order.from_dict(obj.get("order")) if obj.get("order") is not None else None,
            "customer": Customer.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "session": Session.from_dict(obj.get("session")) if obj.get("session") is not None else None,
            "tracking_id": obj.get("tracking_id"),
            "metadata": obj.get("metadata"),
            "options": ClientRedemptionsRedeemRequestBodyAllOfOptions.from_dict(obj.get("options")) if obj.get("options") is not None else None
        })
        return _obj


