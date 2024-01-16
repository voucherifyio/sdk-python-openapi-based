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

class ExportCustomerFilters(BaseModel):
    """
    ExportCustomerFilters
    """
    junction: Optional[Junction] = None
    name: Optional[FieldConditions] = None
    id: Optional[FieldConditions] = None
    description: Optional[FieldConditions] = None
    email: Optional[FieldConditions] = None
    source_id: Optional[FieldConditions] = None
    created_at: Optional[FieldConditions] = None
    address_city: Optional[FieldConditions] = None
    address_state: Optional[FieldConditions] = None
    address_line_1: Optional[FieldConditions] = None
    address_line_2: Optional[FieldConditions] = None
    address_country: Optional[FieldConditions] = None
    address_postal_code: Optional[FieldConditions] = None
    redemptions_total_redeemed: Optional[FieldConditions] = None
    redemptions_total_failed: Optional[FieldConditions] = None
    redemptions_total_succeeded: Optional[FieldConditions] = None
    redemptions_total_rolled_back: Optional[FieldConditions] = None
    redemptions_total_rollback_failed: Optional[FieldConditions] = None
    redemptions_total_rollback_succeeded: Optional[FieldConditions] = None
    orders_total_amount: Optional[FieldConditions] = None
    orders_total_count: Optional[FieldConditions] = None
    orders_average_amount: Optional[FieldConditions] = None
    orders_last_order_amount: Optional[FieldConditions] = None
    orders_last_order_date: Optional[FieldConditions] = None
    loyalty_points: Optional[FieldConditions] = None
    loyalty_referred_customers: Optional[FieldConditions] = None
    updated_at: Optional[FieldConditions] = None
    phone: Optional[FieldConditions] = None
    birthday: Optional[FieldConditions] = None
    metadata: Optional[FieldConditions] = None
    birthdate: Optional[FieldConditions] = None
    __properties = ["junction", "name", "id", "description", "email", "source_id", "created_at", "address_city", "address_state", "address_line_1", "address_line_2", "address_country", "address_postal_code", "redemptions_total_redeemed", "redemptions_total_failed", "redemptions_total_succeeded", "redemptions_total_rolled_back", "redemptions_total_rollback_failed", "redemptions_total_rollback_succeeded", "orders_total_amount", "orders_total_count", "orders_average_amount", "orders_last_order_amount", "orders_last_order_date", "loyalty_points", "loyalty_referred_customers", "updated_at", "phone", "birthday", "metadata", "birthdate"]

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
    def from_json(cls, json_str: str) -> ExportCustomerFilters:
        """Create an instance of ExportCustomerFilters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of name
        if self.name:
            _dict['name'] = self.name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of description
        if self.description:
            _dict['description'] = self.description.to_dict()
        # override the default output from pydantic by calling `to_dict()` of email
        if self.email:
            _dict['email'] = self.email.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source_id
        if self.source_id:
            _dict['source_id'] = self.source_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_at
        if self.created_at:
            _dict['created_at'] = self.created_at.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address_city
        if self.address_city:
            _dict['address_city'] = self.address_city.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address_state
        if self.address_state:
            _dict['address_state'] = self.address_state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address_line_1
        if self.address_line_1:
            _dict['address_line_1'] = self.address_line_1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address_line_2
        if self.address_line_2:
            _dict['address_line_2'] = self.address_line_2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address_country
        if self.address_country:
            _dict['address_country'] = self.address_country.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address_postal_code
        if self.address_postal_code:
            _dict['address_postal_code'] = self.address_postal_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redemptions_total_redeemed
        if self.redemptions_total_redeemed:
            _dict['redemptions_total_redeemed'] = self.redemptions_total_redeemed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redemptions_total_failed
        if self.redemptions_total_failed:
            _dict['redemptions_total_failed'] = self.redemptions_total_failed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redemptions_total_succeeded
        if self.redemptions_total_succeeded:
            _dict['redemptions_total_succeeded'] = self.redemptions_total_succeeded.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redemptions_total_rolled_back
        if self.redemptions_total_rolled_back:
            _dict['redemptions_total_rolled_back'] = self.redemptions_total_rolled_back.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redemptions_total_rollback_failed
        if self.redemptions_total_rollback_failed:
            _dict['redemptions_total_rollback_failed'] = self.redemptions_total_rollback_failed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redemptions_total_rollback_succeeded
        if self.redemptions_total_rollback_succeeded:
            _dict['redemptions_total_rollback_succeeded'] = self.redemptions_total_rollback_succeeded.to_dict()
        # override the default output from pydantic by calling `to_dict()` of orders_total_amount
        if self.orders_total_amount:
            _dict['orders_total_amount'] = self.orders_total_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of orders_total_count
        if self.orders_total_count:
            _dict['orders_total_count'] = self.orders_total_count.to_dict()
        # override the default output from pydantic by calling `to_dict()` of orders_average_amount
        if self.orders_average_amount:
            _dict['orders_average_amount'] = self.orders_average_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of orders_last_order_amount
        if self.orders_last_order_amount:
            _dict['orders_last_order_amount'] = self.orders_last_order_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of orders_last_order_date
        if self.orders_last_order_date:
            _dict['orders_last_order_date'] = self.orders_last_order_date.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loyalty_points
        if self.loyalty_points:
            _dict['loyalty_points'] = self.loyalty_points.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loyalty_referred_customers
        if self.loyalty_referred_customers:
            _dict['loyalty_referred_customers'] = self.loyalty_referred_customers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_at
        if self.updated_at:
            _dict['updated_at'] = self.updated_at.to_dict()
        # override the default output from pydantic by calling `to_dict()` of phone
        if self.phone:
            _dict['phone'] = self.phone.to_dict()
        # override the default output from pydantic by calling `to_dict()` of birthday
        if self.birthday:
            _dict['birthday'] = self.birthday.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of birthdate
        if self.birthdate:
            _dict['birthdate'] = self.birthdate.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExportCustomerFilters:
        """Create an instance of ExportCustomerFilters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExportCustomerFilters.parse_obj(obj)

        _obj = ExportCustomerFilters.parse_obj({
            "junction": obj.get("junction"),
            "name": FieldConditions.from_dict(obj.get("name")) if obj.get("name") is not None else None,
            "id": FieldConditions.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "description": FieldConditions.from_dict(obj.get("description")) if obj.get("description") is not None else None,
            "email": FieldConditions.from_dict(obj.get("email")) if obj.get("email") is not None else None,
            "source_id": FieldConditions.from_dict(obj.get("source_id")) if obj.get("source_id") is not None else None,
            "created_at": FieldConditions.from_dict(obj.get("created_at")) if obj.get("created_at") is not None else None,
            "address_city": FieldConditions.from_dict(obj.get("address_city")) if obj.get("address_city") is not None else None,
            "address_state": FieldConditions.from_dict(obj.get("address_state")) if obj.get("address_state") is not None else None,
            "address_line_1": FieldConditions.from_dict(obj.get("address_line_1")) if obj.get("address_line_1") is not None else None,
            "address_line_2": FieldConditions.from_dict(obj.get("address_line_2")) if obj.get("address_line_2") is not None else None,
            "address_country": FieldConditions.from_dict(obj.get("address_country")) if obj.get("address_country") is not None else None,
            "address_postal_code": FieldConditions.from_dict(obj.get("address_postal_code")) if obj.get("address_postal_code") is not None else None,
            "redemptions_total_redeemed": FieldConditions.from_dict(obj.get("redemptions_total_redeemed")) if obj.get("redemptions_total_redeemed") is not None else None,
            "redemptions_total_failed": FieldConditions.from_dict(obj.get("redemptions_total_failed")) if obj.get("redemptions_total_failed") is not None else None,
            "redemptions_total_succeeded": FieldConditions.from_dict(obj.get("redemptions_total_succeeded")) if obj.get("redemptions_total_succeeded") is not None else None,
            "redemptions_total_rolled_back": FieldConditions.from_dict(obj.get("redemptions_total_rolled_back")) if obj.get("redemptions_total_rolled_back") is not None else None,
            "redemptions_total_rollback_failed": FieldConditions.from_dict(obj.get("redemptions_total_rollback_failed")) if obj.get("redemptions_total_rollback_failed") is not None else None,
            "redemptions_total_rollback_succeeded": FieldConditions.from_dict(obj.get("redemptions_total_rollback_succeeded")) if obj.get("redemptions_total_rollback_succeeded") is not None else None,
            "orders_total_amount": FieldConditions.from_dict(obj.get("orders_total_amount")) if obj.get("orders_total_amount") is not None else None,
            "orders_total_count": FieldConditions.from_dict(obj.get("orders_total_count")) if obj.get("orders_total_count") is not None else None,
            "orders_average_amount": FieldConditions.from_dict(obj.get("orders_average_amount")) if obj.get("orders_average_amount") is not None else None,
            "orders_last_order_amount": FieldConditions.from_dict(obj.get("orders_last_order_amount")) if obj.get("orders_last_order_amount") is not None else None,
            "orders_last_order_date": FieldConditions.from_dict(obj.get("orders_last_order_date")) if obj.get("orders_last_order_date") is not None else None,
            "loyalty_points": FieldConditions.from_dict(obj.get("loyalty_points")) if obj.get("loyalty_points") is not None else None,
            "loyalty_referred_customers": FieldConditions.from_dict(obj.get("loyalty_referred_customers")) if obj.get("loyalty_referred_customers") is not None else None,
            "updated_at": FieldConditions.from_dict(obj.get("updated_at")) if obj.get("updated_at") is not None else None,
            "phone": FieldConditions.from_dict(obj.get("phone")) if obj.get("phone") is not None else None,
            "birthday": FieldConditions.from_dict(obj.get("birthday")) if obj.get("birthday") is not None else None,
            "metadata": FieldConditions.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "birthdate": FieldConditions.from_dict(obj.get("birthdate")) if obj.get("birthdate") is not None else None
        })
        return _obj


