"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import entityschema as components_entityschema
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class GetEntitySchemaRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'dataset_id', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetEntitySchemaResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    entity_schema: Optional[components_entityschema.EntitySchema] = dataclasses.field(default=None)
    r"""GetEntitySchema 200 response"""
    
