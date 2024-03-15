"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import columnschema as components_columnschema
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import response as components_response
from typing import Optional


@dataclasses.dataclass
class PutEntitySchemaColumnRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'dataset_id', 'style': 'simple', 'explode': False }})
    column_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'column_id', 'style': 'simple', 'explode': False }})
    column_schema: components_columnschema.ColumnSchema = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class PutEntitySchemaColumnResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    response: Optional[components_response.Response] = dataclasses.field(default=None)
    r"""PutEntitySchemaColumn 200 response"""
    
