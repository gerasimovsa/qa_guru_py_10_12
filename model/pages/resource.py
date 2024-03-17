from pathlib import Path
import tests


def path(file_name: str):
    filepath = Path(tests.__file__).parent.joinpath(f'resources/{file_name}').absolute()
    return str(filepath)
