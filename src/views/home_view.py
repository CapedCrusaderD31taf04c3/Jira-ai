# Copyright (c) 2024 CapedCrusader
# All rights reserved.
#
# This software is licensed under the terms of the MIT.
# You should have received a copy of the license along with this
# program. If not, see LICENSE File.
# 
# ======================================

from fastapi import APIRouter, status
from webhooks.post_comment import PostCommentWBH

home_router = APIRouter()

class HomeView:
    """
    """
    @home_router.get("/")
    async def home():
        """
        """

        result = PostCommentWBH().post_comment(
            ticket_id="KAN-1",
            comment="This comment is made from API Request"
            )

        return {
            "message": "Success",
            "status": 200,
            "data": {
                "msg" : result
            }
        }