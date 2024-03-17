from jira import JIRA
import os

class InitJira:
    """
    """
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


# issue = jira.issue('KAN-1')
# print(issue.fields.project.key)            # 'JRA'
# print(issue.fields.issuetype.name)         # 'New Feature'
# print(issue.fields.reporter.displayName)