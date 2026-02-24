import shutil
import subprocess

URL = "https://www.google.com"


def open_in_google_chrome(url: str) -> None:
    chrome_commands = [
        ["google-chrome", url],
        ["google-chrome-stable", url],
        ["chromium-browser", url],
        ["chromium", url],
    ]

    for command in chrome_commands:
        if shutil.which(command[0]):
            subprocess.run(command, check=False)
            return

    raise RuntimeError("Google Chrome is not installed or not in PATH.")


if __name__ == "__main__":
    open_in_google_chrome(URL)
