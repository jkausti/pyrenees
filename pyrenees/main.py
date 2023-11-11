from textual.app import App, ComposeResult
from textual.widgets import TextArea
from pyvim.src.buffer import Buffer
from pathlib import Path

# TEXT = """\
#         def hello(name):
#             print(f"hello {name}")
#
#         def goodbye(name):
#             print(f"goodbye {name}")
#
# """

class TextAreaExample(App):

    def __init__():
    def compose(self) -> ComposeResult:


        yield TextArea(buf.text[1], language="python")



def main():main
    app = TextAreaExample()
    app.run()


# for running it in --dev mode
if __name__ == '__main__':
    buf = Buffer(Path("~/projects/pyvim/example_files/test.py"))

    app = TextAreaExample()
    app.run()


