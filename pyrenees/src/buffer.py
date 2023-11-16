from datetime import datetime
from pathlib import Path
import os
from typing import Optional
from textual.widgets import TextArea, Static
from pyrenees.src.widgets.basic import FilenameInput
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

    def set_path(self, val: str) -> None:
        p = Path(val)
        print(f"PATH!! :: {str(p)}")
        if os.path.isdir(str(p.parent)):
            self.path = p
        else:
            try:
                os.makedirs(str(p.parent))
                self.path = p
            except Exception:
                self.mount(Static("ERROR"))


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
            self.get_input()
            # self.path = Path(os.path.abspath(filename_input))

    # def attach_path(self, path: Path):
    # self.path = path

    def get_input(self):
        input_widget = FilenameInput(self)
        self.mount(input_widget)
        print("Focusing input widget!!!")
        input_widget.focus()
        
        # while input_widget.value_set == False:
            # pass

        # input_val = input_widget.value
        # TODO: Handle validation of path value
        # input_widget.remove()
        # return input_val

        

        # Insert input widget for entering the path
        # get path from widget -> make user click button
        # validate that entered path exists, if not create it
        # widget disappears
