"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from whylabs_client import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Session:
    r"""Information about a session"""
    session_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sessionId') }})
    r"""The id of the session"""
    org_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orgId') }})
    r"""The org id of the session"""
    model_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelId') }})
    r"""The model id of the session. There should only be a single model."""
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userId') }})
    r"""The generated user id for the session."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetSessionResponse:
    r"""Response for getting sessions."""
    session: Session = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('session') }})
    

