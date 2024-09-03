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
from voucherify_client.models.loyalties_points_expiration_export_create_response_body_parameters import LoyaltiesPointsExpirationExportCreateResponseBodyParameters

class LoyaltiesPointsExpirationExportCreateResponseBody(BaseModel):
    """
    Object representing an export of points expirations.   # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="Unique export ID.")
    object: Optional[StrictStr] = Field('export', description="The type of object being represented. This object stores information about the export.")
    created_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the export was scheduled in ISO 8601 format.")
    status: Optional[StrictStr] = Field('SCHEDULED', description="Status of the export. Informs you whether the export has already been completed.")
    channel: Optional[StrictStr] = Field(None, description="The channel through which the export was triggered.")
    exported_object: Optional[StrictStr] = Field('points_expiration', description="The type of exported object.")
    parameters: Optional[LoyaltiesPointsExpirationExportCreateResponseBodyParameters] = None
    result: Optional[Dict[str, Any]] = Field(None, description="Always null.")
    user_id: Optional[StrictStr] = Field(None, description="`user_id` identifies the specific user who initiated the export through the Voucherify Dashboard. `user_id` is returned when the channel value is `WEBSITE`.")
    __properties = ["id", "object", "created_at", "status", "channel", "exported_object", "parameters", "result", "user_id"]

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('export',):
            raise ValueError("must be one of enum values ('export')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('SCHEDULED',):
            raise ValueError("must be one of enum values ('SCHEDULED')")
        return value

    @validator('channel')
    def channel_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('API', 'WEBSITE',):
            raise ValueError("must be one of enum values ('API', 'WEBSITE')")
        return value

    @validator('exported_object')
    def exported_object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('points_expiration',):
            raise ValueError("must be one of enum values ('points_expiration')")
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
    def from_json(cls, json_str: str) -> LoyaltiesPointsExpirationExportCreateResponseBody:
        """Create an instance of LoyaltiesPointsExpirationExportCreateResponseBody from a JSON string"""
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
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if object (nullable) is None
        # and __fields_set__ contains the field
        if self.object is None and "object" in self.__fields_set__:
            _dict['object'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if channel (nullable) is None
        # and __fields_set__ contains the field
        if self.channel is None and "channel" in self.__fields_set__:
            _dict['channel'] = None

        # set to None if exported_object (nullable) is None
        # and __fields_set__ contains the field
        if self.exported_object is None and "exported_object" in self.__fields_set__:
            _dict['exported_object'] = None

        # set to None if result (nullable) is None
        # and __fields_set__ contains the field
        if self.result is None and "result" in self.__fields_set__:
            _dict['result'] = None

        # set to None if user_id (nullable) is None
        # and __fields_set__ contains the field
        if self.user_id is None and "user_id" in self.__fields_set__:
            _dict['user_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoyaltiesPointsExpirationExportCreateResponseBody:
        """Create an instance of LoyaltiesPointsExpirationExportCreateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoyaltiesPointsExpirationExportCreateResponseBody.parse_obj(obj)

        _obj = LoyaltiesPointsExpirationExportCreateResponseBody.parse_obj({
            "id": obj.get("id"),
            "object": obj.get("object") if obj.get("object") is not None else 'export',
            "created_at": obj.get("created_at"),
            "status": obj.get("status") if obj.get("status") is not None else 'SCHEDULED',
            "channel": obj.get("channel"),
            "exported_object": obj.get("exported_object") if obj.get("exported_object") is not None else 'points_expiration',
            "parameters": LoyaltiesPointsExpirationExportCreateResponseBodyParameters.from_dict(obj.get("parameters")) if obj.get("parameters") is not None else None,
            "result": obj.get("result"),
            "user_id": obj.get("user_id")
        })
        return _obj


