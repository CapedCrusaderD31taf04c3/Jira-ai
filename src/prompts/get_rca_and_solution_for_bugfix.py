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

    OUTPUT_SPECIFICATION = """Provide proper Solution or roadmap to solve this issue and Root Cause in below given format only, keep the key names and value data type should same
    Q:{
        "heading": "Application Crashed on main menu",
        "info": "input_choice = int(input()) \nValueError: invalid literal for int() with base 10: 'one'"
    }
    A:{
        "solution": "To fix this issue, you need to ensure that the input provided is a valid integer. One approach could be to validate the input before attempting to convert it to an integer. For example, you could use a loop to prompt the user until they provide a valid integer input.",
        "root_cause": "The error occurred because the input provided by the user was not a valid integer, causing the ValueError when trying to convert it to an integer"
    }
    """

    PROMPT = f"""
    {INPUT_PREPARATION}
    {WORK_INSTRUCTION}
    {OUTPUT_SPECIFICATION}
    """
