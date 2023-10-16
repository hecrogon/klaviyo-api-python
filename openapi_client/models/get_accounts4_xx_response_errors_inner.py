# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2023-10-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.get_accounts4_xx_response_errors_inner_source import GetAccounts4XXResponseErrorsInnerSource

class GetAccounts4XXResponseErrorsInner(BaseModel):
    """
    GetAccounts4XXResponseErrorsInner
    """
    id: StrictStr = Field(...)
    code: StrictStr = Field(...)
    title: StrictStr = Field(...)
    detail: StrictStr = Field(...)
    source: Optional[GetAccounts4XXResponseErrorsInnerSource] = None
    __properties = ["id", "code", "title", "detail", "source"]

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
    def from_json(cls, json_str: str) -> GetAccounts4XXResponseErrorsInner:
        """Create an instance of GetAccounts4XXResponseErrorsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetAccounts4XXResponseErrorsInner:
        """Create an instance of GetAccounts4XXResponseErrorsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetAccounts4XXResponseErrorsInner.parse_obj(obj)

        _obj = GetAccounts4XXResponseErrorsInner.parse_obj({
            "id": obj.get("id"),
            "code": obj.get("code"),
            "title": obj.get("title"),
            "detail": obj.get("detail"),
            "source": GetAccounts4XXResponseErrorsInnerSource.from_dict(obj.get("source")) if obj.get("source") is not None else None
        })
        return _obj


