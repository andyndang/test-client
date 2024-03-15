"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .subscriptionproductsummary import SubscriptionProductSummary
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from whylabs_client import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubscriptionSummary:
    r"""Summary of a subscription"""
    UNSET='__SPEAKEASY_UNSET__'
    org_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orgId') }})
    subscription_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subscriptionId') }})
    status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    product: SubscriptionProductSummary = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('product') }})
    r"""Summary of a subscription product"""
    billing_interval: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billingInterval') }})
    created: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created') }})
    current_period_end: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currentPeriodEnd') }})
    cancelled_at_period_end: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cancelledAtPeriodEnd') }})
    cancelled_at: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cancelledAt'), 'exclude': lambda f: f is SubscriptionSummary.UNSET }})
    
