<!-- Start SDK Example Usage [usage] -->
```python
import whylabs_client
from whylabs_client.models import operations

s = whylabs_client.WhylabsClient(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.account.get_account_memberships(org_id='org-123', user_id='user-123', managed_org_id='org-123', role=operations.Role.VIEWER)

if res.get_account_memberships_response is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->