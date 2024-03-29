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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from voucherify_client.models.customer import Customer

class CreatePublicationWithSpecificVoucher(BaseModel):
    """
    Create publication with specific voucher.  # noqa: E501
    """
    source_id: Optional[StrictStr] = Field(None, description="The merchant’s publication ID if it is different from the Voucherify publication ID. It's an optional tracking identifier of a publication. It is really useful in case of an integration between multiple systems. It can be a publication ID from a CRM system, database or 3rd-party service. If `source_id` is provided only 1 voucher can be published per request.")
    customer: Customer = Field(...)
    metadata: Optional[Dict[str, Any]] = Field(None, description="The metadata object stores all custom attributes assigned to the publication. A set of key/value pairs that you can attach to a publication object. It can be useful for storing additional information about the publication in a structured format.")
    voucher: StrictStr = Field(..., description="Code of voucher being published.")
    __properties = ["source_id", "customer", "metadata", "voucher"]

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
    def from_json(cls, json_str: str) -> CreatePublicationWithSpecificVoucher:
        """Create an instance of CreatePublicationWithSpecificVoucher from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreatePublicationWithSpecificVoucher:
        """Create an instance of CreatePublicationWithSpecificVoucher from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreatePublicationWithSpecificVoucher.parse_obj(obj)

        _obj = CreatePublicationWithSpecificVoucher.parse_obj({
            "source_id": obj.get("source_id"),
            "customer": Customer.from_dict(obj.get("customer")) if obj.get("customer") is not None else None,
            "metadata": obj.get("metadata"),
            "voucher": obj.get("voucher")
        })
        return _obj


