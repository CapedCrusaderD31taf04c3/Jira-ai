from fastapi import APIRouter, status
from api_requests.post_comment import PostCommentAPI

home_router = APIRouter()

class HomeView:
    """
    """
    @home_router.get("/")
    async def home():
        """
        """

        result = PostCommentAPI().post_comment(
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