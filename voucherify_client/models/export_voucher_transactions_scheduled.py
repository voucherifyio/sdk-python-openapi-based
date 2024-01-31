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
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, validator
from voucherify_client.models.loyalties_members_transactions_export_create_request_body_parameters import LoyaltiesMembersTransactionsExportCreateRequestBodyParameters

class ExportVoucherTransactionsScheduled(BaseModel):
    """
    ExportVoucherTransactionsScheduled
    """
    id: StrictStr = Field(..., description="Unique export ID.")
    object: StrictStr = Field(..., description="The type of object being represented. This object stores information about the export.")
    created_at: datetime = Field(..., description="Timestamp representing the date and time when the export was scheduled in ISO 8601 format.")
    status: StrictStr = Field(..., description="Status of the export. Informs you whether the export has already been completed, i.e. indicates whether the file containing the exported data has been generated.")
    channel: Optional[StrictStr] = Field(None, description="The channel through which the export was triggered.")
    result: Optional[Dict[str, Any]] = Field(..., description="Contains the URL of the CSV file.")
    user_id: StrictStr = Field(..., description="Identifies the specific user who initiated the export through the Voucherify Dashboard; returned when the channel value is WEBSITE.")
    exported_object: StrictStr = Field(..., description="The type of object to be exported.")
    parameters: Optional[LoyaltiesMembersTransactionsExportCreateRequestBodyParameters] = None
    __properties = ["id", "object", "created_at", "status", "channel", "result", "user_id", "exported_object", "parameters"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('export',):
            raise ValueError("must be one of enum values ('export')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('SCHEDULED',):
            raise ValueError("must be one of enum values ('SCHEDULED')")
        return value

    @validator('exported_object')
    def exported_object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('voucher_transactions',):
            raise ValueError("must be one of enum values ('voucher_transactions')")
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
    def from_json(cls, json_str: str) -> ExportVoucherTransactionsScheduled:
        """Create an instance of ExportVoucherTransactionsScheduled from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of parameters
        if self.parameters:
            _dict['parameters'] = self.parameters.to_dict()
        # set to None if result (nullable) is None
        # and __fields_set__ contains the field
        if self.result is None and "result" in self.__fields_set__:
            _dict['result'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExportVoucherTransactionsScheduled:
        """Create an instance of ExportVoucherTransactionsScheduled from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExportVoucherTransactionsScheduled.parse_obj(obj)

        _obj = ExportVoucherTransactionsScheduled.parse_obj({
            "id": obj.get("id"),
            "object": obj.get("object") if obj.get("object") is not None else 'export',
            "created_at": obj.get("created_at"),
            "status": obj.get("status") if obj.get("status") is not None else 'SCHEDULED',
            "channel": obj.get("channel"),
            "result": obj.get("result"),
            "user_id": obj.get("user_id"),
            "exported_object": obj.get("exported_object") if obj.get("exported_object") is not None else 'voucher_transactions',
            "parameters": LoyaltiesMembersTransactionsExportCreateRequestBodyParameters.from_dict(obj.get("parameters")) if obj.get("parameters") is not None else None
        })
        return _obj


