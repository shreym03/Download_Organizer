# Download Folder Organizer

A Python script that organizes your cluttered `Downloads` folder by sorting files and folders into categorized subdirectories.

## Features

- Categorizes files by extension (e.g., Images, Videos, Documents, Archives)
- Moves folders into a `Folders/` subdirectory
- Supports `--dry-run` mode to simulate organization without changing anything
- Logs moved files and their destinations (disabled during dry run)

## Usage

Run from your terminal:

```bash
# Simulate only — nothing is actually moved
python3 organize_downloads.py --dry-run

# Actually move files and folders
python3 organize_downloads.py
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Notes

This script was created as a personal utility project to help manage cluttered downloads.
Some structural and design elements were refined with the help of AI-assisted tools during development.

## License

This project is licensed under the terms of the MIT License
See the [LICENSE](LICENSE) file for details.
