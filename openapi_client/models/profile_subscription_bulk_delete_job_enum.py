# coding: utf-8

"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.

    The version of the OpenAPI document: 2023-10-15
    Contact: developers@klaviyo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ProfileSubscriptionBulkDeleteJobEnum(str, Enum):
    """
    ProfileSubscriptionBulkDeleteJobEnum
    """

    """
    allowed enum values
    """
    PROFILE_MINUS_SUBSCRIPTION_MINUS_BULK_MINUS_DELETE_MINUS_JOB = 'profile-subscription-bulk-delete-job'

    @classmethod
    def from_json(cls, json_str: str) -> ProfileSubscriptionBulkDeleteJobEnum:
        """Create an instance of ProfileSubscriptionBulkDeleteJobEnum from a JSON string"""
        return ProfileSubscriptionBulkDeleteJobEnum(json.loads(json_str))


