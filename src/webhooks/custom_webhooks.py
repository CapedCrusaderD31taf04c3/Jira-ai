# Copyright (c) 2024 CapedCrusader
# All rights reserved.
#
# This software is licensed under the terms of the MIT.
# You should have received a copy of the license along with this
# program. If not, see LICENSE File.
# 
# ======================================

from requests import request

class Webhook:
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
    
    
