# Copyright (c) 2024 CapedCrusader
# All rights reserved.
#
# This software is licensed under the terms of the MIT.
# You should have received a copy of the license along with this
# program. If not, see LICENSE File.
# 
# ======================================



from pathlib import Path
from dotenv import load_dotenv

from fastapi import FastAPI
from views.comment_view import comment_router
from views.ticket_view import ticket_router
from views.home_view import home_router

class LoadEnvVars:
    """
    """
    @staticmethod
    def load_env_vars() -> None:
        env_path = Path(__file__).parent.parent / ".env"
        load_dotenv(dotenv_path=env_path)


class InitiateAIServer:
    """
    """
    
    app = FastAPI()
    
    @classmethod
    def include_routers(cls):
        """
        """
        routers = [
            home_router, comment_router, ticket_router
        ]

        for router in routers:
            cls.app.include_router(router)
            
    @classmethod
    def get_app(cls):
        """
        """
        # Adding all Routers
        cls.include_routers()

        return cls.app

# Run the FastAPI application
if __name__ == "__main__":
    """
    """
    
    import uvicorn

    LoadEnvVars.load_env_vars()

    app = InitiateAIServer.get_app()
    
    uvicorn.run(app, host="0.0.0.0", port=8000)


