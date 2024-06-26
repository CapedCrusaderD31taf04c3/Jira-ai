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

from jira import JIRA
import os

class InitJira:
    """
    """
    JIRA.DEFAULT_OPTIONS["rest_api_version"] = "3"
    jira = JIRA(
        os.getenv("JIRA_DOMAIN"),
        basic_auth=(
            os.getenv("JIRA_EMAIL"), 
            os.getenv("JIRA_PAT_TOKEN")
        )
    )

    @classmethod
    def get_jira_instance(cls):
        """
        """

        return cls.jira
