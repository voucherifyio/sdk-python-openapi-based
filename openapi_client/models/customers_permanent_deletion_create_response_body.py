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

from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.customers_permanent_deletion_create_response_body_data_json import CustomersPermanentDeletionCreateResponseBodyDataJson

class CustomersPermanentDeletionCreateResponseBody(BaseModel):
    """
    Response body schema for **POST** `/customers/{customerId}/permanent-deletion`.  # noqa: E501
    """
    id: StrictStr = Field(..., description="Unique permanent deletion object ID.")
    created_at: datetime = Field(..., description="Timestamp representing the date and time when the customer was requested to be deleted in ISO 8601 format.")
    related_object_id: StrictStr = Field(..., description="Unique customer ID that is being deleted.")
    related_object: StrictStr = Field(..., description="Object being deleted.")
    status: StrictStr = Field(..., description="Deletion status.")
    data_json: CustomersPermanentDeletionCreateResponseBodyDataJson = Field(...)
    object: StrictStr = Field(..., description="The type of object represented by JSON.")
    __properties = ["id", "created_at", "related_object_id", "related_object", "status", "data_json", "object"]

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
    def from_json(cls, json_str: str) -> CustomersPermanentDeletionCreateResponseBody:
        """Create an instance of CustomersPermanentDeletionCreateResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data_json
        if self.data_json:
            _dict['data_json'] = self.data_json.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomersPermanentDeletionCreateResponseBody:
        """Create an instance of CustomersPermanentDeletionCreateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomersPermanentDeletionCreateResponseBody.parse_obj(obj)

        _obj = CustomersPermanentDeletionCreateResponseBody.parse_obj({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "related_object_id": obj.get("related_object_id"),
            "related_object": obj.get("related_object") if obj.get("related_object") is not None else 'customer',
            "status": obj.get("status") if obj.get("status") is not None else 'DONE',
            "data_json": CustomersPermanentDeletionCreateResponseBodyDataJson.from_dict(obj.get("data_json")) if obj.get("data_json") is not None else None,
            "object": obj.get("object") if obj.get("object") is not None else 'pernament_deletion'
        })
        return _obj


