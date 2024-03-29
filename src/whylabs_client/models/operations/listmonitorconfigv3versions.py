"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import monitorconfigversion as components_monitorconfigversion
from typing import List, Optional


@dataclasses.dataclass
class ListMonitorConfigV3VersionsRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'dataset_id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class ListMonitorConfigV3VersionsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    monitor_config_versions: Optional[List[components_monitorconfigversion.MonitorConfigVersion]] = dataclasses.field(default=None)
    r"""ListMonitorConfigV3Versions 200 response"""
    

