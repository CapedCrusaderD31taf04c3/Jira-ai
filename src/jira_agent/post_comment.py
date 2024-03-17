from .jira_main import InitJira


class PostComment:
    """
    """
    def __init__(self) -> None:
        self.jira = InitJira.get_jira_instance()

    def post_comment(self, ticket_id, comment):
        response = self.jira.add_comment(
            issue=ticket_id,
            body=comment
        )

        return response.__dict__

    