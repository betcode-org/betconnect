from .baseendpoint import BaseEndpoint
from betconnect import resources

class Account(BaseEndpoint):

    _METHOD_URIS = {
        'get_balance': 'api/v2/get_balance'
    }

    def active_bookmakers(self):
        method_uri = self._METHOD_URIS['get_balance']

        (response, response_json, elapsed_time) = self.request(method_uri=method_uri, params={})

        return self.process_response(
            response=response,
            response_json=response_json,
            resource=resources.ActiveSports,
            elapsed_time=elapsed_time
        )


