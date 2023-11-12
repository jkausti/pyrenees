from datetime import datetime
from pathlib import Path
import functools
import os
from typing import Tuple, Optional

# Buffer class
#
# Contains data about the buffer being edited and related functions


class Buffer:
    def __init__(self, path: Optional[Path] = None):
        if path:
            self.path = Path(os.path.expanduser(str(path)))
            self.latest_save = datetime.now()
            self.last_save_content = self.text
        else:
            self.path = path

    @functools.cached_property
    def text(self) -> str:
        if self.path:
            with open(str(self.path), "r") as f:
                return f.read()
        else:
            return ""

    @property
    def text_bytes(self) -> bytes:
        return self.text.encode("utf-8")

    def save(self):
        if self.path:
            with open(str(self.path), "w") as f:
                f.write(self.text)

            self.last_save_content = self.text
            del self.text
            self.latest_save = datetime.now()
        else:
            self.path = self.get_path()

            with open(str(self.path), "w") as f:
                f.write(self.text)

    def attach_path(self, path: Path):
        self.path = path

    def get_path(self) -> Path:
        pass
