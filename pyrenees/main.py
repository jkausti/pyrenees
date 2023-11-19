from textual.app import App, ComposeResult
from textual.widgets import Header, Label
from pathlib import Path
from pyrenees.src.buffer import Buffer
from pyrenees.src.config import Config
import rich_click as click
import os
from typing import Optional
from textual import on

from pyrenees.src.widgets.basic import FilenameInput
from pyrenees.src.io import save


@click.command
@click.argument("path", required=False)
def pyrenees(path: Optional[str] = None):
    """
    Command line argument for pyrenees.
    """

    if path:
        path = os.path.abspath(path)
        if os.path.isfile(path):
            buf = Buffer(Path(path))
        else:
            buf = Buffer()
    else:
        buf = Buffer()

    app = TextAreaExample(buf)
    app.run()


class TextAreaExample(App):
    CSS_PATH = "./src/styles/main_styles.tcss"

    def __init__(self, buffer: Buffer):
        super().__init__()
        self.buffer = buffer
        self.config = Config(os.getcwd())

    def compose(self) -> ComposeResult:
        yield Header()
        self.buffer.language = "python"
        self.buffer.theme = "monokai"
        self.buffer.text = self.buffer.get_text()
        # text_area = Buffer(self.buffer.text, language="python", theme="dracula")
        yield self.buffer

    # Save file
    @on(Buffer.Saved)
    def save(self, message: Buffer.Saved) -> None:
        # print(message.saved_text)
        if self.buffer.path:
            result = save(content=message.saved_text, path=self.buffer.path)
            self.mount(Label(result))
        else:
            self.input_widget = FilenameInput()
            self.input_widget.insert_text_at_cursor(f"{self.config.cwd}/")
            self.mount(self.input_widget)
            self.input_widget.focus()


    @on(FilenameInput.Submitted)
    def save_input(self, event: FilenameInput.Submitted):
        # val = self.query_one(FilenameInput).value
        # print(event.value)
        self.buffer.path = Path(event.value)
        result = save(content=self.buffer.text, path=self.buffer.path)
        self.input_widget.remove()
        self.mount(Label(result))
        self.buffer.focus()
