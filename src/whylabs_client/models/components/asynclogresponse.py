"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .segmenttag import SegmentTag
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional
from whylabs_client import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Tags:
    tags: List[SegmentTag] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AsyncLogResponse:
    r"""Response payload for LogAsync."""
    UNSET='__SPEAKEASY_UNSET__'
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    model_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelId') }})
    upload_timestamp: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uploadTimestamp') }})
    upload_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uploadUrl') }})
    tags: Optional[Tags] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is AsyncLogResponse.UNSET }})
    

