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
        Task is one big jira epic has to be divided into multiple jira stories with necessary data as given in examples, 
        for your information, there are total 7 teams, 
        T1-Security(1cbc4b6a-6079-45ce-8534-462898a6d806) - PRO-DEV, PRO-DEV-SEC, 
        T2-Features(c45c8bd8-ba06-4979-b61e-5e5447d1fa3d) - PRO-DEV,PRO-DEV-FEAT, 
        T3-Frontend(8664327d-0c94-4f76-847c-290321d73852) - PRO-DEV,PRO-DEV-FRONT, 
        T4-BugFixers(78f67111-0f72-494f-ada8-a04d5268488c) - PRO-DEV,PRO-DEV-BUGFIXERS, 
        T5-Testers(313eae01-3ce3-4f68-9ca5-703844ea3cbe) - PRO-DEV,PRO-DEV-TEST, 
        T6-DevOps(0441b38c-4b5f-46fd-946b-a560121a53db) - PRO-DEV,PRO-DEV-DEVOPS, 
        T7-Release(f316a36e-214c-4847-b0a4-edf1b7a2fb88) - PRO-DEV,PRO-DEV-RELAESE, PRO-DEV-LEAD, 
    """

    WORK_INSTRUCTION = """
        Each team holds labels and responsibility for their related topic, 
        there are multiple labels PRO-DEV, PRO-DEV-SEC, PRO-DEV-FEAT, PRO-DEV-FRONT, PRO-DEV-BUGFIXERS, PRO-DEV-TEST, PRO-DEV-DEVOPS, PRO-DEV-RELAESE, PRO-DEV-LEAD, 
        each story must have 1 team id and few required labels,
    """

    OUTPUT_SPECIFICATION = """
        few examples are given below, provide only output with the given output format list of dictionaries with only provided key names
    """

    OUPUT_EXAMPLES = """
    Q: {
        "heading": "Provide Feature to add unique users to list",
        "info": "This task involves implementing a feature to add unique users to a list. The feature entails generating unique identifiers for users and adding them to a database. Additionally, it requires writing test cases to ensure that each user is assigned a unique identifier. Finally, updating documentation or procedures related to user creation may also be necessary to reflect the changes made in the system."
    }
    A: [
        {
            "title": "Create Unique Id for all the users", 
            "description": "Generate Unique id for user and add him to database",
            "team": "1cbc4b6a-6079-45ce-8534-462898a6d806",
            "labels": ["PRO-DEV", "PRO-DEV-SEC"]
        },
        {
            "title": "Test unique ids for users",
            "description": "Write a test case to test that all users uahve their own unique ids"
            "team": "313eae01-3ce3-4f68-9ca5-703844ea3cbe",
            "labels": ["PRO-DEV", "PRO-DEV-TEST"]
        },
        {
            "title": "Update document, procedure of User Creation",
            "description": "updated a document of procedure of User creation",
            "team": "f316a36e-214c-4847-b0a4-edf1b7a2fb88",
            "labels": ["PRO-DEV", "PRO-DEV-RELAESE"]
        }
    ]

    Q: {
        "heaading": "Increase Security of User Authentication"
        "info": "Develop a functionality to add unique users to a list, including generating unique IDs and updating documentation. Test the user ID generation process to ensure uniqueness."
    }
    A: [
        {
            "title": "Enhance Password Security with Password Strength Checker",
            "description": "Improve password security by implementing a password strength checker during registration and password change processes. Develop a tool that evaluates password strength and provides feedback.",
		    "team": "1cbc4b6a-6079-45ce-8534-462898a6d806",
		    "labels": ["PRO-DEV", "PRO-DEV-SEC"]
        },
        {
            "title": "Implement Two-Factor Authentication (2FA) for User Accounts",
            "description": "Integrate a two-factor authentication system for user accounts to enhance security. Develop a mechanism using SMS codes or authenticator apps for user login.",
		    "team": "1cbc4b6a-6079-45ce-8534-462898a6d806",
		    "labels": ["PRO-DEV", "PRO-DEV-SEC"]
        },
        {
            "title": "Add Email Notification Feature for Account Activity",
            "description": "Implement a feature to send email notifications to users for various account activities. Develop a system that sends emails for new messages, friend requests, or account settings changes."
		    "team": "c45c8bd8-ba06-4979-b61e-5e5447d1fa3d",
		    "labels": ["PRO-DEV", "PRO-DEV-FEAT"]
        },
        {
            "title": "Test 2FA Authentication",
            "description": "write a test case to check 2FA authentication for user",
		    "team": "313eae01-3ce3-4f68-9ca5-703844ea3cbe",
		    "labels": ["PRO-DEV", "PRO-DEV-TEST"]
        },
        {
            "title": "Test Email Notification",
            "description": "write a test case to validate email notification for user activity",
		    "team": "313eae01-3ce3-4f68-9ca5-703844ea3cbe",
		    "labels": ["PRO-DEV", "PRO-DEV-TEST"]
        }
    ]

    Q: {
        "heading": "Onboard User for Application",
        "info": "Enable user onboarding for the application by creating interactive tutorials for various pages. Also, include testing email notification functionality for user activity."
    A: [
        {
            "title": "Create User Onboarding Tutorial for home page",
            "description": "Develop an interactive tutorial to guide new users through home page",
		    "team": "c45c8bd8-ba06-4979-b61e-5e5447d1fa3d",
		    "labels": ["PRO-DEV", "PRO-DEV-FEAT"]
        },
        {
            "summary": "Create User Onboarding Tutorial for search page",
            "description": "Develop an interactive tutorial to guide new users through search page"
		    "team": "c45c8bd8-ba06-4979-b61e-5e5447d1fa3d",
		    "labels": ["PRO-DEV", "PRO-DEV-FEAT"]
        },
        {
            "summary": "Create User Onboarding Tutorial for profile page",
            "description": "Develop an interactive tutorial to guide new users through profile page"
		    "team": "c45c8bd8-ba06-4979-b61e-5e5447d1fa3d",
		    "labels": ["PRO-DEV", "PRO-DEV-FEAT"]
        },
        {
            "summary": "Test Email Notification",
            "description": "write a test case to validate email notification for user activity"
		    "team": "313eae01-3ce3-4f68-9ca5-703844ea3cbe",
		    "labels": ["PRO-DEV", "PRO-DEV-TEST"]
        }
    ]
    """


    PROMPT = (
        f"{INPUT_PREPARATION}\n"
        f"{WORK_INSTRUCTION}\n"
        f"{OUTPUT_SPECIFICATION}\n"
        f"{OUPUT_EXAMPLES}\n"
    )

    PROMPT_ = """
        Task is one big jira epic has to be divided into multiple jira stories with necessary data as given in examples, 
        for your information, there are total 7 teams, 
        T1-Security(1cbc4b6a-6079-45ce-8534-462898a6d806) - PRO-DEV, PRO-DEV-SEC, 
        T2-Features(c45c8bd8-ba06-4979-b61e-5e5447d1fa3d) - PRO-DEV,PRO-DEV-FEAT, 
        T3-Frontend(8664327d-0c94-4f76-847c-290321d73852) - PRO-DEV,PRO-DEV-FRONT, 
        T4-BugFixers(78f67111-0f72-494f-ada8-a04d5268488c) - PRO-DEV,PRO-DEV-BUGFIXERS, 
        T5-Testers(313eae01-3ce3-4f68-9ca5-703844ea3cbe) - PRO-DEV,PRO-DEV-TEST, 
        T6-DevOps(0441b38c-4b5f-46fd-946b-a560121a53db) - PRO-DEV,PRO-DEV-DEVOPS, 
        T7-Release(f316a36e-214c-4847-b0a4-edf1b7a2fb88) - PRO-DEV,PRO-DEV-RELAESE, PRO-DEV-LEAD, 
        Each team holds labels and responsibility for their related topic, 
        there are multiple labels PRO-DEV, PRO-DEV-SEC, PRO-DEV-FEAT, PRO-DEV-FRONT, PRO-DEV-BUGFIXERS, PRO-DEV-TEST, PRO-DEV-DEVOPS, PRO-DEV-RELAESE, PRO-DEV-LEAD, 
        each story must have 1 team id and few required labels,
        few examples are given below, provide only output with the given output format list of dictionaries with only provided key names
        examples - 
        Q: {
            "heading": "Provide Feature to add unique users to list",
            "info": "This task involves implementing a feature to add unique users to a list. The feature entails generating unique identifiers for users and adding them to a database. Additionally, it requires writing test cases to ensure that each user is assigned a unique identifier. Finally, updating documentation or procedures related to user creation may also be necessary to reflect the changes made in the system."
        }
        A: [
            {
                "title": "Create Unique Id for all the users", 
                "description": "Generate Unique id for user and add him to database",
                "team": "1cbc4b6a-6079-45ce-8534-462898a6d806",
                "labels": ["PRO-DEV", "PRO-DEV-SEC"]
            },
            {
                "title": "Test unique ids for users",
                "description": "Write a test case to test that all users uahve their own unique ids"
                "team": "313eae01-3ce3-4f68-9ca5-703844ea3cbe",
                "labels": ["PRO-DEV", "PRO-DEV-TEST"]
            },
            {
                "title": "Update document, procedure of User Creation",
                "description": "updated a document of procedure of User creation",
                "team": "f316a36e-214c-4847-b0a4-edf1b7a2fb88",
                "labels": ["PRO-DEV", "PRO-DEV-RELAESE"]
            }
        ]
    """