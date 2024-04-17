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

import requests
import os

class PRCreator:
    """
    """

    def __init__(self, title, body, head_branch):
        """
        """

        self.title = title
        self.body = body
        self.head_branch = head_branch
  
    @classmethod
    def prepare_url(cls):
        """
        """

        url = (
            "https://api.github.com/"
            f"repos/{os.getenv('REPO_OWNER')}/"
            f"{os.getenv('REPO_NAME')}/pulls"
        )

        return url

    def prepare_payload(self) -> str:
        """
        """

        payload = {
            "title": self.title,
            "body": self.body,
            "head": self.head_branch,
            "base": os.getenv("DEFAULT_BRANCH")
        }

        return str(payload)
    
    @classmethod
    def prepare_headers(cls):
        """
        """

        headers = {
          'Accept': 'application/vnd.github+json',
          'Authorization': f'Bearer {os.getenv("GITHUB_TOKEN")}',
          'X-GitHub-Api-Version': '2022-11-28',
          'Content-Type': 'application/x-www-form-urlencoded'
        }

        return headers

    def create_pull_request(self):
        """
        """

        response = requests.request(
            "POST", 
            url=self.prepare_url(), 
            headers=self.prepare_headers(),
            data=self.prepare_payload()
        )

        return response
