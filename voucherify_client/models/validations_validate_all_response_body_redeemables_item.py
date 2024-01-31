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
from voucherify_client.models.validations_redeemable_applicable import ValidationsRedeemableApplicable
from voucherify_client.models.validations_redeemable_inapplicable import ValidationsRedeemableInapplicable
from voucherify_client.models.validations_redeemable_skipped import ValidationsRedeemableSkipped
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

VALIDATIONS_VALIDATE_ALL_RESPONSE_BODY_REDEEMABLES_ITEM_ONE_OF_SCHEMAS = ["ValidationsRedeemableApplicable", "ValidationsRedeemableInapplicable", "ValidationsRedeemableSkipped"]

class ValidationsValidateAllResponseBodyRedeemablesItem(BaseModel):
    """
    ValidationsValidateAllResponseBodyRedeemablesItem
    """
    # data type: ValidationsRedeemableApplicable
    oneof_schema_1_validator: Optional[ValidationsRedeemableApplicable] = None
    # data type: ValidationsRedeemableInapplicable
    oneof_schema_2_validator: Optional[ValidationsRedeemableInapplicable] = None
    # data type: ValidationsRedeemableSkipped
    oneof_schema_3_validator: Optional[ValidationsRedeemableSkipped] = None
    if TYPE_CHECKING:
        actual_instance: Union[ValidationsRedeemableApplicable, ValidationsRedeemableInapplicable, ValidationsRedeemableSkipped]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(VALIDATIONS_VALIDATE_ALL_RESPONSE_BODY_REDEEMABLES_ITEM_ONE_OF_SCHEMAS, const=True)

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
        instance = ValidationsValidateAllResponseBodyRedeemablesItem.construct()
        error_messages = []
        match = 0
        # validate data type: ValidationsRedeemableApplicable
        if not isinstance(v, ValidationsRedeemableApplicable):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ValidationsRedeemableApplicable`")
        else:
            match += 1
        # validate data type: ValidationsRedeemableInapplicable
        if not isinstance(v, ValidationsRedeemableInapplicable):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ValidationsRedeemableInapplicable`")
        else:
            match += 1
        # validate data type: ValidationsRedeemableSkipped
        if not isinstance(v, ValidationsRedeemableSkipped):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ValidationsRedeemableSkipped`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ValidationsValidateAllResponseBodyRedeemablesItem with oneOf schemas: ValidationsRedeemableApplicable, ValidationsRedeemableInapplicable, ValidationsRedeemableSkipped. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ValidationsValidateAllResponseBodyRedeemablesItem with oneOf schemas: ValidationsRedeemableApplicable, ValidationsRedeemableInapplicable, ValidationsRedeemableSkipped. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> ValidationsValidateAllResponseBodyRedeemablesItem:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> ValidationsValidateAllResponseBodyRedeemablesItem:
        """Returns the object represented by the json string"""
        instance = ValidationsValidateAllResponseBodyRedeemablesItem.construct()
        error_messages = []
        match = 0

        # deserialize data into ValidationsRedeemableApplicable
        try:
            instance.actual_instance = ValidationsRedeemableApplicable.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ValidationsRedeemableInapplicable
        try:
            instance.actual_instance = ValidationsRedeemableInapplicable.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ValidationsRedeemableSkipped
        try:
            instance.actual_instance = ValidationsRedeemableSkipped.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ValidationsValidateAllResponseBodyRedeemablesItem with oneOf schemas: ValidationsRedeemableApplicable, ValidationsRedeemableInapplicable, ValidationsRedeemableSkipped. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ValidationsValidateAllResponseBodyRedeemablesItem with oneOf schemas: ValidationsRedeemableApplicable, ValidationsRedeemableInapplicable, ValidationsRedeemableSkipped. Details: " + ", ".join(error_messages))
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


