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


class RCAAndSolutionPMT:

    INPUT_PREPARATION = """Bug, Error or Exception is reported in the format title:description, summarize this,"""

    WORK_INSTRUCTION = """This error occurred because of problem in source code,"""

    OUTPUT_SPECIFICATION = """Provide Solution and Root Cause in below given format only, keep the key names and value data type same
    {
        "solution": "This is a solution",
        "root_cause": "This is a root cause"
    }
    """

    PROMPT = f"""
    {INPUT_PREPARATION}
    {WORK_INSTRUCTION}
    {OUTPUT_SPECIFICATION}
    """
