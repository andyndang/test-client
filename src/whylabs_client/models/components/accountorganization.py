"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from whylabs_client import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AccountOrganization:
    r"""Response for the GetAccountMemberships API"""
    org_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orgId') }})
    r"""Organization ID"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Organization name"""
    

