"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import List
from whylabs_client import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SegmentsListRequest:
    segments: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('segments') }})
    

