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

