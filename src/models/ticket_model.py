# Copyright (c) 2024 CapedCrusader
# All rights reserved.
#
# This software is licensed under the terms of the MIT.
# You should have received a copy of the license along with this
# program. If not, see LICENSE File.
# 
# ======================================


from pydantic import BaseModel

class TicketModel(BaseModel):
    """
    """
    
    issue: dict
    user: dict
    timestamp: int