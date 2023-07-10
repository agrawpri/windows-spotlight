"""
Copies windows spotlight images from --src_dir to --dest_dir.

Author: Priyansh Agrawal (https://www.github.com/Priyansh121096)
"""
import os
import shutil
from pathlib import Path

import click


def main(src_dir: str, dest_dir: str):
    # if os.name != "nt":
    #     raise RuntimeError(
    #         f"This script can only be run on Windows (os.name returns '{os.name}'; should return 'nt')."
    #     )
    src_dir, dest_dir = Path(src_dir), Path(dest_dir)

    if os.path.exists(dest_dir) and not os.path.isdir(dest_dir):
        raise RuntimeError(f"{dest_dir} should be a directory.")

    if not os.path.exists(dest_dir):
        print(f"Creating {dest_dir}")
        os.mkdir(dest_dir)

    for file in os.listdir(src_dir):
        source_path = src_dir / file
        dest_path = dest_dir / f"{file}.jpg"

        # Keep files larger than 1MB.
        if os.path.isfile(source_path) and (source_path.stat().st_size >> 20) >= 1:
            print(f"Copying {source_path} to {dest_path}")
            shutil.copy(source_path, dest_path)

    print("Done")


@click.command()
@click.option("--src_dir", "-s", help="Directory where the spotlight images are stored.")
@click.option(
    "--dest_dir",
    "-d",
    help="Directory to copy the images to.",
)
def run(src_dir: str, dest_dir: str):
    return main(src_dir, dest_dir)


if __name__ == "__main__":
    run()
