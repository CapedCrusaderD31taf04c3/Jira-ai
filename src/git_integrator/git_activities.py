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

from git_repository import Repository
from .create_pr import PRCreator
import re

class GitActivity(Repository):
    """
    """

    def __init__(self):
        """
        """
        self.git.checkout(self.default_branch)
        self.git.pull()

        self.branch_name = ""

    def prepare_branch_name(self, ticket_id, ticket_title):
        """
        """

        alphanumeric_string = re.sub(
            r'[^a-zA-Z0-9\s\\-]', 
            '', 
            f"{ticket_id} {ticket_title}"
        )

        branch_name = re.sub(r'\s+', '-', alphanumeric_string)
        return branch_name

    def create_new_branch(self, ticket_id, ticket_title):
        """
        """

        self.branch_name = self.prepare_branch_name(
            ticket_id=ticket_id, 
            ticket_title=ticket_title
        )

        self.git.branch(self.branch_name)
        return self

    def checkout_to_branch(self, branch_name):
        """
        """

        self.git.checkout(branch_name)
        return self
    
    def pull_changes(self):
        """
        """

        self.git.pull()

    def stage_changes(self):
        """
        """

        self.git.add(".")
        return self
    
    def commit_changes(self, commit_message):
        """
        """

        self.git.commit(m=commit_message)
        return self


    def push_changes(self):
        """
        """

        self.git.push("origin", self.branch_name)

        return self
    
    def status(self):
        """
        """

        self.git.status()

        return self

    def log(self):
        """
        """

        self.git.log()

        return self
    

class Procedure(GitActivity):
    """
    """

    def __init__(self):
        """
        """
        super().__init__()

        # Inititating
        self.create_new_branch(
            ticket_id="TASK-123", 
            ticket_title="We are Testing Git Intgrator"
        ).checkout_to_branch(self.branch_name)

        # Patching

        # Finalizing

        self.stage_changes().commit_changes(
            commit_message="This is a Commit Message"
        ).push_changes()

        # Creating PR
        
        # PRCreator(
        #     title="TASK-123-Testing-Git-Integrator", 
        #     body="PR Created for Github Integrator",
        #     head_branch="TASK-123-We-are-Testing-Git-Intgrator"
        #     )
