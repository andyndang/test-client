# CreateOrganizationMembershipRequest


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `org_id`                                           | *str*                                              | :heavy_check_mark:                                 | N/A                                                | org-123                                            |
| `email`                                            | *str*                                              | :heavy_check_mark:                                 | N/A                                                | user@whylabs.ai                                    |
| `role`                                             | [components.Role](../../models/components/role.md) | :heavy_check_mark:                                 | N/A                                                | admin                                              |
| `set_default`                                      | *Optional[bool]*                                   | :heavy_minus_sign:                                 | N/A                                                |                                                    |