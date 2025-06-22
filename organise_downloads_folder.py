import os
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set

download_path: Path = Path.home() / "Downloads"
log_file_path: Path = download_path / "download_organizer.log"
folder_target_path: Path = download_path / "Folders"

file_categories: Dict[str, List[str]] = {
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ott"],
    "Text Files": [".txt", ".log", ".ini", ".conf", ".csv", ".json", ".xml", ".yml", ".yaml", ".rmf", ".md"],
    "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".webm"],
    "Compressed": [".zip", ".tar", ".gz", ".rar", ".7z", ".bz2",".tar.xz",".jar"],
    "Programs": [".deb", ".AppImage", ".exe", ".msi", ".sh", ".bat"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".c", ".java"],
    "Torrent": [".torrent"],
    "Patch Files": [".bps", ".ups"],
    "Others": []
}

def categorize_file(file_path: Path):
    ext = file_path.suffix.lower()
    for category, extension in file_categories.items():
        if ext in extension:
            return category
    return "Others"


def log_action(item_name: str, destination: Path):
    time_str = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open(log_file_path, "a") as log:
        log.write(f"[{time_str}] Moved '{item_name}' to '{destination}'\n")


def organinize_downloads_folder(dry_run: bool = True):
    destination_folders = set(file_categories) | {"Folders"}

    for item in download_path.iterdir():
        if item.name.startswith(".") or item.name == log_file_path.name:
            continue

        if item.is_file():
            category = categorize_file(item)
            category_path = download_path / category
            category_path.mkdir(exist_ok=True)
            destination = category_path / item.name

            if dry_run:
                print(f"[DRY RUN] Would move file: {item.name} -> {category}/")
            else:
                try:
                    shutil.move(str(item), str(destination))
                    print(f" Moved: {item.name} to Folder {category}/")
                    log_action(item.name, category_path)
                except Exception as e:
                    print(f"Could not move {item.name}: {e}")

        elif item.is_dir() and item.name not in destination_folders:
            folder_target_path.mkdir(exist_ok=True)
            destination = folder_target_path / item.name

            if dry_run:
                print(f"[DRY RUN] Would move folder: {item.name} -> Folders/")
            else:
                try:
                    shutil.move(str(item), str(destination))
                    print(f"Moved Folder: {item.name} to Folders/")
                    log_action(item.name, folder_target_path)
                except Exception as e:
                    print(f"Could not move folder {item.name}:{e}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Organize your Downloads folder by file type.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate the organization without moving any files or folders"
    )

    args = parser.parse_args()
    organinize_downloads_folder(dry_run=args.dry_run)
