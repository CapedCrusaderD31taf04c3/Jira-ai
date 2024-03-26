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

from pathlib import Path
from dotenv import load_dotenv

from fastapi import FastAPI
from views.comment_view import comment_router
from views.ticket_view import ticket_router
from views.home_view import home_router
from views.chat_view import chat_router
from views.ticket_v2_view import ticket_router_v2
from views.search_view import search_router

from logger.custom_logger import Logger


class LoadEnvVars:
    """
    """
    @staticmethod
    def load_env_vars() -> None:
        """
        """

        Logger.info(message="Loading Env Vars", stage="START")

        env_path = Path(__file__).parent.parent / ".env"
        load_dotenv(dotenv_path=env_path)

        Logger.info(message="Loaded Env Vars", stage="End")


class InitiateAIServer:
    """
    """
    
    app = FastAPI()
    
    @classmethod
    def include_routers(cls):
        """
        """
        routers = [
            home_router, comment_router, 
            ticket_router,ticket_router_v2, 
            chat_router, search_router
        ]

        Logger.info(message="Including URL Routers", stage="START")

        for router in routers:
            cls.app.include_router(router)
        
        Logger.info(message="Included URL Routers", stage="END")
            
    @classmethod
    def get_app(cls):
        """
        """
        Logger.info(message="Server Configuring", stage="START")
        
        # Adding all Routers
        cls.include_routers()
        
        Logger.info(message="Server Configured", stage="END")

        return cls.app

# Run the FastAPI application
if __name__ == "__main__":
    """
    """
    
    import uvicorn

    Logger.info(message="Initiating Env Var Loader", stage="START")
    LoadEnvVars.load_env_vars()

    Logger.info(message="Initiating Server", stage="START")
    app = InitiateAIServer.get_app()
    
    uvicorn.run(app, host="0.0.0.0", port=8000)