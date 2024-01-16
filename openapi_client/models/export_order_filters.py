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
from openapi_client.models.field_conditions import FieldConditions
from openapi_client.models.junction import Junction

class ExportOrderFilters(BaseModel):
    """
    ExportOrderFilters
    """
    junction: Optional[Junction] = None
    id: Optional[FieldConditions] = None
    source_id: Optional[FieldConditions] = None
    created_at: Optional[FieldConditions] = None
    updated_at: Optional[FieldConditions] = None
    status: Optional[FieldConditions] = None
    amount: Optional[FieldConditions] = None
    discount_amount: Optional[FieldConditions] = None
    items_discount_amount: Optional[FieldConditions] = None
    total_discount_amount: Optional[FieldConditions] = None
    total_amount: Optional[FieldConditions] = None
    customer_id: Optional[FieldConditions] = None
    referrer_id: Optional[FieldConditions] = None
    metadata: Optional[FieldConditions] = None
    __properties = ["junction", "id", "source_id", "created_at", "updated_at", "status", "amount", "discount_amount", "items_discount_amount", "total_discount_amount", "total_amount", "customer_id", "referrer_id", "metadata"]

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
    def from_json(cls, json_str: str) -> ExportOrderFilters:
        """Create an instance of ExportOrderFilters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source_id
        if self.source_id:
            _dict['source_id'] = self.source_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_at
        if self.created_at:
            _dict['created_at'] = self.created_at.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_at
        if self.updated_at:
            _dict['updated_at'] = self.updated_at.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discount_amount
        if self.discount_amount:
            _dict['discount_amount'] = self.discount_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of items_discount_amount
        if self.items_discount_amount:
            _dict['items_discount_amount'] = self.items_discount_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_discount_amount
        if self.total_discount_amount:
            _dict['total_discount_amount'] = self.total_discount_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_amount
        if self.total_amount:
            _dict['total_amount'] = self.total_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer_id
        if self.customer_id:
            _dict['customer_id'] = self.customer_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of referrer_id
        if self.referrer_id:
            _dict['referrer_id'] = self.referrer_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExportOrderFilters:
        """Create an instance of ExportOrderFilters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExportOrderFilters.parse_obj(obj)

        _obj = ExportOrderFilters.parse_obj({
            "junction": obj.get("junction"),
            "id": FieldConditions.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "source_id": FieldConditions.from_dict(obj.get("source_id")) if obj.get("source_id") is not None else None,
            "created_at": FieldConditions.from_dict(obj.get("created_at")) if obj.get("created_at") is not None else None,
            "updated_at": FieldConditions.from_dict(obj.get("updated_at")) if obj.get("updated_at") is not None else None,
            "status": FieldConditions.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "amount": FieldConditions.from_dict(obj.get("amount")) if obj.get("amount") is not None else None,
            "discount_amount": FieldConditions.from_dict(obj.get("discount_amount")) if obj.get("discount_amount") is not None else None,
            "items_discount_amount": FieldConditions.from_dict(obj.get("items_discount_amount")) if obj.get("items_discount_amount") is not None else None,
            "total_discount_amount": FieldConditions.from_dict(obj.get("total_discount_amount")) if obj.get("total_discount_amount") is not None else None,
            "total_amount": FieldConditions.from_dict(obj.get("total_amount")) if obj.get("total_amount") is not None else None,
            "customer_id": FieldConditions.from_dict(obj.get("customer_id")) if obj.get("customer_id") is not None else None,
            "referrer_id": FieldConditions.from_dict(obj.get("referrer_id")) if obj.get("referrer_id") is not None else None,
            "metadata": FieldConditions.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None
        })
        return _obj

