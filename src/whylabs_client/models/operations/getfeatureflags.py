"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import featureflags as components_featureflags
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class GetFeatureFlagsRequest:
    user_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'user_id', 'style': 'form', 'explode': True }})
    org_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'org_id', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class GetFeatureFlagsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    feature_flags: Optional[components_featureflags.FeatureFlags] = dataclasses.field(default=None)
    r"""GetFeatureFlags 200 response"""
    

