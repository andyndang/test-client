"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .modelmetadataresponse import ModelMetadataResponse
from dataclasses_json import Undefined, dataclass_json
from typing import List
from whylabs_client import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListModelsResponse:
    r"""Response for the ListModels API"""
    items: List[ModelMetadataResponse] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items') }})
    r"""A list of all known model ids for an organization."""
    
