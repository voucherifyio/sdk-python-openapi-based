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

from datetime import date, datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, validator
from openapi_client.models.customer_base_address import CustomerBaseAddress
from openapi_client.models.customer_loyalty import CustomerLoyalty
from openapi_client.models.customer_referrals import CustomerReferrals
from openapi_client.models.customer_response_data_assets import CustomerResponseDataAssets
from openapi_client.models.customer_summary import CustomerSummary

class CustomersUpdateResponseBody(BaseModel):
    """
    Response body schema for **PUT** `/customers/{customerId}`.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="The ID of an existing customer that will be linked to redemption in this request.")
    source_id: Optional[StrictStr] = Field(None, description="A unique identifier of the customer who validates a voucher. It can be a customer ID or email from a CRM system, database, or a third-party service. If you also pass a customer ID (unique ID assigned by Voucherify), the source ID will be ignored.")
    summary: Optional[CustomerSummary] = None
    loyalty: Optional[CustomerLoyalty] = None
    referrals: Optional[CustomerReferrals] = None
    system_metadata: Optional[Dict[str, Any]] = Field(None, description="Object used to store system metadata information.")
    created_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the customer was created in ISO 8601 format.")
    updated_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the customer was updated in ISO 8601 format.")
    assets: Optional[CustomerResponseDataAssets] = None
    object: StrictStr = Field(..., description="The type of object represented by JSON.")
    name: Optional[StrictStr] = Field(None, description="Customer's first and last name.")
    description: Optional[StrictStr] = Field(None, description="An arbitrary string that you can attach to a customer object.")
    email: Optional[StrictStr] = Field(None, description="Customer's email address.")
    phone: Optional[StrictStr] = Field(None, description="Customer's phone number. This parameter is mandatory when you try to send out codes to customers via an SMS channel.")
    birthday: Optional[date] = Field(None, description="*Deprecated* Customer's birthdate; format YYYY-MM-DD.")
    birthdate: Optional[date] = Field(None, description="Customer's birthdate; format YYYY-MM-DD.")
    address: Optional[CustomerBaseAddress] = None
    metadata: Optional[Dict[str, Any]] = Field(None, description="A set of custom key/value pairs that you can attach to a customer. The metadata object stores all custom attributes assigned to the customer. It can be useful for storing additional information about the customer in a structured format. This metadata can be used for validating whether the customer qualifies for a discount or it can be used in building customer segments.")
    __properties = ["id", "source_id", "summary", "loyalty", "referrals", "system_metadata", "created_at", "updated_at", "assets", "object", "name", "description", "email", "phone", "birthday", "birthdate", "address", "metadata"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('customer',):
            raise ValueError("must be one of enum values ('customer')")
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
    def from_json(cls, json_str: str) -> CustomersUpdateResponseBody:
        """Create an instance of CustomersUpdateResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loyalty
        if self.loyalty:
            _dict['loyalty'] = self.loyalty.to_dict()
        # override the default output from pydantic by calling `to_dict()` of referrals
        if self.referrals:
            _dict['referrals'] = self.referrals.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # set to None if summary (nullable) is None
        # and __fields_set__ contains the field
        if self.summary is None and "summary" in self.__fields_set__:
            _dict['summary'] = None

        # set to None if loyalty (nullable) is None
        # and __fields_set__ contains the field
        if self.loyalty is None and "loyalty" in self.__fields_set__:
            _dict['loyalty'] = None

        # set to None if referrals (nullable) is None
        # and __fields_set__ contains the field
        if self.referrals is None and "referrals" in self.__fields_set__:
            _dict['referrals'] = None

        # set to None if address (nullable) is None
        # and __fields_set__ contains the field
        if self.address is None and "address" in self.__fields_set__:
            _dict['address'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomersUpdateResponseBody:
        """Create an instance of CustomersUpdateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomersUpdateResponseBody.parse_obj(obj)

        _obj = CustomersUpdateResponseBody.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("source_id"),
            "summary": CustomerSummary.from_dict(obj.get("summary")) if obj.get("summary") is not None else None,
            "loyalty": CustomerLoyalty.from_dict(obj.get("loyalty")) if obj.get("loyalty") is not None else None,
            "referrals": CustomerReferrals.from_dict(obj.get("referrals")) if obj.get("referrals") is not None else None,
            "system_metadata": obj.get("system_metadata"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "assets": CustomerResponseDataAssets.from_dict(obj.get("assets")) if obj.get("assets") is not None else None,
            "object": obj.get("object") if obj.get("object") is not None else 'customer',
            "name": obj.get("name"),
            "description": obj.get("description"),
            "email": obj.get("email"),
            "phone": obj.get("phone"),
            "birthday": obj.get("birthday"),
            "birthdate": obj.get("birthdate"),
            "address": CustomerBaseAddress.from_dict(obj.get("address")) if obj.get("address") is not None else None,
            "metadata": obj.get("metadata")
        })
        return _obj


