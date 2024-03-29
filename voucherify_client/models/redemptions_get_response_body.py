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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from voucherify_client.models.redemption import Redemption
from voucherify_client.models.redemption_rollback import RedemptionRollback
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

REDEMPTIONS_GET_RESPONSE_BODY_ONE_OF_SCHEMAS = ["Redemption", "RedemptionRollback"]

class RedemptionsGetResponseBody(BaseModel):
    """
    Response body schema for **GET** `/redemptions/{redemptionId}
    """
    # data type: Redemption
    oneof_schema_1_validator: Optional[Redemption] = None
    # data type: RedemptionRollback
    oneof_schema_2_validator: Optional[RedemptionRollback] = None
    if TYPE_CHECKING:
        actual_instance: Union[Redemption, RedemptionRollback]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(REDEMPTIONS_GET_RESPONSE_BODY_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = RedemptionsGetResponseBody.construct()
        error_messages = []
        match = 0
        # validate data type: Redemption
        if not isinstance(v, Redemption):
            error_messages.append(f"Error! Input type `{type(v)}` is not `Redemption`")
        else:
            match += 1
        # validate data type: RedemptionRollback
        if not isinstance(v, RedemptionRollback):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RedemptionRollback`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in RedemptionsGetResponseBody with oneOf schemas: Redemption, RedemptionRollback. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in RedemptionsGetResponseBody with oneOf schemas: Redemption, RedemptionRollback. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> RedemptionsGetResponseBody:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> RedemptionsGetResponseBody:
        """Returns the object represented by the json string"""
        instance = RedemptionsGetResponseBody.construct()
        error_messages = []
        match = 0

        # deserialize data into Redemption
        try:
            instance.actual_instance = Redemption.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RedemptionRollback
        try:
            instance.actual_instance = RedemptionRollback.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into RedemptionsGetResponseBody with oneOf schemas: Redemption, RedemptionRollback. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into RedemptionsGetResponseBody with oneOf schemas: Redemption, RedemptionRollback. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())


