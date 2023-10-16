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


from typing import Any, Dict
from pydantic import BaseModel, Field

class TemplateRenderQueryResourceObjectAttributes(BaseModel):
    """
    TemplateRenderQueryResourceObjectAttributes
    """
    context: Dict[str, Any] = Field(..., description="The context for the template render. This must be a JSON object which has values for any tags used in the template. See [this doc](https://help.klaviyo.com/hc/en-us/articles/4408802648731) for more details.")
    __properties = ["context"]

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
    def from_json(cls, json_str: str) -> TemplateRenderQueryResourceObjectAttributes:
        """Create an instance of TemplateRenderQueryResourceObjectAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TemplateRenderQueryResourceObjectAttributes:
        """Create an instance of TemplateRenderQueryResourceObjectAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TemplateRenderQueryResourceObjectAttributes.parse_obj(obj)

        _obj = TemplateRenderQueryResourceObjectAttributes.parse_obj({
            "context": obj.get("context")
        })
        return _obj


