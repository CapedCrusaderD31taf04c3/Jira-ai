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


class UpdateTicket:
    """
    """
    def __init__(self) -> None:
        self.jira = InitJira.get_jira_instance()

    def update_rca(self, ticket_id, rca):
        """
        """
        Logger.info(message=f"Updating RCA on {ticket_id}", stage="START")
        issue = self.jira.issue(ticket_id)
        issue.update(
            fields={
                "customfield_10033": rca
                }
        )
        Logger.info(message=f"Updated RCA in {ticket_id}", stage="END")
        return True
    
    def update_team(self, ticket_id, team):
        """
        """
        issue = self.jira.issue(ticket_id)
        issue.update(
            fields={
                "customfield_10001": team
                }
        )
        Logger.info(message=f"Updated Team in ticket: {ticket_id}")
        return True