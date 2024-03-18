# Copyright (C) 2024 CapedCrusaderD31taf04c3 <https://github.com/CapedCrusaderD31taf04c3>

# This program is not a free software: you can not redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# =========================================================================================

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