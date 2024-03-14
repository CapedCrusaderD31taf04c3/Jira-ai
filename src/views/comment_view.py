from fastapi import APIRouter, status
from webhooks.post_comment import PostCommentWBH

comment_router = APIRouter()


class CommentView:
    """
    """
    @comment_router.get("/")
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