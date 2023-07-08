"""
Copies windows spotlight images to C:\\Users\Admin\Pictures\\Spotlight. You can then use them as wallpapers or do
anything that you want with them.

Author: Priyansh Agrawal (https://www.github.com/Priyansh121096)
"""
import os
import shutil
from pathlib import Path

SOURCE_DIR = Path(f"{os.environ['LOCALAPPDATA']}\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets")
DEST_DIR = Path(f"C:\\Users\Admin\Pictures\\Spotlight")


def main():
    if os.path.exists(DEST_DIR) and not os.path.isdir(DEST_DIR):
        raise RuntimeError(f"{DEST_DIR} should be a directory.")

    if not os.path.exists(DEST_DIR):
        print(f"Creating {DEST_DIR}")
        os.mkdir(DEST_DIR)

    for file in os.listdir(SOURCE_DIR):
        source_path = SOURCE_DIR / file
        dest_path = DEST_DIR / f"{file}.jpg"

        # Keep files larger than 1MB.
        if os.path.isfile(source_path) and (source_path.stat().st_size >> 20) >= 1:
            print(f"Copying {source_path} to {dest_path}")
            shutil.copy(source_path, dest_path)

    print("Done")


if __name__ == '__main__':
    main()
