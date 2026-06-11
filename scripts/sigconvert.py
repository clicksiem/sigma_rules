from typing import TypedDict
from sigma.backends.clickhouse.clickhouse import ClickhouseBackend
from sigma.backends.loki.loki import LogQLBackend
from sigma.collection import SigmaCollection
from sigma.conversion.base import TextQueryBackend
from sigma.exceptions import SigmaError
from pathlib import Path
import os
import logging
import argparse

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

# TODO: why not use Path.glob?


def list_files_recursively(
    path: Path = Path("."), extension: str = ".yml"
) -> list[Path]:
    if not path.is_dir():
        logger.error("Path is not a dir")
        return []

    files = []
    logger.info(f"Listing files in {path}")
    for entry in os.listdir(path):
        entry = path / entry
        if entry.is_dir():
            logger.debug(f"new directory {entry}")
            files.extend(list_files_recursively(entry))
        elif entry.is_file():
            if entry.name.endswith(extension):
                logger.debug(f"new file {entry}")
                files.append(entry)
        else:
            continue
    return files


class BackendFormat(TypedDict):
    backend: TextQueryBackend
    output_format: str

backend_format: dict[str, BackendFormat] = {
    "clickhouse": {
        "backend": ClickhouseBackend(),
        "output_format": "clickdetect",
    },
    "loki": {"backend": LogQLBackend(), "output_format": "default"},
}

def load_and_save(path: Path, _backend="clickhouse"):
    collection: SigmaCollection = SigmaCollection.from_yaml(path.read_text())

    
    format = backend_format.get(_backend, {})
    backend = format.get('backend', None)
    output = format.get('output_format', None)

    if not format or not backend or not output:
        raise Exception('backend not found')

    path = Path(f"{_backend}", *path.parts[1:])  # replace "sigma/"
    rule_data = backend.convert(collection, output_format=output)[0]
    # logger.debug(f'RULE DATA: {rule_data}')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(rule_data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-b",
        "--backend",
        help="sigma backend (default: clickhouse)",
        default="clickhouse",
        type=str,
    )
    parser.add_argument(
        "-d",
        "--dir",
        help="directory of the sigma rules (default: ./sigma/rules/)",
        default="./sigma/rules/",
        type=str,
    )

    args = parser.parse_args()

    files = list_files_recursively(Path(args.dir))
    for file in files:
        try:
            load_and_save(file, args.backend)
        except Exception as err:
            logger.error(f"Failed to load {file}\n{str(err)}")


main()
