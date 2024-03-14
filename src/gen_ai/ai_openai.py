# Copyright (c) 2024 CapedCrusader
# All rights reserved.
#
# This software is licensed under the terms of the MIT.
# You should have received a copy of the license along with this
# program. If not, see LICENSE File.
# 
# ======================================

import os

from openai import OpenAI

class JiraAI():
    """
    """
    client = OpenAI(api_key="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")
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
    def ask_openai(cls, question):
        """
        """
        try:
          response = cls.client.chat.completions.create(
              model=cls.model,
              response_format=cls.response_format,
              messages=[
                  {
                    "role": cls.role, 
                    "content": question
                  }
              ]
            )
          return response.choices[0].message.content
        except Exception as e:
           return str(e)
