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
from .update_ticket import UpdateTicket
from jira_agent.ADF.issue_templates import IssueTemplateV2
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
        results = self.jira.create_issues(field_list=field_list)
        Logger.info(message="Created \"Story\" Type Tickets", stage="END")
        
        # Updating Teams
        for index, result in enumerate(results):
            UpdateTicket().update_team(
                ticket_id=result["issue"].key,
                team=stories[index]["team"],
                labels=stories[index]["labels"],
                acceptance_criteria=stories[index]["acceptance_criteria"]
            )

        Logger.info(message=f"{len(stories)} Tickets Created Successfully")
        return results


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
            
            rich_text_desc = IssueTemplateV2.create_issue_description(
                story_desc=story.get("description", ""),
                in_scope=story.get("in_scope", []),
                out_scope=story.get("out_scope",[])
            )

            ticket = {
                "summary": story["title"],
                "description": rich_text_desc,
                "issuetype": {
                    "name": "Story"
                }
                # "labels": story["labels"]
            }

            ticket.update({"project": project})
            if parent_ticket_id:
                ticket.update({"parent": parent})

            ticket_list.append(
                 ticket
            )

        return ticket_list