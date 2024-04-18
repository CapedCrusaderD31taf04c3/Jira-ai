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


from pydantic import BaseModel
from typing import List

class GetRCAAndSolutionAIResponse(BaseModel):
    """
    """
    solution: str
    root_cause: str


class CreateStoriesAIResponse(BaseModel):
    """
    """
    
    title: str 
    description : str
    acceptance_criteria : List[str]
    team : str
    labels : List[str]
    in_scope : List[str]
    out_scope : List[str]
