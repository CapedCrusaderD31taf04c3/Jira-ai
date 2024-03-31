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
import os
import json


class CreateTicket:
    """
    """
    def __init__(self) -> None:
        self.jira = InitJira.get_jira_instance()

    def create_tickets(self, stories_text, parent_ticket_id = None):
        """
        """
        
        Logger.info(message="Creating \"Story\" Type Tickets", stage="START")     
        stories = json.loads(stories_text)
        Logger.info(message=f"{len(stories)} Tickets will be created")    
        field_list = self.get_field_list(
            stories=stories,
            parent_ticket_id=parent_ticket_id
        )
        result = self.jira.create_issues(field_list=field_list)
        Logger.info(message="Created \"Story\" Type Tickets", stage="END")
        Logger.info(message=f"{len(stories)} Tickets Created Successfully")
        return result


    def get_field_list(self, stories, parent_ticket_id = None):
        """
        """
        
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
                "summary": story["story_title"],
                "description": story.get("description", ""),
                "issuetype": {
                    "name": "Story"
                },
                "labels": story["labels"]
                # "customfield_10001": story["team"]
            }

            ticket.update({"project": project})
            if parent_ticket_id:
                ticket.update({"parent": parent})

            ticket_list.append(
                 ticket
            )

        return ticket_list

