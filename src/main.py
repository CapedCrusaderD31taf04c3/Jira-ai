from typing import Union
from fastapi import FastAPI

from views.comment_view import comment_router
from views.ticket_view import ticket_router


app = FastAPI()


app.include_router(comment_router)
app.include_router(ticket_router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


