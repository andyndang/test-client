# CreateOrganizationRequest


## Fields

| Field                                                                                                    | Type                                                                                                     | Required                                                                                                 | Description                                                                                              | Example                                                                                                  |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                   | *str*                                                                                                    | :heavy_check_mark:                                                                                       | The name of the organization                                                                             | ACME, Inc                                                                                                |
| `subscription_tier`                                                                                      | [Optional[operations.QueryParamSubscriptionTier]](../../models/operations/queryparamsubscriptiontier.md) | :heavy_minus_sign:                                                                                       | Organization's subscription tier. Should be PAID for real customers                                      | FREE                                                                                                     |
| `email_domains`                                                                                          | *Optional[str]*                                                                                          | :heavy_minus_sign:                                                                                       | Email domains associated with this organization, as a comma separated list                               | acme.ai,acme.com                                                                                         |
| `override_id`                                                                                            | *Optional[str]*                                                                                          | :heavy_minus_sign:                                                                                       | Custom ID. If this ID is invalid this method will throw an exception                                     | org-123                                                                                                  |
| `observatory_url`                                                                                        | *Optional[str]*                                                                                          | :heavy_minus_sign:                                                                                       | N/A                                                                                                      | https://hub.whylabsapp.com                                                                               |
| `parent_org_id`                                                                                          | *Optional[str]*                                                                                          | :heavy_minus_sign:                                                                                       | N/A                                                                                                      | org-123                                                                                                  |
| `storage_bucket_override`                                                                                | *Optional[str]*                                                                                          | :heavy_minus_sign:                                                                                       | N/A                                                                                                      |                                                                                                          |
| `allow_managed_membership_updates_only`                                                                  | *Optional[bool]*                                                                                         | :heavy_minus_sign:                                                                                       | N/A                                                                                                      |                                                                                                          |