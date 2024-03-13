import requests
import json
from .custom_requests import APIRequest
import os

class PostCommentAPI(APIRequest):
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


        return response.text