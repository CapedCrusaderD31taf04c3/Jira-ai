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

from .jira_main import InitJira
from logger.custom_logger import Logger

class PostComment:
    """
    """
    def __init__(self) -> None:
        """
        """
        self.jira = InitJira.get_jira_instance()

    def post_comment(self, ticket_id, comment):
        """
        """
        Logger.info(message=f"Commenting On {ticket_id}", stage="START")
        response = self.jira.add_comment(
            issue=ticket_id,
            body=comment
        )
        Logger.info(message=f"Commented to {ticket_id}", stage="END")
        return response.__dict__

    