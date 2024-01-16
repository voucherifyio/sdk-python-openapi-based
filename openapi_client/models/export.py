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
from openapi_client.models.export_customer import ExportCustomer
from openapi_client.models.export_order import ExportOrder
from openapi_client.models.export_points_expiration import ExportPointsExpiration
from openapi_client.models.export_publication import ExportPublication
from openapi_client.models.export_redemption import ExportRedemption
from openapi_client.models.export_voucher import ExportVoucher
from openapi_client.models.export_voucher_transactions import ExportVoucherTransactions
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

EXPORT_ONE_OF_SCHEMAS = ["ExportCustomer", "ExportOrder", "ExportPointsExpiration", "ExportPublication", "ExportRedemption", "ExportVoucher", "ExportVoucherTransactions"]

class Export(BaseModel):
    """
    Export
    """
    # data type: ExportVoucher
    oneof_schema_1_validator: Optional[ExportVoucher] = None
    # data type: ExportRedemption
    oneof_schema_2_validator: Optional[ExportRedemption] = None
    # data type: ExportCustomer
    oneof_schema_3_validator: Optional[ExportCustomer] = None
    # data type: ExportPublication
    oneof_schema_4_validator: Optional[ExportPublication] = None
    # data type: ExportOrder
    oneof_schema_5_validator: Optional[ExportOrder] = None
    # data type: ExportPointsExpiration
    oneof_schema_6_validator: Optional[ExportPointsExpiration] = None
    # data type: ExportVoucherTransactions
    oneof_schema_7_validator: Optional[ExportVoucherTransactions] = None
    if TYPE_CHECKING:
        actual_instance: Union[ExportCustomer, ExportOrder, ExportPointsExpiration, ExportPublication, ExportRedemption, ExportVoucher, ExportVoucherTransactions]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(EXPORT_ONE_OF_SCHEMAS, const=True)

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
        instance = Export.construct()
        error_messages = []
        match = 0
        # validate data type: ExportVoucher
        if not isinstance(v, ExportVoucher):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExportVoucher`")
        else:
            match += 1
        # validate data type: ExportRedemption
        if not isinstance(v, ExportRedemption):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExportRedemption`")
        else:
            match += 1
        # validate data type: ExportCustomer
        if not isinstance(v, ExportCustomer):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExportCustomer`")
        else:
            match += 1
        # validate data type: ExportPublication
        if not isinstance(v, ExportPublication):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExportPublication`")
        else:
            match += 1
        # validate data type: ExportOrder
        if not isinstance(v, ExportOrder):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExportOrder`")
        else:
            match += 1
        # validate data type: ExportPointsExpiration
        if not isinstance(v, ExportPointsExpiration):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExportPointsExpiration`")
        else:
            match += 1
        # validate data type: ExportVoucherTransactions
        if not isinstance(v, ExportVoucherTransactions):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExportVoucherTransactions`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in Export with oneOf schemas: ExportCustomer, ExportOrder, ExportPointsExpiration, ExportPublication, ExportRedemption, ExportVoucher, ExportVoucherTransactions. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in Export with oneOf schemas: ExportCustomer, ExportOrder, ExportPointsExpiration, ExportPublication, ExportRedemption, ExportVoucher, ExportVoucherTransactions. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Export:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Export:
        """Returns the object represented by the json string"""
        instance = Export.construct()
        error_messages = []
        match = 0

        # deserialize data into ExportVoucher
        try:
            instance.actual_instance = ExportVoucher.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExportRedemption
        try:
            instance.actual_instance = ExportRedemption.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExportCustomer
        try:
            instance.actual_instance = ExportCustomer.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExportPublication
        try:
            instance.actual_instance = ExportPublication.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExportOrder
        try:
            instance.actual_instance = ExportOrder.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExportPointsExpiration
        try:
            instance.actual_instance = ExportPointsExpiration.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExportVoucherTransactions
        try:
            instance.actual_instance = ExportVoucherTransactions.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into Export with oneOf schemas: ExportCustomer, ExportOrder, ExportPointsExpiration, ExportPublication, ExportRedemption, ExportVoucher, ExportVoucherTransactions. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Export with oneOf schemas: ExportCustomer, ExportOrder, ExportPointsExpiration, ExportPublication, ExportRedemption, ExportVoucher, ExportVoucherTransactions. Details: " + ", ".join(error_messages))
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


