from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from pathlib import Path
import functools
import os

# Buffer class
#
# Contains data about the buffer being edited and related functions

class Buffer:

    def __init__(self, path: Optional[Path] = None):
        self.path = Path(os.path.expanduser(path))

        if self.path:
            self.latest_save = datetime.now()
            self.last_save_content = self.text[1]

            # if str(self.path).startswith('~'):
            #     self.path = Path(os.path.expanduser(str(self.path)))

        print(type(self.path))

    
    @functools.cached_property
    def text(self) -> tuple[str, str]:
        
        if self.path:
            try:
                with open(str(self.path), 'r') as f:
                    return ("success", f.read())
            except UnicodeDecodeError:
                return ("error", "Not possible to edit binary files")
        else:
            return ("error", "Buffer not attached to file")

    
    
    @property
    def text_bytes(self) -> bytes:
        return self.text[1].encode('utf-8')

    def save(self):
        if self.path:
            with open(str(self.path), "w") as f:
                f.write(self.text[1])

            self.last_save_content = self.text[1]
            del self.text
            self.latest_save = datetime.now()
        else:
            self.get_path()

    def attach_path(self, path: Path):
        self.path = path

    def get_path(self):
        pass

