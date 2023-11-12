import os
from typing import Optional


class Config:
    def __init__(self, cwd: Optional[str] = None):
        if not cwd:
            self.cwd = os.getcwd()
        else:
            self.cwd = cwd
