"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import List
from whylabs_client import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetProfileObservatoryLinkRequest:
    r"""Get a url for viewing profiles in the observatory"""
    batch_profile_timestamps: List[int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batchProfileTimestamps') }})
    reference_profile_ids: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('referenceProfileIds') }})
    

