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

import json
from pathlib import Path

class CodeUpdater:
    """
    """

    def __init__(self, answer) -> None:
        """
        """

        self.solutions = json.loads(answer)

    # File update
    def file_updater(self, file_location, file_data):
        """
        """
        if file_location.exists():
            with open(file_location, "w") as fw:
                fw.write(file_data)

    def file_creater(self, file_location, file_data):
        """
        """
        if not file_location.parent.exists():
            file_location.parent.mkdir(parents=True)
        with open(file_location, "w") as fw:
            fw.write(file_data)

    def file_deleter(self, file_location):
        """
        """
        if file_location.exists():
            # If the file exists, delete it
            file_location.unlink()
        
        are_files_exists = [item.is_file() for item in file_location.parent.iterdir()]

        if not any(are_files_exists):
            file_location.parent.rmdir()
	
    def update(self):
        """
        """

        for solution in self.solutions:
            if solution["to_update"]:
                self.file_updater(
                    file_location=Path(solution["file_location"]),
                    file_data=solution["source_code"]
                )

            elif solution["to_create"]:
                self.file_creater(
                    file_location=Path(solution["file_location"]),
                    file_data=solution["source_code"]
                )

            elif solution["to_delete"]:
                self.file_deleter(
                    file_location=Path(solution["file_location"])
                )
