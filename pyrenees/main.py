from textual.app import App, ComposeResult
from textual.widgets import TextArea, Header
from pathlib import Path
from pyrenees.src.buffer import Buffer
from pyrenees.src.config import Config
import rich_click as click
import os
from typing import Optional

# TEXT = """\
#         def hello(name):
#             print(f"hello {name}")
#
#         def goodbye(name):
#             print(f"goodbye {name}")
#
# """


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

    main(buf=buf)


class TextAreaExample(App):
    def __init__(self, buffer):
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


def main(buf: Buffer):
    app = TextAreaExample(buf)
    app.run()


# for running it in --dev mode
# if __name__ == "__main__":
# main()
