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
import os

class CreateTicket:
    """
    """
    def __init__(self) -> None:
        self.jira = InitJira.get_jira_instance()

    def create_tickets(self, stories, parent_ticket_id = None):
        """
        {
            "fields": {
                "project":
                {
                    "key": "KAN"
                },
                "parent":
                {
                    "key": "KAN-3"
                },
                "summary": "Child of KAN-3",
                "description": "I am child of KAN-3",
                "issuetype": {
                    "name": "Story"
                }
            }
        }
        """

        field_list = self.get_field_list(
            stories=stories,
            parent_ticket_id=parent_ticket_id
        )

        result = self.jira.create_issues(field_list=field_list)

        return result


    def get_field_list(self, stories, parent_ticket_id = None):

        project = {
            "key": os.getenv("JIRA_PROJECT_CODE")
        }
        if parent_ticket_id:
            parent = {
                "key": parent_ticket_id
            }

        ticket_list = []

        for story in stories:
            ticket = {
                "summary": story["title"],
                "description": story["description"],
                "issuetype": {
                    "name": "Story"
                }
            }

            ticket.update({"project": project})
            if parent_ticket_id:
                ticket.update({"parent": parent})

            ticket_list.append(
                 ticket
            )

        return ticket_list

