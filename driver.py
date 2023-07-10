"""
Copies windows spotlight images to C:\\Users\Admin\Pictures\\Spotlight. Calls ./main.py internally.

Author: Priyansh Agrawal (https://www.github.com/Priyansh121096)
"""
import os

from main import main


def run():
    return main(
        f"{os.environ['LOCALAPPDATA']}\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets",
        "C:\\Users\Admin\Pictures\Spotlight",
    )


if __name__ == "__main__":
    run()
