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



class ADFComponents:
    """
    ADF --> Atlassian Document Format
    This format allows for rich text integration through REST API
    """

    @classmethod
    def get_paragraph_adf(cls,user_text:str)->dict:
        paragraph_adf = {
            "type":"paragraph",
            "content": [
                {
                "type": "text",
                "text": str(user_text)
                }
            ]
        }

        return paragraph_adf


    @classmethod
    def get_single_list_item(cls,user_text:str)->dict:

        paragraph_adf = cls.get_paragraph_adf(user_text)

        listItem_adf = {
            "type": "listItem",
            "content":[paragraph_adf]
        }

        return listItem_adf

    @classmethod
    def get_bold_paragraph_adf(cls,user_text:str)->dict:

        bold_paragraph_adf = {
            "type": "paragraph",
            "content": [
                {
                "type": "text",
                "text": user_text,
                "marks": [
                    {
                    "type": "strong"
                    }
                ]
                }
            ]
        }

        return bold_paragraph_adf

    @classmethod
    def get_success_panel(cls)->dict:
        success_panel_adf = {
            "type": "panel",
            "attrs": 
                {
                "panelType": "success"
                },
            "content":[]
        }

        return success_panel_adf

    @classmethod
    def get_bullet_list(cls)->dict:

        bullet_list_adf = {
            "type": "bulletList",
            "content": []
        }

        return bullet_list_adf

    @classmethod
    def get_main_doc_adf(cls)->dict:

        main_doc_adf = {
            "version": 1,
            "type": "doc",
            "content": []
        }
        
        return main_doc_adf

    @classmethod
    def get_code_block(cls,language:str,code_snippet:str)->dict:

        code_block_adf = {
            "type": "codeBlock",
            "attrs": 
                {
                "language": language
                },
            "content": [
                {
                    "type": "text",
                    "text": code_snippet
                }
            ]
        }

        return code_block_adf

    @classmethod
    def get_cross_emoji(cls):
        cross_emoji = {
          "type": "emoji",
          "attrs": {
            "shortName": ":cross_mark:",
            "id": "atlassian-cross_mark",
            "text": ":cross_mark:"
          }
        }

        return cross_emoji
    
    @classmethod
    def acceptance_criteria(cls,acceptance_criteria):
        emoji_block = cls.get_cross_emoji()
        acceptance_criteria_block = [
            emoji_block,
            {
            "type": "text",
            "text": f" {acceptance_criteria}"
            },
            {
            "type": "hardBreak"
            }
        ]

        return acceptance_criteria_block