# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.  # noqa: E501

    The version of the OpenAPI document: 2023-08-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel
from openapi_client.models.campaign_message_assign_template_query_resource_object_relationships_template import CampaignMessageAssignTemplateQueryResourceObjectRelationshipsTemplate

class CampaignMessageAssignTemplateQueryResourceObjectRelationships(BaseModel):
    """
    CampaignMessageAssignTemplateQueryResourceObjectRelationships
    """
    template: Optional[CampaignMessageAssignTemplateQueryResourceObjectRelationshipsTemplate] = None
    __properties = ["template"]

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
    def from_json(cls, json_str: str) -> CampaignMessageAssignTemplateQueryResourceObjectRelationships:
        """Create an instance of CampaignMessageAssignTemplateQueryResourceObjectRelationships from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of template
        if self.template:
            _dict['template'] = self.template.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CampaignMessageAssignTemplateQueryResourceObjectRelationships:
        """Create an instance of CampaignMessageAssignTemplateQueryResourceObjectRelationships from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CampaignMessageAssignTemplateQueryResourceObjectRelationships.parse_obj(obj)

        _obj = CampaignMessageAssignTemplateQueryResourceObjectRelationships.parse_obj({
            "template": CampaignMessageAssignTemplateQueryResourceObjectRelationshipsTemplate.from_dict(obj.get("template")) if obj.get("template") is not None else None
        })
        return _obj

