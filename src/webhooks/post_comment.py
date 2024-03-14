# Copyright (c) 2024 CapedCrusader
# All rights reserved.
#
# This software is licensed under the terms of the MIT.
# You should have received a copy of the license along with this
# program. If not, see LICENSE File.
# 
# ======================================

import json
from .custom_webhooks import Webhook
import os

class PostCommentWBH(Webhook):
    """
    """

    def url(self, ticket_id):
        """
        """
        
        url = (
            f"{os.getenv('JIRA_DOMAIN')}"
            f"/rest/api/latest/issue/{ticket_id}/comment"
        )

        return url
    
    def headers(self):
        """
        """
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Basic {os.getenv('JIRA_TOKEN')}"
        }

        return headers
    
    def payload(self, comment):
        """
        """

        payload = json.dumps({
            "body": comment
        })

        return payload

    
    def post_comment(self, ticket_id, comment):
        """
        """

        response = self.post(
            url=self.url(ticket_id=ticket_id),
            headers=self.headers(),
            payload=self.payload(comment=comment)
        )

        if response.status_code == 201:
            return response.text
        else:
            return response.text