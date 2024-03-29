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

    CREATE_STORIES_FROM_EPIC_PROMPT = """
    Here one big jira epic have to be divide into multiple jira stories, few examples are give below, 
    provide only output with the output format list of dictionaries with title and description keys

    Q: Provide Feature to add unique users to list
    A: [
        {
            "title": "Create Unique Id for all the users", 
            "description": "Generate Unique id for user and add him to database"
        },
        {
            "title": "Test unique ids for users",
            "description": "Write a test case to test that all users uahve their own unique ids"
        },
        {
            "title": "Update document, procedure of User Creation",
            "description": "updated a document of procedure of User creation"
        }
    ]

    Q: Increase Security of User Authentication 
    A: [
        {
            "title": "Enhance Password Security with Password Strength Checker",
            "description": "Improve password security by implementing a password strength checker during registration and password change processes. Develop a tool that evaluates password strength and provides feedback."
        },
        {
            "title": "Implement Two-Factor Authentication (2FA) for User Accounts",
            "description": "Integrate a two-factor authentication system for user accounts to enhance security. Develop a mechanism using SMS codes or authenticator apps for user login."
        },
        {
            "title": "Add Email Notification Feature for Account Activity",
            "description": "Implement a feature to send email notifications to users for various account activities. Develop a system that sends emails for new messages, friend requests, or account settings changes."
        },
        {
            "title": "Test 2FA Authentication",
            "description": "write a test case to check 2FA authentication for user"
        },
        {
            "title": "Test Email Notification",
            "description": "write a test case to validate email notification for user activity"
        }
    ]

    Q: Onboard User for Application
    [
        {
            "title": "Create User Onboarding Tutorial for home page",
            "description": "Develop an interactive tutorial to guide new users through home page"
        },
        {
            "title": "Create User Onboarding Tutorial for search page",
            "description": "Develop an interactive tutorial to guide new users through search page"
        },
        {
            "title": "Create User Onboarding Tutorial for profile page",
            "description": "Develop an interactive tutorial to guide new users through profile page"
        },
        {
            "title": "Test Email Notification",
            "description": "write a test case to validate email notification for user activity"
        }
    ]

    Generate stories for below epic

    """