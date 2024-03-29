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
from voucherify_client.models.export_customer_scheduled import ExportCustomerScheduled
from voucherify_client.models.export_order_scheduled import ExportOrderScheduled
from voucherify_client.models.export_points_expiration_scheduled import ExportPointsExpirationScheduled
from voucherify_client.models.export_publication_scheduled import ExportPublicationScheduled
from voucherify_client.models.export_redemption_scheduled import ExportRedemptionScheduled
from voucherify_client.models.export_voucher_scheduled import ExportVoucherScheduled
from voucherify_client.models.export_voucher_transactions_scheduled import ExportVoucherTransactionsScheduled
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

EXPORTS_CREATE_RESPONSE_BODY_ONE_OF_SCHEMAS = ["ExportCustomerScheduled", "ExportOrderScheduled", "ExportPointsExpirationScheduled", "ExportPublicationScheduled", "ExportRedemptionScheduled", "ExportVoucherScheduled", "ExportVoucherTransactionsScheduled"]

class ExportsCreateResponseBody(BaseModel):
    """
    Response body schema for **POST** `/exports`.
    """
    # data type: ExportVoucherScheduled
    oneof_schema_1_validator: Optional[ExportVoucherScheduled] = None
    # data type: ExportRedemptionScheduled
    oneof_schema_2_validator: Optional[ExportRedemptionScheduled] = None
    # data type: ExportCustomerScheduled
    oneof_schema_3_validator: Optional[ExportCustomerScheduled] = None
    # data type: ExportPublicationScheduled
    oneof_schema_4_validator: Optional[ExportPublicationScheduled] = None
    # data type: ExportOrderScheduled
    oneof_schema_5_validator: Optional[ExportOrderScheduled] = None
    # data type: ExportPointsExpirationScheduled
    oneof_schema_6_validator: Optional[ExportPointsExpirationScheduled] = None
    # data type: ExportVoucherTransactionsScheduled
    oneof_schema_7_validator: Optional[ExportVoucherTransactionsScheduled] = None
    if TYPE_CHECKING:
        actual_instance: Union[ExportCustomerScheduled, ExportOrderScheduled, ExportPointsExpirationScheduled, ExportPublicationScheduled, ExportRedemptionScheduled, ExportVoucherScheduled, ExportVoucherTransactionsScheduled]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(EXPORTS_CREATE_RESPONSE_BODY_ONE_OF_SCHEMAS, const=True)

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
        instance = ExportsCreateResponseBody.construct()
        error_messages = []
        match = 0
        # validate data type: ExportVoucherScheduled
        if not isinstance(v, ExportVoucherScheduled):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExportVoucherScheduled`")
        else:
            match += 1
        # validate data type: ExportRedemptionScheduled
        if not isinstance(v, ExportRedemptionScheduled):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExportRedemptionScheduled`")
        else:
            match += 1
        # validate data type: ExportCustomerScheduled
        if not isinstance(v, ExportCustomerScheduled):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExportCustomerScheduled`")
        else:
            match += 1
        # validate data type: ExportPublicationScheduled
        if not isinstance(v, ExportPublicationScheduled):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExportPublicationScheduled`")
        else:
            match += 1
        # validate data type: ExportOrderScheduled
        if not isinstance(v, ExportOrderScheduled):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExportOrderScheduled`")
        else:
            match += 1
        # validate data type: ExportPointsExpirationScheduled
        if not isinstance(v, ExportPointsExpirationScheduled):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExportPointsExpirationScheduled`")
        else:
            match += 1
        # validate data type: ExportVoucherTransactionsScheduled
        if not isinstance(v, ExportVoucherTransactionsScheduled):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExportVoucherTransactionsScheduled`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ExportsCreateResponseBody with oneOf schemas: ExportCustomerScheduled, ExportOrderScheduled, ExportPointsExpirationScheduled, ExportPublicationScheduled, ExportRedemptionScheduled, ExportVoucherScheduled, ExportVoucherTransactionsScheduled. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ExportsCreateResponseBody with oneOf schemas: ExportCustomerScheduled, ExportOrderScheduled, ExportPointsExpirationScheduled, ExportPublicationScheduled, ExportRedemptionScheduled, ExportVoucherScheduled, ExportVoucherTransactionsScheduled. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> ExportsCreateResponseBody:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> ExportsCreateResponseBody:
        """Returns the object represented by the json string"""
        instance = ExportsCreateResponseBody.construct()
        error_messages = []
        match = 0

        # deserialize data into ExportVoucherScheduled
        try:
            instance.actual_instance = ExportVoucherScheduled.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExportRedemptionScheduled
        try:
            instance.actual_instance = ExportRedemptionScheduled.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExportCustomerScheduled
        try:
            instance.actual_instance = ExportCustomerScheduled.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExportPublicationScheduled
        try:
            instance.actual_instance = ExportPublicationScheduled.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExportOrderScheduled
        try:
            instance.actual_instance = ExportOrderScheduled.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExportPointsExpirationScheduled
        try:
            instance.actual_instance = ExportPointsExpirationScheduled.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExportVoucherTransactionsScheduled
        try:
            instance.actual_instance = ExportVoucherTransactionsScheduled.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ExportsCreateResponseBody with oneOf schemas: ExportCustomerScheduled, ExportOrderScheduled, ExportPointsExpirationScheduled, ExportPublicationScheduled, ExportRedemptionScheduled, ExportVoucherScheduled, ExportVoucherTransactionsScheduled. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ExportsCreateResponseBody with oneOf schemas: ExportCustomerScheduled, ExportOrderScheduled, ExportPointsExpirationScheduled, ExportPublicationScheduled, ExportRedemptionScheduled, ExportVoucherScheduled, ExportVoucherTransactionsScheduled. Details: " + ", ".join(error_messages))
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


