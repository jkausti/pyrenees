from textual.widgets import Input
import os
from pathlib import Path


class FilenameInput(Input):

    def __init__(self, buffer):
        super().__init__()
        self.placeholder = 'Enter a filename'
        self.buffer = buffer


    def on_input_submitted(self):
        path = Path(os.path.abspath(self.value))
        self.buffer.path = path
        print(f"PATH IS {path} YYYEAH BABAY")
        self.buffer.save()
