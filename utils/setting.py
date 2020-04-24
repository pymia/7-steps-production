from pathlib import Path


def get_formatted_path(file_path: str) -> Path:
    data_folder = Path("data")
    formatted_path = data_folder / file_path
    return formatted_path
