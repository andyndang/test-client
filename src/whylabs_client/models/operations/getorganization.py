"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import organizationmetadata as components_organizationmetadata
from typing import Optional


@dataclasses.dataclass
class GetOrganizationRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    r"""The unique ID of an organization"""
    



@dataclasses.dataclass
class GetOrganizationResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    organization_metadata: Optional[components_organizationmetadata.OrganizationMetadata] = dataclasses.field(default=None)
    r"""The organization metadata"""
    

