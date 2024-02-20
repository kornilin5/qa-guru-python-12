from pathlib import Path
import tests


def path_picture(file_name):
    return str(
        Path(tests.__file__).parent.joinpath(
            f'resources/{file_name}').absolute())
