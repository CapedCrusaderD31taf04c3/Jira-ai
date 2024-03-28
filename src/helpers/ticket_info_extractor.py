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

from logger.custom_logger import Logger

class TicketInfoExtractor:
    """
    """

    def __init__(self, ticket):
        """
        """

        Logger.info(message="Retrieving Ticket Information", stage="START")

        self.ticket_key = ticket.issue.get("key", None)
        self.ticket_summary = ticket.issue.get("fields", {}).get("summary", None)
        self.ticket_desc = ticket.issue.get("fields", {}).get("description", None)
        self.ticket_type = ticket.issue.get("fields", {}).get("issuetype", {}).get("namedValue", None)
        
        Logger.info(message="Retrieved Ticket Information", stage="END")