from datetime import datetime
from pathlib import Path
import os
from typing import Optional
from textual.widgets import TextArea
from textual import events
from textual.message import Message

# Buffer class
#
# Contains data about the buffer being edited and related functions





class Buffer(TextArea):
    """
    An extension of the TextArea which handles reads and writes to local
    filesystem.
    """

    class Saved(Message):
        """
        Text saved message.
        """
        
        def __init__(self, text: str):
            self.saved_text = text
            super().__init__()



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


    def _on_key(self, event: events.Key) -> None:
        if event.key == "ctrl+s":
            self.post_message(self.Saved(self.text))

