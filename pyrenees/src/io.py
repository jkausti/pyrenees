from pathlib import Path


def save(content: str, path: Path) -> str:
    with open(str(path), 'w') as  f:
        f.write(content)

    return f"File \"{str(path)}\" written."


