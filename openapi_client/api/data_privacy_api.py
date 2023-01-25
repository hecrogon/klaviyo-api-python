"""
    Klaviyo API

    The Klaviyo REST API. Please visit https://developers.klaviyo.com for more details.  # noqa: E501

    The version of the OpenAPI document: 2023-01-24
    Contact: developers@klaviyo.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.data_privacy_create_deletion_job_query import DataPrivacyCreateDeletionJobQuery
from openapi_client.model.get_catalog_items4_xx_response import GetCatalogItems4XXResponse


class DataPrivacyApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.request_profile_deletion_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Klaviyo-API-Key'
                ],
                'endpoint_path': '/api/data-privacy-deletion-jobs/',
                'operation_id': 'request_profile_deletion',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'data_privacy_create_deletion_job_query',
                ],
                'required': [
                    'data_privacy_create_deletion_job_query',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'data_privacy_create_deletion_job_query':
                        (DataPrivacyCreateDeletionJobQuery,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'data_privacy_create_deletion_job_query': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def request_profile_deletion(
        self,
        data_privacy_create_deletion_job_query,
        **kwargs
    ):
        """Request Profile Deletion  # noqa: E501

        Request a deletion for the profiles corresponding to one of the following identifiers: `email`, `phone_number`, or `profile_id`. If multiple identifiers are provided, we will return an error. All profiles that match the provided identifier will be deleted.         The deletion occurs asynchronously; however, once it has completed, the deleted profile will appear on the [Deleted Profiles page](https://www.klaviyo.com/account/deleted).         For more information on the deletion process, please refer to our [Help Center docs on how to handle GDPR and CCPA deletion requests](https://help.klaviyo.com/hc/en-us/articles/360004217631-How-to-Handle-GDPR-Requests#record-gdpr-and-ccpa%20%20-deletion-requests2).<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `Data Privacy Write`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.request_profile_deletion(data_privacy_create_deletion_job_query, async_req=True)
        >>> result = thread.get()

        Args:
            data_privacy_create_deletion_job_query (DataPrivacyCreateDeletionJobQuery):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['data_privacy_create_deletion_job_query'] = \
            data_privacy_create_deletion_job_query
        return self.request_profile_deletion_endpoint.call_with_http_info(**kwargs)

