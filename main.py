"""
Copies windows spotlight images to C:\\Users\Admin\Pictures\\Spotlight. You can then use them as wallpapers or do
anything that you want with them.

Author: Priyansh Agrawal (https://www.github.com/Priyansh121096)
"""
import os
import shutil
from pathlib import Path
import click


DEFAULT_DEST_DIR = "C:\\Users\Admin\Pictures\\Spotlight"


@click.command()
@click.option(
    "--dest_dir",
    "-d",
    default=DEFAULT_DEST_DIR,
    help=f"Directory to copy the images to. By default, images are copied to {DEFAULT_DEST_DIR}.",
)
def main(dest_dir):
    if os.name != "nt":
        raise RuntimeError(f"This script can only be run on Windows (os.name returns '{os.name}'; should return 'nt').")

    source_dir = Path(
        f"{os.environ['LOCALAPPDATA']}\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
    )
    dest_dir = Path(dest_dir)

    if os.path.exists(dest_dir) and not os.path.isdir(dest_dir):
        raise RuntimeError(f"{dest_dir} should be a directory.")

    if not os.path.exists(dest_dir):
        print(f"Creating {dest_dir}")
        os.mkdir(dest_dir)

    for file in os.listdir(source_dir):
        source_path = source_dir / file
        dest_path = dest_dir / f"{file}.jpg"

        # Keep files larger than 1MB.
        if os.path.isfile(source_path) and (source_path.stat().st_size >> 20) >= 1:
            print(f"Copying {source_path} to {dest_path}")
            shutil.copy(source_path, dest_path)

    print("Done")


if __name__ == "__main__":
    main()
