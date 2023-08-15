# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.  # noqa: E501

    The version of the OpenAPI document: 2023-08-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class CatalogItemEnum(str, Enum):
    """
    CatalogItemEnum
    """

    """
    allowed enum values
    """
    CATALOG_MINUS_ITEM = 'catalog-item'

    @classmethod
    def from_json(cls, json_str: str) -> CatalogItemEnum:
        """Create an instance of CatalogItemEnum from a JSON string"""
        return CatalogItemEnum(json.loads(json_str))


