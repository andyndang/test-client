# GetAccountMembershipsRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `org_id`                                                     | *str*                                                        | :heavy_check_mark:                                           | N/A                                                          | org-123                                                      |
| `user_id`                                                    | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          | user-123                                                     |
| `managed_org_id`                                             | *Optional[str]*                                              | :heavy_minus_sign:                                           | N/A                                                          | org-123                                                      |
| `role`                                                       | [Optional[operations.Role]](../../models/operations/role.md) | :heavy_minus_sign:                                           | N/A                                                          | admin                                                        |