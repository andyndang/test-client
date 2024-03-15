"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import response as components_response
from typing import Optional


@dataclasses.dataclass
class DeleteEntitySchemaMetricRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'dataset_id', 'style': 'simple', 'explode': False }})
    metric_label: str = dataclasses.field(metadata={'path_param': { 'field_name': 'metric_label', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class DeleteEntitySchemaMetricResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    response: Optional[components_response.Response] = dataclasses.field(default=None)
    r"""DeleteEntitySchemaMetric 200 response"""
    
