"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import organizationsummary as components_organizationsummary
from enum import Enum
from typing import Optional

class PartiallyUpdateOrganizationQueryParamSubscriptionTier(str, Enum):
    r"""Organization's subscription tier. Should be PAID for real customers"""
    FREE = 'FREE'
    PAID = 'PAID'
    AWS_MARKETPLACE = 'AWS_MARKETPLACE'
    SUBSCRIPTION = 'SUBSCRIPTION'


@dataclasses.dataclass
class PartiallyUpdateOrganizationRequest:
    UNSET='__SPEAKEASY_UNSET__'
    org_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'org_id', 'style': 'simple', 'explode': False }})
    r"""The unique ID of an organization. If an organization with this ID does not exist, this method will throw an exception."""
    name: Optional[str] = dataclasses.field(default=UNSET, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    r"""The name of the organization"""
    subscription_tier: Optional[PartiallyUpdateOrganizationQueryParamSubscriptionTier] = dataclasses.field(default=UNSET, metadata={'query_param': { 'field_name': 'subscription_tier', 'style': 'form', 'explode': True }})
    r"""Organization's subscription tier. Should be PAID for real customers"""
    email_domains: Optional[str] = dataclasses.field(default=UNSET, metadata={'query_param': { 'field_name': 'email_domains', 'style': 'form', 'explode': True }})
    r"""Email domains associated with this organization, as a comma separated list"""
    observatory_url: Optional[str] = dataclasses.field(default=UNSET, metadata={'query_param': { 'field_name': 'observatory_url', 'style': 'form', 'explode': True }})
    r"""Url that users of this organization will be redirected to in some cases (such as via Siren notifications). NOTE: should NOT be followed by a trailing slash!"""
    parent_org_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'query_param': { 'field_name': 'parent_org_id', 'style': 'form', 'explode': True }})
    storage_bucket_override: Optional[str] = dataclasses.field(default=UNSET, metadata={'query_param': { 'field_name': 'storage_bucket_override', 'style': 'form', 'explode': True }})
    allow_managed_membership_updates_only: Optional[bool] = dataclasses.field(default=UNSET, metadata={'query_param': { 'field_name': 'allow_managed_membership_updates_only', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class PartiallyUpdateOrganizationResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    organization_summary: Optional[components_organizationsummary.OrganizationSummary] = dataclasses.field(default=None)
    r"""A summary of the organization object if succeeds"""
    

