"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import referenceprofileitemresponse as components_referenceprofileitemresponse
from typing import List, Optional


@dataclasses.dataclass
class ListReferenceProfilesRequest:
    UNSET='__SPEAKEASY_UNSET__'
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    r"""Your company's unique organization ID"""
    model_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'model_id', 'style': 'simple', 'explode': False }})
    r"""The unique model ID in your company."""
    from_epoch: Optional[int] = dataclasses.field(default=UNSET, metadata={'query_param': { 'field_name': 'from_epoch', 'style': 'form', 'explode': True }})
    r"""Milli epoch time that represents the end of the time range to query based on the upload timestamp."""
    to_epoch: Optional[int] = dataclasses.field(default=UNSET, metadata={'query_param': { 'field_name': 'to_epoch', 'style': 'form', 'explode': True }})
    r"""Milli epoch time that represents the end of the time range to query based on the upload timestamp."""
    



@dataclasses.dataclass
class ListReferenceProfilesResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    reference_profile_item_responses: Optional[List[components_referenceprofileitemresponse.ReferenceProfileItemResponse]] = dataclasses.field(default=None)
    r"""The metadata for the summarized dataset profile including paths to JSON and protobuf data"""
    

