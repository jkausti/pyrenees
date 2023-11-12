from datetime import datetime
from pathlib import Path
import functools
import os
from typing import Optional
from textual.widgets import TextArea
from textual import events

# Buffer class
#
# Contains data about the buffer being edited and related functions


class Buffer(TextArea):
    def __init__(self, path: Optional[Path] = None):
        super().__init__()
        if path:
            if "~" in str(path):
                # pathlib cannot handle '~' in path strings
                self.path = Path(os.path.expanduser(str(path)))
            else:
                self.path = Path(path)

            self.latest_save = datetime.now()

        else:
            self.path = path

    def get_text(self) -> str:
        if self.path:
            with open(str(self.path), "r") as f:
                return f.read()
        else:
            return ""

    # @property
    # def text_bytes(self) -> bytes:
    #     return self.text.encode("utf-8")

    def _on_key(self, event: events.Key) -> None:
        if event.key == "ctrl+s":
            """
            Save a file
            """
            self.save()

    def save(self):
        if self.path:
            with open(str(self.path), "w") as f:
                f.write(self.text)

            self.last_save_content = self.text
            self.latest_save = datetime.now()
            print(self.latest_save)
        else:
            pass
            # self.path = self.get_path()
            #
            # with open(str(self.path), "w") as f:
            #     f.write(self.text)

    # def attach_path(self, path: Path):
    # self.path = path

    # def get_path(self) -> Path:
    # pass
