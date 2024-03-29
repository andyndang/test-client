"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from whylabs_client import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class User:
    r"""User metadata"""
    UNSET='__SPEAKEASY_UNSET__'
    user_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userId') }})
    r"""The id of the user."""
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""The user's email address."""
    preferences: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('preferences'), 'exclude': lambda f: f is User.UNSET }})
    r"""The user's JSON serialized preferences. Schema defined in Dashbird."""
    

