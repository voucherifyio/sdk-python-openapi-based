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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conint, validator

class AsyncActionGetResponseBody(BaseModel):
    """
    Response body schema for **GET** `v1/async-actions/{asyncActionId}`.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="Async action unique ID.")
    type: Optional[StrictStr] = Field(None, description="Type of async action.")
    status: Optional[StrictStr] = Field(None, description="Status of the async action. Informs you whether the async action has already been completed.")
    operation_status: Optional[StrictStr] = Field(None, description="Status of async action processing. Informs about the async action status, whether it failed, succeeded, or the status is unknown.")
    created_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the async action was scheduled in ISO 8601 format.")
    updated_at: Optional[datetime] = Field(None, description="Timestamp representing the date and time when the async action was updated. The value is shown in the ISO 8601 format.")
    request_id: Optional[StrictStr] = Field(None, description="Unique request ID.")
    processing_time: Optional[StrictInt] = Field(None, description="The length of time it took to process the request in milliseconds.")
    progress: Optional[conint(strict=True, le=100, ge=0)] = Field(None, description="% progress to completion of the asynchronous action.")
    object: Optional[StrictStr] = Field('async_action', description="The type of the object represented by JSON. This object stores information about the `async_action`.")
    result: Optional[Dict[str, Any]] = None
    __properties = ["id", "type", "status", "operation_status", "created_at", "updated_at", "request_id", "processing_time", "progress", "object", "result"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('DONE', 'ENQUEUED', 'FAILED', 'IN_PROGRESS',):
            raise ValueError("must be one of enum values ('DONE', 'ENQUEUED', 'FAILED', 'IN_PROGRESS')")
        return value

    @validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('async_action',):
            raise ValueError("must be one of enum values ('async_action')")
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
    def from_json(cls, json_str: str) -> AsyncActionGetResponseBody:
        """Create an instance of AsyncActionGetResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if operation_status (nullable) is None
        # and __fields_set__ contains the field
        if self.operation_status is None and "operation_status" in self.__fields_set__:
            _dict['operation_status'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        # set to None if request_id (nullable) is None
        # and __fields_set__ contains the field
        if self.request_id is None and "request_id" in self.__fields_set__:
            _dict['request_id'] = None

        # set to None if processing_time (nullable) is None
        # and __fields_set__ contains the field
        if self.processing_time is None and "processing_time" in self.__fields_set__:
            _dict['processing_time'] = None

        # set to None if progress (nullable) is None
        # and __fields_set__ contains the field
        if self.progress is None and "progress" in self.__fields_set__:
            _dict['progress'] = None

        # set to None if object (nullable) is None
        # and __fields_set__ contains the field
        if self.object is None and "object" in self.__fields_set__:
            _dict['object'] = None

        # set to None if result (nullable) is None
        # and __fields_set__ contains the field
        if self.result is None and "result" in self.__fields_set__:
            _dict['result'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AsyncActionGetResponseBody:
        """Create an instance of AsyncActionGetResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AsyncActionGetResponseBody.parse_obj(obj)

        _obj = AsyncActionGetResponseBody.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "status": obj.get("status"),
            "operation_status": obj.get("operation_status"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "request_id": obj.get("request_id"),
            "processing_time": obj.get("processing_time"),
            "progress": obj.get("progress"),
            "object": obj.get("object") if obj.get("object") is not None else 'async_action',
            "result": obj.get("result")
        })
        return _obj


