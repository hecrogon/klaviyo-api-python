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
from openapi_client.model.get_catalog_items4_xx_response import GetCatalogItems4XXResponse
from openapi_client.model.metric_aggregate_query import MetricAggregateQuery


class MetricsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_metric_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'Klaviyo-API-Key'
                ],
                'endpoint_path': '/api/metrics/{id}/',
                'operation_id': 'get_metric',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'fields_metric',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                    'fields_metric',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('fields_metric',): {

                        "NAME": "name",
                        "CREATED": "created",
                        "UPDATED": "updated",
                        "INTEGRATION": "integration"
                    },
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'fields_metric':
                        ([str],),
                },
                'attribute_map': {
                    'id': 'id',
                    'fields_metric': 'fields[metric]',
                },
                'location_map': {
                    'id': 'path',
                    'fields_metric': 'query',
                },
                'collection_format_map': {
                    'fields_metric': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_metrics_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'Klaviyo-API-Key'
                ],
                'endpoint_path': '/api/metrics/',
                'operation_id': 'get_metrics',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'fields_metric',
                    'filter',
                    'page_cursor',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'fields_metric',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('fields_metric',): {

                        "NAME": "name",
                        "CREATED": "created",
                        "UPDATED": "updated",
                        "INTEGRATION": "integration"
                    },
                },
                'openapi_types': {
                    'fields_metric':
                        ([str],),
                    'filter':
                        (str,),
                    'page_cursor':
                        (str,),
                },
                'attribute_map': {
                    'fields_metric': 'fields[metric]',
                    'filter': 'filter',
                    'page_cursor': 'page[cursor]',
                },
                'location_map': {
                    'fields_metric': 'query',
                    'filter': 'query',
                    'page_cursor': 'query',
                },
                'collection_format_map': {
                    'fields_metric': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.query_metric_aggregates_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'Klaviyo-API-Key'
                ],
                'endpoint_path': '/api/metric-aggregates/',
                'operation_id': 'query_metric_aggregates',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'metric_aggregate_query',
                ],
                'required': [
                    'metric_aggregate_query',
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
                    'metric_aggregate_query':
                        (MetricAggregateQuery,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'metric_aggregate_query': 'body',
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

    def get_metric(
        self,
        id,
        **kwargs
    ):
        """Get Metric  # noqa: E501

        Get a metric with the given metric ID. Request specific fields using [sparse fieldsets](https://developers.klaviyo.com/en/v2022-10-17/reference/api_overview#sparse-fieldsets)<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `Metrics Read`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_metric(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): Metric ID

        Keyword Args:
            fields_metric ([str]): For more information please visit https://developers.klaviyo.com/en/v2023-01-24/reference/api-overview#sparse-fieldsets. [optional]
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
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
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
        kwargs['id'] = \
            id
        return self.get_metric_endpoint.call_with_http_info(**kwargs)

    def get_metrics(
        self,
        **kwargs
    ):
        """Get Metrics  # noqa: E501

        Get all metrics in an account. Requests can be filtered by the following fields: integration `name`, integration `category` Request specific fields using [sparse fieldsets](https://developers.klaviyo.com/en/v2022-10-17/reference/api_overview#sparse-fieldsets). Returns a maximum of 200 results per page, which can be paginated with [cursor-based pagination](https://developers.klaviyo.com/en/v2022-10-17/reference/api_overview#pagination)<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `Metrics Read`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_metrics(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            fields_metric ([str]): For more information please visit https://developers.klaviyo.com/en/v2023-01-24/reference/api-overview#sparse-fieldsets. [optional]
            filter (str): For more information please visit https://developers.klaviyo.com/en/v2023-01-24/reference/api-overview#filtering<br>Allowed field(s)/operator(s):<br>`integration.name`: `equals`<br>`integration.category`: `equals`. [optional]
            page_cursor (str): For more information please visit https://developers.klaviyo.com/en/v2023-01-24/reference/api-overview#pagination. [optional]
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
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
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
        return self.get_metrics_endpoint.call_with_http_info(**kwargs)

    def query_metric_aggregates(
        self,
        metric_aggregate_query,
        **kwargs
    ):
        """Query Metric Aggregates  # noqa: E501

        Query and aggregate event data associated with a metric, including native Klaviyo metrics, integration-specific metrics, and custom events. Queries must be passed in the JSON body of your `POST` request.  Results can be filtered and grouped by time, event, or profile dimensions.  **Request body parameters** (nested under `attributes`):  * `return_fields`: request specific fields using [sparse fieldsets](https://developers.klaviyo.com/en/v2022-10-17/reference/api_overview#sparse-fieldsets) * `sort`: sort results by a specified field, such as `\"-timestamp\"` * `page_cursor`: results can be paginated with [cursor-based pagination](https://developers.klaviyo.com/en/v2022-10-17/reference/api_overview#pagination) * `page_size`: limit the number of returned results per page * `by`: optional attributes used to group by the aggregation function     * When using `by` attributes, an empty `dimensions` response is expected when the counts for the events do not have the associated dimension requested by the set `by` attribute. For example, a query including `\"by\": [\"$flow\"]` will return an empty dimensions response for counts of metrics not associated with a `$flow` * `measurement`: the measurement key supports the following values:     * `\"sum_value\"`: perform a summation of the `_Event Value_`, optionally partitioned over any dimension provided in the `by` field     * `\"count\"`: counts the number of events associated to a metric, optionally partitioned over any dimension provided in the `by` field     * `\"unique\"` counts the number of unique customers associated to a metric, optionally partitioned over any dimension provided in the `by` field * `interval`: aggregation interval, such as `\"hour\"`,`\"day\"`,`\"week\"`, and `\"month\"` * `metric_id`: the metric ID used in the aggregation * `filter`: list of filters for specific fields, must include time range using ISO 8601 format (`\"YYYY-MM-DDTHH:MM:SS.mmmmmm\"`)     * The time range can be filtered by providing a `greater_or_equal` filter on the datetime field, such as `\"greater-or-equal(datetime,2021-07-01T00:00:00)\"` and a `less-than` filter on the same datetime field, such as `\"less-than(datetime,2022-07-01T00:00:00)\"`     * The time range may span a maximum of one year. Time range dates may be set to a maximum of 5 years prior to the current date     * Filter the list of supported aggregate dimensions using the common filter syntax, such as `\"equals(URL,\\\"https://www.klaviyo.com/\\\")\"` * `timezone`: the timezone used when processing the query. Case sensitive. This field is validated against a list of common timezones from the [IANA Time Zone Database](https://www.iana.org/time-zones)  For a comprehensive list of native Klaviyo metrics and their associated attributes for grouping and filtering, please refer to the [metrics attributes guide](https://developers.klaviyo.com/en/v2022-10-17/docs/supported_metrics_and_attributes).<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `Metrics Read`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.query_metric_aggregates(metric_aggregate_query, async_req=True)
        >>> result = thread.get()

        Args:
            metric_aggregate_query (MetricAggregateQuery): Retrieve Metric Aggregations

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
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
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
        kwargs['metric_aggregate_query'] = \
            metric_aggregate_query
        return self.query_metric_aggregates_endpoint.call_with_http_info(**kwargs)

