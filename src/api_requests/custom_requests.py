from requests import request

class APIRequest:
    """
    """

    def get(self, url, headers, payload):
        """
        """
        response = request(method="GET", url=url, headers=headers, data=payload)

        return response
    
    def post(self, url, headers, payload):
        """
        """
        response = request(method="POST", url=url, headers=headers, data=payload)

        return response
    
    def put(self, url, headers, payload):
        """
        """
        response = request(method="PUT", url=url, headers=headers, data=payload)

        return response
    
    
