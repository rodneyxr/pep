from opa_client.opa import OpaClient


class MyOPAClient:
    """
    Wrapper around the OPA client to make it easier to use.
    """

    def __init__(self, opa_url="http://localhost:8181/v1/data/abac/allow"):
        self._client = OpaClient()
        self._opa_url = opa_url
        self.check_connection()
        # print(self._client.get_policies_list())

    def check_connection(self):
        self._client.check_connection()

    def request_access(self, user, document):
        # Create the authorization request
        request_data = {
            "input": {"user": user.to_dict(), "document": document.to_dict()}
        }
        # print(request_data)

        # Send the request to the OPA for evaluation
        result = self._client.check_permission(
            input_data=request_data, policy_name="policies/abac.rego", rule_name="allow"
        )["result"]
        return result
