"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from whylabs_client import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpdateAccountUserRequest:
    r"""Request to update a user in an account"""
    UNSET='__SPEAKEASY_UNSET__'
    external_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('externalId'), 'exclude': lambda f: f is UpdateAccountUserRequest.UNSET }})
    r"""The external id the user is known by in the provisioner"""
    user_schema: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('userSchema'), 'exclude': lambda f: f is UpdateAccountUserRequest.UNSET }})
    active: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('active'), 'exclude': lambda f: f is UpdateAccountUserRequest.UNSET }})
    
