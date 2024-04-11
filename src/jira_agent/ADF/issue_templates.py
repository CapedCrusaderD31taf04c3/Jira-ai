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

from jira_agent.ADF.adf_components import ADFComponents

class IssueTemplate1:
    """
    Simple Rich text template for issues of the following format:

    User Story Description  (format: bold and green panel)
    < user story description text >  (format: single paragraph )
    """

    @classmethod
    def create_user_story_panel(cls,description:str):
        heading = ADFComponents.get_bold_paragraph_adf("User Story")
        user_story_description = ADFComponents.get_paragraph_adf(description)
        user_story_panel = ADFComponents.get_success_panel()
        user_story_panel["content"] = [heading,user_story_description]

        return user_story_panel
    
    @classmethod
    def create_issue_description(cls,story_desc:str) -> dict:

        description_payload = ADFComponents.get_main_doc_adf()

        user_story_panel = cls.create_user_story_panel(description=story_desc)
        description_payload["content"] = [user_story_panel]
        return description_payload


class IssueTemplate2:
    """
    Rich text templates for issues of the following format:

    User Story Description  (format: bold and green panel)
    < user story description text >  (format: single paragraph )

    In Scope (format: bold and green panel)
    - <point 1>     (format: Bullet list for each item)
    - <point 2>
    ...

    Out Scope (format: bold and green panel)
    - <point 1>     (format: Bullet list for each item)
    - <point 2>
    """

    @classmethod
    def create_user_story_panel(cls,description:str):
        heading = ADFComponents.get_bold_paragraph_adf("User Story")
        user_story_description = ADFComponents.get_paragraph_adf(description)
        user_story_panel = ADFComponents.get_success_panel()
        user_story_panel["content"] = [heading,user_story_description]

        return user_story_panel

    @classmethod
    def create_in_scope_panel(cls,in_scope_list:list):
        heading = ADFComponents.get_bold_paragraph_adf("In Scope")
        in_scope_list_points = ADFComponents.get_bullet_list()

        for item in in_scope_list:
            if(type(item) != str):
                item = str(item)
            
            list_item = ADFComponents.get_single_list_item(user_text=item)
            in_scope_list_points["content"].append(list_item)
        
        in_scope_panel = ADFComponents.get_success_panel()
        in_scope_panel["content"] = [heading,in_scope_list_points]

        return in_scope_panel

    @classmethod
    def create_out_scope_panel(cls,out_scope_list:list):
        heading = ADFComponents.get_bold_paragraph_adf("Out Scope")
        out_scope_list_points = ADFComponents.get_bullet_list()

        for item in out_scope_list:
            if(type(item) != str):
                item = str(item)
            
            list_item = ADFComponents.get_single_list_item(user_text=item)
            out_scope_list_points["content"].append(list_item)
        
        out_scope_panel = ADFComponents.get_success_panel()
        out_scope_panel["content"] = [heading,out_scope_list_points]

        return out_scope_panel

    @classmethod
    def create_issue_description(cls,story_desc:str,in_scope:list,out_scope:list) -> dict:

        description_payload = ADFComponents.get_main_doc_adf()

        user_story_panel = cls.create_user_story_panel(description=story_desc)
        in_scope_panel = cls.create_in_scope_panel(in_scope_list=in_scope)
        out_scope_panel = cls.create_out_scope_panel(out_scope_list=out_scope)

        description_payload["content"] = [user_story_panel,in_scope_panel,out_scope_panel]

        return description_payload
