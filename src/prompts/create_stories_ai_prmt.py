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

class CreateStoriesOpenAIPMT:
    """
    """
    INPUT_PREPARATION  = """
        Here one big jira epic have to be divide into multiple jira stories with necessary data as given in examples, 
        there are total 7 teams, 
        T1-Security - PRO-DEV, PRO-DEV-SEC, 
        T2-Features - PRO-DEV,PRO-DEV-FEAT, 
        T3-Frontend - PRO-DEV,PRO-DEV-FRONT, 
        T4-BugFixers - PRO-DEV,PRO-DEV-BUGFIXERS, 
        T5-Testers - PRO-DEV,PRO-DEV-TEST, 
        T6-DevOps - PRO-DEV,PRO-DEV-DEVOPS, 
        T7-Release - PRO-DEV,PRO-DEV-RELAESE, PRO-DEV-LEAD
    """

    WORK_INSTRUCTION = """
        Each team holds labels and responsibility for their related topic, 
        there are multiple labels PRO-DEV, PRO-DEV-SEC, PRO-DEV-FEAT, PRO-DEV-FRONT, PRO-DEV-BUGFIXERS, PRO-DEV-TEST, PRO-DEV-DEVOPS, PRO-DEV-RELAESE, PRO-DEV-LEAD, 
        each story must have 1 team and few required labels,
    """

    OUTPUT_SPECIFICATION = """
        few examples are given below, provide only output with the output format list of dictionaries with only provided key names
    """

    OUPUT_EXAMPLES = """
    Q: Provide Feature to add unique users to list:This task involves implementing a feature to add unique users to a list. The feature entails generating unique identifiers for users and adding them to a database. Additionally, it requires writing test cases to ensure that each user is assigned a unique identifier. Finally, updating documentation or procedures related to user creation may also be necessary to reflect the changes made in the system.
    A: [
        {
            "summary": "Create Unique Id for all the users", 
            "description": "Generate Unique id for user and add him to database",
		    "team": "T1-Security",
		    "labels": ["PRO-DEV", "PRO-DEV-SEC"]
        },
        {
            "summary": "Test unique ids for users",
            "description": "Write a test case to test that all users uahve their own unique ids"
		    "team": "T5-Testers",
		    "labels": ["PRO-DEV", "PRO-DEV-TEST"]
        },
        {
            "summary": "Update document, procedure of User Creation",
            "description": "updated a document of procedure of User creation",
		    "team": "T7-Release",
		    "labels": [PRO-DEV, "PRO-DEV-RELAESE"]
        }
    ]

    Q: Increase Security of User Authentication: Develop a functionality to add unique users to a list, including generating unique IDs and updating documentation. Test the user ID generation process to ensure uniqueness.
    A: [
        {
            "summary": "Enhance Password Security with Password Strength Checker",
            "description": "Improve password security by implementing a password strength checker during registration and password change processes. Develop a tool that evaluates password strength and provides feedback.",
		    "team": "T1-Security",
		    "labels": ["PRO-DEV", "PRO-DEV-SEC"]
        },
        {
            "summary": "Implement Two-Factor Authentication (2FA) for User Accounts",
            "description": "Integrate a two-factor authentication system for user accounts to enhance security. Develop a mechanism using SMS codes or authenticator apps for user login.",
		    "team": "T1-Security",
		    "labels": ["PRO-DEV", "PRO-DEV-SEC"]
        },
        {
            "summary": "Add Email Notification Feature for Account Activity",
            "description": "Implement a feature to send email notifications to users for various account activities. Develop a system that sends emails for new messages, friend requests, or account settings changes."
		    "team": "T2-Features",
		    "labels": ["PRO-DEV", "PRO-DEV-FEAT"]
        },
        {
            "summary": "Test 2FA Authentication",
            "description": "write a test case to check 2FA authentication for user",
		    "team": "T5-Testers",
		    "labels": ["PRO-DEV", "PRO-DEV-TEST"]
        },
        {
            "summary": "Test Email Notification",
            "description": "write a test case to validate email notification for user activity",
		    "team": "T5-Testers",
		    "labels": ["PRO-DEV", "PRO-DEV-TEST"]
        }
    ]

    Q: Onboard User for Application:Enable user onboarding for the application by creating interactive tutorials for various pages. Also, include testing email notification functionality for user activity.
    A:[
        {
            "summary": "Create User Onboarding Tutorial for home page",
            "description": "Develop an interactive tutorial to guide new users through home page",
		    "team": "T2-Features",
		    "labels": ["PRO-DEV", "PRO-DEV-FEAT"]
        },
        {
            "summary": "Create User Onboarding Tutorial for search page",
            "description": "Develop an interactive tutorial to guide new users through search page"
		    "team": "T2-Features",
		    "labels": ["PRO-DEV", "PRO-DEV-FEAT"]
        },
        {
            "summary": "Create User Onboarding Tutorial for profile page",
            "description": "Develop an interactive tutorial to guide new users through profile page"
		    "team": "T2-Features",
		    "labels": ["PRO-DEV", "PRO-DEV-FEAT"]
        },
        {
            "summary": "Test Email Notification",
            "description": "write a test case to validate email notification for user activity"
		    "team": "T5-Testers",
		    "labels": ["PRO-DEV", "PRO-DEV-TEST"]
        }
    ]
    """

    PROMPT = f"""
    {INPUT_PREPARATION}
    {WORK_INSTRUCTION}
    {OUTPUT_SPECIFICATION}
    Generate stories for below epic
    Q:
    """