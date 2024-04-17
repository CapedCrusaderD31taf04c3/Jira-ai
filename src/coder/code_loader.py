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

from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PythonLoader


class SourceCodeLoader:
    """
    """

    docs = []

    @classmethod
    def loader(cls):
        """
        """

        loader = DirectoryLoader(
            "E:/Dummy_Project/todo_app/src", 
            glob="**/*.py",
            exclude=["*.pyc"],
            recursive=True,
            loader_cls=PythonLoader
        )

        cls.docs = loader.load()

        return cls.docs

