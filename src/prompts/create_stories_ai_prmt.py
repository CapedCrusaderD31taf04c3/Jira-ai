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

    "T1-Security": {"id":"1cbc4b6a-6079-45ce-8534-462898a6d806","labels": ["PRO-DEV", "PRO-DEV-SEC"],
                    "scope":["Security Requirements",
                            "Threat Modeling",
                            "Secure Architecture",
                            "Security Testing"]},

    "T2-Features":{"id":"c45c8bd8-ba06-4979-b61e-5e5447d1fa3d","labels":["PRO-DEV","PRO-DEV-FEAT"],
                    "scope":["Feature Ideation",
                    "Feature Design and Specification",
                    "Implementation",
                    "Testing and QA"]},

    "T3-Frontend":{"id":"8664327d-0c94-4f76-847c-290321d73852","labels":["PRO-DEV","PRO-DEV-FRONT"],
                    "Scope":["Accessibility Implementation",
                    "UX Optimization",
                    "Integration with Backend Systems",
                    "Performance Optimization",
                    "Testing and QA"]
                    },

    "T4-BugFixers":{"id":"78f67111-0f72-494f-ada8-a04d5268488c","labels":["PRO-DEV","PRO-DEV-BUGFIXERS"],
                    "scope":["Bug Investigation and RCA",
                    "SCA and Debugging",
                    "Bug Fixing",
                    "Regression Testing"]},

    "T5-Testers":{"id":"313eae01-3ce3-4f68-9ca5-703844ea3cbe","labels":["PRO-DEV","PRO-DEV-TEST"],
                    "scope":["Test Planning","Test Case Design","Defect Reporting"]},

    "T6-DevOps":{"id":"0441b38c-4b5f-46fd-946b-a560121a53db","labels":["PRO-DEV","PRO-DEV-DEVOPS"],
                "scope":["Infrastructure Provisioning",
                "CI/CD",
                "Configuration Management",
                "Containerization and Orchestration"]},

    "T7-Release":{"id":"f316a36e-214c-4847-b0a4-edf1b7a2fb88","labels":["PRO-DEV","PRO-DEV-RELEASE", "PRO-DEV-LEAD"],
                    "scope":["Version Control",
                    "Release Packaging",
                    "Pre-release Testing","Documentation"]} 
    """

    WORK_INSTRUCTION = """
        Each team holds labels and scope for their related topic,
        each story must have title,description,acceptance_criteria, 1 team id,few required labels and
        in_scope related to that task and out_scope specific to that task.
        there must be atleast one in_scope and out_scope
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
                "acceptance_criteria":["users are created with unique ids","unit test cases exist"],
                "team": "1cbc4b6a-6079-45ce-8534-462898a6d806",
                "labels": ["PRO-DEV", "PRO-DEV-SEC"],
                "in_scope":["Secure Architecture","Security Testing"],
                "out_scope":["Security Requirements","Threat Modeling"]
            },
            {
                "title": "Test unique ids for users",
                "description": "Write a test case to test that all users have their own unique ids",
                "acceptance_criteria":["test requirement doc is updated","integration tests exists"],
                "team": "313eae01-3ce3-4f68-9ca5-703844ea3cbe",
                "labels": ["PRO-DEV", "PRO-DEV-TEST"],
                "in_scope":["Test Planning","Test Case Design"],
                "out_scope":["Defect Reporting"]
            },
            {
                "title": "Update document, procedure of User Creation",
                "description": "updated a document of procedure of User creation",
                "acceptance_criteria":["requirement spec doc is available"],
                "team": "f316a36e-214c-4847-b0a4-edf1b7a2fb88",
                "labels": ["PRO-DEV", "PRO-DEV-RELAESE"],
                "in_scope":["Documentation"],
                "out_scope":["Version Control","Release Packaging","Pre-release Testing"]
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
            "acceptance_criteria":["password strength is checked whenever user creates a new password"],
		    "team": "1cbc4b6a-6079-45ce-8534-462898a6d806",
		    "labels": ["PRO-DEV", "PRO-DEV-SEC"],
            "in_scope":["Secure Architecture"],
            "out_scope":["Threat Modeling"]
        },
        {
            "title": "Implement Two-Factor Authentication (2FA) for User Accounts",
            "description": "Integrate a two-factor authentication system for user accounts to enhance security. Develop a mechanism using SMS codes or authenticator apps for user login.",
            "acceptance_criteria":["2FA is working as expected"],
		    "team": "1cbc4b6a-6079-45ce-8534-462898a6d806",
		    "labels": ["PRO-DEV", "PRO-DEV-SEC"],
            "in_scope":["Secure Architecture","Threat Modeling"],
            "out_scope":["Security Requirements"]
        },
        {
            "title": "Add Email Notification Feature for Account Activity",
            "description": "Implement a feature to send email notifications to users for various account activities. Develop a system that sends emails for new messages, friend requests, or account settings changes.",
            "acceptance_criteria":["user receives email notification as per account activity"],
		    "team": "c45c8bd8-ba06-4979-b61e-5e5447d1fa3d",
		    "labels": ["PRO-DEV", "PRO-DEV-FEAT"],
            "in_scope":["Feature Ideation","Feature Design and Specification"],
            "out_scope":["Implementation","Testing and QA"]
        },
        {
            "title": "Test 2FA Authentication",
            "description": "write a test case to check 2FA authentication for user",
            "acceptance_criteria":["tests are available for 2 FA"],
		    "team": "313eae01-3ce3-4f68-9ca5-703844ea3cbe",
		    "labels": ["PRO-DEV", "PRO-DEV-TEST"],
            "in_scope":["Test Case Design","Defect Reporting"],
            "out_scope":[ "Test Planning"]
        },
        {
            "title": "Test Email Notification",
            "description": "write a test case to validate email notification for user activity",
            "acceptance_criteria":["tests are available for email notifications sent"],
		    "team": "313eae01-3ce3-4f68-9ca5-703844ea3cbe",
		    "labels": ["PRO-DEV", "PRO-DEV-TEST"],
            "in_scope":["Test Planning"],
            "out_scope":["Test Case Design","Defect Reporting"]
        }
    ]

    Q: {
        "heading": "Onboard User for Application",
        "info": "Enable user onboarding for the application by creating interactive tutorials for various pages. Also, include testing email notification functionality for user activity."
    A: [
        {
            "title": "Create User Onboarding Tutorial for home page",
            "description": "Develop an interactive tutorial to guide new users through home page",
            "acceptance_criteria":["home page should provide interactive guidance, accessible."],
		    "team": "c45c8bd8-ba06-4979-b61e-5e5447d1fa3d",
		    "labels": ["PRO-DEV", "PRO-DEV-FEAT"],
            "in_scope":["Feature Ideation","Feature Design and Specification"],
            "out_scope":["Implementation","Testing and QA"]
        },
        {
            "summary": "Create User Onboarding Tutorial for search page",
            "description": "Develop an interactive tutorial to guide new users through search page",
            "acceptance_criteria":["search page should provide interactive guidance, accessible."],
		    "team": "c45c8bd8-ba06-4979-b61e-5e5447d1fa3d",
		    "labels": ["PRO-DEV", "PRO-DEV-FEAT"],
            "in_scope":["Implementation","Testing and QA"],
            "out_scope":["Feature Ideation","Feature Design and Specification"]
        },
        {
            "summary": "Create User Onboarding Tutorial for profile page",
            "description": "Develop an interactive tutorial to guide new users through profile page",
            "acceptance_criteria":["brief introduction explaining the tutorial's purpose and benefits, welcoming new users to the profile page"],
		    "team": "c45c8bd8-ba06-4979-b61e-5e5447d1fa3d",
		    "labels": ["PRO-DEV", "PRO-DEV-FEAT"],
            "in_scope":["Implementation"],
            "out_scope":["Feature Ideation","Feature Design and Specification"]
        },
        {
            "summary": "Test Email Notification",
            "description": "write a test case to validate email notification for user activity",
            "acceptance_criteria":["tests are available for email notifications sent"],
		    "team": "313eae01-3ce3-4f68-9ca5-703844ea3cbe",
		    "labels": ["PRO-DEV", "PRO-DEV-TEST"],
            "in_scope":["Test Planning","Test Case Design"],
            "out_scope":["Defect Reporting"]
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

    "T1-Security": {"id":"1cbc4b6a-6079-45ce-8534-462898a6d806","labels": ["PRO-DEV", "PRO-DEV-SEC"],
                    "scope":["Security Requirements",
                            "Threat Modeling",
                            "Secure Architecture",
                            "Security Testing"]},

    "T2-Features":{"id":"c45c8bd8-ba06-4979-b61e-5e5447d1fa3d","labels":["PRO-DEV","PRO-DEV-FEAT"],
                    "scope":["Feature Ideation",
                    "Feature Design and Specification",
                    "Implementation",
                    "Testing and QA"]},

    "T3-Frontend":{"id":"8664327d-0c94-4f76-847c-290321d73852","labels":["PRO-DEV","PRO-DEV-FRONT"],
                    "Scope":["Accessibility Implementation",
                    "UX Optimization",
                    "Integration with Backend Systems",
                    "Performance Optimization",
                    "Testing and QA"]
                    },

    "T4-BugFixers":{"id":"78f67111-0f72-494f-ada8-a04d5268488c","labels":["PRO-DEV","PRO-DEV-BUGFIXERS"],
                    "scope":["Bug Investigation and RCA",
                    "SCA and Debugging",
                    "Bug Fixing",
                    "Regression Testing"]},

    "T5-Testers":{"id":"313eae01-3ce3-4f68-9ca5-703844ea3cbe","labels":["PRO-DEV","PRO-DEV-TEST"],
                    "scope":["Test Planning","Test Case Design","Defect Reporting"]},

    "T6-DevOps":{"id":"0441b38c-4b5f-46fd-946b-a560121a53db","labels":["PRO-DEV","PRO-DEV-DEVOPS"],
                "scope":["Infrastructure Provisioning",
                "CI/CD",
                "Configuration Management",
                "Containerization and Orchestration"]},

    "T7-Release":{"id":"f316a36e-214c-4847-b0a4-edf1b7a2fb88","labels":["PRO-DEV","PRO-DEV-RELEASE", "PRO-DEV-LEAD"],
                    "scope":["Version Control",
                    "Release Packaging",
                    "Pre-release Testing","Documentation"]}

        Each team holds labels and scope for their related topic,
        each story must have title,description,acceptance_criteria, 1 team id,few required labels and
        in_scope related to that task and out_scope specific to that task.
        there must be atleast one in_scope and out_scope
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
                "acceptance_criteria":["users are created with unique ids","unit test cases exist"],
                "team": "1cbc4b6a-6079-45ce-8534-462898a6d806",
                "labels": ["PRO-DEV", "PRO-DEV-SEC"],
                "in_scope":["Secure Architecture","Security Testing"],
                "out_scope":["Security Requirements","Threat Modeling"]
            },
            {
                "title": "Test unique ids for users",
                "description": "Write a test case to test that all users have their own unique ids",
                "acceptance_criteria":["test requirement doc is updated","integration tests exists"],
                "team": "313eae01-3ce3-4f68-9ca5-703844ea3cbe",
                "labels": ["PRO-DEV", "PRO-DEV-TEST"],
                "in_scope":["Test Planning","Test Case Design"],
                "out_scope":["Defect Reporting"]
            },
            {
                "title": "Update document, procedure of User Creation",
                "description": "updated a document of procedure of User creation",
                "acceptance_criteria":["requirement spec doc is available"],
                "team": "f316a36e-214c-4847-b0a4-edf1b7a2fb88",
                "labels": ["PRO-DEV", "PRO-DEV-RELAESE"],
                "in_scope":["Documentation"],
                "out_scope":["Version Control","Release Packaging","Pre-release Testing"]
            }
        ]
    """