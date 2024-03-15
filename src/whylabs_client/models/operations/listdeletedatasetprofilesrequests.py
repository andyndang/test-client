"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import deleteprofile as components_deleteprofile
from ...models.components import httpmetadata as components_httpmetadata
from typing import List, Optional


@dataclasses.dataclass
class ListDeleteDatasetProfilesRequestsRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    r"""Your company's unique organization ID"""
    



@dataclasses.dataclass
class ListDeleteDatasetProfilesRequestsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    delete_profiles: Optional[List[components_deleteprofile.DeleteProfile]] = dataclasses.field(default=None)
    r"""The list of \[DeleteProfile\] requests if operation succeeds"""
    
