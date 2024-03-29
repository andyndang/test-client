"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import deleteanalyzerresult as components_deleteanalyzerresult
from ...models.components import httpmetadata as components_httpmetadata
from typing import List, Optional


@dataclasses.dataclass
class ListDeleteAnalyzerResultsRequestsRequest:
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    r"""Your company's unique organization ID"""
    



@dataclasses.dataclass
class ListDeleteAnalyzerResultsRequestsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    delete_analyzer_results: Optional[List[components_deleteanalyzerresult.DeleteAnalyzerResult]] = dataclasses.field(default=None)
    r"""The list of \[DeleteAnalyzerResult\] requests if operation succeeds"""
    

