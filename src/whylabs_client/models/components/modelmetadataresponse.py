"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from whylabs_client import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ModelMetadataResponse:
    r"""Response for the model metadata"""
    UNSET='__SPEAKEASY_UNSET__'
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    org_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orgId') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    creation_time: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creationTime') }})
    time_period: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timePeriod') }})
    model_category: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelCategory') }})
    model_type: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelType'), 'exclude': lambda f: f is ModelMetadataResponse.UNSET }})
    active: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('active'), 'exclude': lambda f: f is ModelMetadataResponse.UNSET }})
    

