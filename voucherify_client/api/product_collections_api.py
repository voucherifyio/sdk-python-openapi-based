# coding: utf-8

"""
    Voucherify API

    Voucherify promotion engine REST API. Please see https://docs.voucherify.io/docs for more details.

    The version of the OpenAPI document: v2018-08-01
    Contact: support@voucherify.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from datetime import datetime

from pydantic import Field, StrictStr, conint

from typing import Optional

from voucherify_client.models.parameter_order import ParameterOrder
from voucherify_client.models.product_collections_create_request_body import ProductCollectionsCreateRequestBody
from voucherify_client.models.product_collections_create_response_body import ProductCollectionsCreateResponseBody
from voucherify_client.models.product_collections_get_response_body import ProductCollectionsGetResponseBody
from voucherify_client.models.product_collections_list_response_body import ProductCollectionsListResponseBody
from voucherify_client.models.product_collections_products_list_response_body import ProductCollectionsProductsListResponseBody

from voucherify_client.api_client import ApiClient
from voucherify_client.api_response import ApiResponse
from voucherify_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ProductCollectionsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_product_collection(self, product_collections_create_request_body : Optional[ProductCollectionsCreateRequestBody] = None, **kwargs) -> ProductCollectionsCreateResponseBody:  # noqa: E501
        """Create Product Collection  # noqa: E501

        This method creates a new product collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_product_collection(product_collections_create_request_body, async_req=True)
        >>> result = thread.get()

        :param product_collections_create_request_body:
        :type product_collections_create_request_body: ProductCollectionsCreateRequestBody
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ProductCollectionsCreateResponseBody
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_product_collection_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.create_product_collection_with_http_info(product_collections_create_request_body, **kwargs)  # noqa: E501

    @validate_arguments
    def create_product_collection_with_http_info(self, product_collections_create_request_body : Optional[ProductCollectionsCreateRequestBody] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Create Product Collection  # noqa: E501

        This method creates a new product collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_product_collection_with_http_info(product_collections_create_request_body, async_req=True)
        >>> result = thread.get()

        :param product_collections_create_request_body:
        :type product_collections_create_request_body: ProductCollectionsCreateRequestBody
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ProductCollectionsCreateResponseBody, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'product_collections_create_request_body'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_product_collection" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['product_collections_create_request_body'] is not None:
            _body_params = _params['product_collections_create_request_body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['X-App-Id', 'X-App-Token']  # noqa: E501

        _response_types_map = {
            '200': "ProductCollectionsCreateResponseBody",
        }

        return self.api_client.call_api(
            '/v1/product-collections', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def delete_product_collection(self, product_collection_id : Annotated[StrictStr, Field(..., description="A unique product collection ID.")], **kwargs) -> None:  # noqa: E501
        """Delete Product Collection  # noqa: E501

        This method deletes a product collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_product_collection(product_collection_id, async_req=True)
        >>> result = thread.get()

        :param product_collection_id: A unique product collection ID. (required)
        :type product_collection_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the delete_product_collection_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.delete_product_collection_with_http_info(product_collection_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_product_collection_with_http_info(self, product_collection_id : Annotated[StrictStr, Field(..., description="A unique product collection ID.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Delete Product Collection  # noqa: E501

        This method deletes a product collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_product_collection_with_http_info(product_collection_id, async_req=True)
        >>> result = thread.get()

        :param product_collection_id: A unique product collection ID. (required)
        :type product_collection_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'product_collection_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_product_collection" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['product_collection_id']:
            _path_params['productCollectionId'] = _params['product_collection_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ['X-App-Id', 'X-App-Token']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/v1/product-collections/{productCollectionId}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_product_collection(self, product_collection_id : Annotated[StrictStr, Field(..., description="A unique product collection ID.")], **kwargs) -> ProductCollectionsGetResponseBody:  # noqa: E501
        """Get Product Collection  # noqa: E501

        Retrieves the product collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_product_collection(product_collection_id, async_req=True)
        >>> result = thread.get()

        :param product_collection_id: A unique product collection ID. (required)
        :type product_collection_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ProductCollectionsGetResponseBody
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_product_collection_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_product_collection_with_http_info(product_collection_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_product_collection_with_http_info(self, product_collection_id : Annotated[StrictStr, Field(..., description="A unique product collection ID.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get Product Collection  # noqa: E501

        Retrieves the product collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_product_collection_with_http_info(product_collection_id, async_req=True)
        >>> result = thread.get()

        :param product_collection_id: A unique product collection ID. (required)
        :type product_collection_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ProductCollectionsGetResponseBody, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'product_collection_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product_collection" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['product_collection_id']:
            _path_params['productCollectionId'] = _params['product_collection_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['X-App-Id', 'X-App-Token']  # noqa: E501

        _response_types_map = {
            '200': "ProductCollectionsGetResponseBody",
        }

        return self.api_client.call_api(
            '/v1/product-collections/{productCollectionId}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def list_product_collections(self, limit : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items.")] = None, page : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Which page of results to return. The lowest value is 1.")] = None, order : Annotated[Optional[ParameterOrder], Field(description="Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order.")] = None, **kwargs) -> ProductCollectionsListResponseBody:  # noqa: E501
        """List Product Collections  # noqa: E501

        This method returns a list of product collections.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_product_collections(limit, page, order, async_req=True)
        >>> result = thread.get()

        :param limit: Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items.
        :type limit: int
        :param page: Which page of results to return. The lowest value is 1.
        :type page: int
        :param order: Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order.
        :type order: ParameterOrder
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ProductCollectionsListResponseBody
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_product_collections_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.list_product_collections_with_http_info(limit, page, order, **kwargs)  # noqa: E501

    @validate_arguments
    def list_product_collections_with_http_info(self, limit : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items.")] = None, page : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Which page of results to return. The lowest value is 1.")] = None, order : Annotated[Optional[ParameterOrder], Field(description="Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List Product Collections  # noqa: E501

        This method returns a list of product collections.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_product_collections_with_http_info(limit, page, order, async_req=True)
        >>> result = thread.get()

        :param limit: Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items.
        :type limit: int
        :param page: Which page of results to return. The lowest value is 1.
        :type page: int
        :param order: Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order.
        :type order: ParameterOrder
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ProductCollectionsListResponseBody, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'limit',
            'page',
            'order'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_product_collections" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('page', _params['page']))

        if _params.get('order') is not None:  # noqa: E501
            _query_params.append(('order', _params['order'].value))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['X-App-Id', 'X-App-Token']  # noqa: E501

        _response_types_map = {
            '200': "ProductCollectionsListResponseBody",
        }

        return self.api_client.call_api(
            '/v1/product-collections', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def list_products_in_collection(self, product_collection_id : Annotated[StrictStr, Field(..., description="Unique product collection ID.")], limit : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items.")] = None, page : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Which page of results to return. The lowest value is 1.")] = None, order : Annotated[Optional[ParameterOrder], Field(description="Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order.")] = None, starting_after : Annotated[Optional[datetime], Field(description="Timestamp representing the date and time to use in starting_after cursor to get more data. Represented in ISO 8601 format.")] = None, **kwargs) -> ProductCollectionsProductsListResponseBody:  # noqa: E501
        """List Products in Collection  # noqa: E501

        Retrieves list of products from a product collection; works for both dynamic and static product collections.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_products_in_collection(product_collection_id, limit, page, order, starting_after, async_req=True)
        >>> result = thread.get()

        :param product_collection_id: Unique product collection ID. (required)
        :type product_collection_id: str
        :param limit: Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items.
        :type limit: int
        :param page: Which page of results to return. The lowest value is 1.
        :type page: int
        :param order: Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order.
        :type order: ParameterOrder
        :param starting_after: Timestamp representing the date and time to use in starting_after cursor to get more data. Represented in ISO 8601 format.
        :type starting_after: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ProductCollectionsProductsListResponseBody
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_products_in_collection_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.list_products_in_collection_with_http_info(product_collection_id, limit, page, order, starting_after, **kwargs)  # noqa: E501

    @validate_arguments
    def list_products_in_collection_with_http_info(self, product_collection_id : Annotated[StrictStr, Field(..., description="Unique product collection ID.")], limit : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items.")] = None, page : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Which page of results to return. The lowest value is 1.")] = None, order : Annotated[Optional[ParameterOrder], Field(description="Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order.")] = None, starting_after : Annotated[Optional[datetime], Field(description="Timestamp representing the date and time to use in starting_after cursor to get more data. Represented in ISO 8601 format.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List Products in Collection  # noqa: E501

        Retrieves list of products from a product collection; works for both dynamic and static product collections.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_products_in_collection_with_http_info(product_collection_id, limit, page, order, starting_after, async_req=True)
        >>> result = thread.get()

        :param product_collection_id: Unique product collection ID. (required)
        :type product_collection_id: str
        :param limit: Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items.
        :type limit: int
        :param page: Which page of results to return. The lowest value is 1.
        :type page: int
        :param order: Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order.
        :type order: ParameterOrder
        :param starting_after: Timestamp representing the date and time to use in starting_after cursor to get more data. Represented in ISO 8601 format.
        :type starting_after: datetime
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ProductCollectionsProductsListResponseBody, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'product_collection_id',
            'limit',
            'page',
            'order',
            'starting_after'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_products_in_collection" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['product_collection_id']:
            _path_params['productCollectionId'] = _params['product_collection_id']


        # process the query parameters
        _query_params = []
        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('page', _params['page']))

        if _params.get('order') is not None:  # noqa: E501
            _query_params.append(('order', _params['order'].value))

        if _params.get('starting_after') is not None:  # noqa: E501
            if isinstance(_params['starting_after'], datetime):
                _query_params.append(('starting_after', _params['starting_after'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('starting_after', _params['starting_after']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['X-App-Id', 'X-App-Token']  # noqa: E501

        _response_types_map = {
            '200': "ProductCollectionsProductsListResponseBody",
        }

        return self.api_client.call_api(
            '/v1/product-collections/{productCollectionId}/products', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
