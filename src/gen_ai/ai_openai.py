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

import os
from openai import OpenAI

from logger.custom_logger import Logger


class JiraAI():
    """
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    model = "gpt-3.5-turbo-0125"
    response_format= { 
        "type": "json_object" 
    }
    role = "user"
  
  
    def __init__(self) -> None:
      """
      """
      pass  

    @classmethod
    def ask_openai(cls, question, ticket_type="Story"):
        """
        """
        try:
          response = cls.client.chat.completions.create(
              model=cls.model,
              messages=[
                {
                  "role": cls.role, 
                  "content": question
                }
              ]
            )
          return response.choices[0].message.content
        except Exception as e:
           Logger.error(message=str(e))
           return str(e)
