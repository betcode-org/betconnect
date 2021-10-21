
from typing import Union, Optional

class RPError(Exception):

    """
        base exception class

    """


    pass

class APIError(RPError):
    """
    Exception raised if error is found.
    """

    def __init__(
        self,
        response: Optional[dict],
        uri: str = None,
        params: dict = None,
        exception: Exception = None,
    ):
        if response:
            error_data = response.get("error")
            message = (
                "%s \nParams: %s \nException: %s \nError: %s \nFull Response: %s"
                % (uri, params, exception, error_data, response)
            )
        else:
            message = "%s \nParams: %s \nException: %s" % (uri, params, exception)
        super(APIError, self).__init__(message)


class RequestException:

    def __init__(self,
                 response,
                 response_json,
                 elapsed_time
                 ):
        self.response = response
        self.response_json = response_json
        self.elapsed_time = elapsed_time
        self.errors = response_json.get('errors')

        return

