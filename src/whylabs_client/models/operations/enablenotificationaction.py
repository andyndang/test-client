"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata


@dataclasses.dataclass
class EnableNotificationActionRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    action_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'action_id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class EnableNotificationActionResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    

