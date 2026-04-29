**File Organizer**

A simple script that sorts files in a target folder into category subfolders based on file extensions.

The main script is `file_organizer/file_organizer.py` and includes two primary actions:
- Organize: move files into category folders (Images, Documents, Videos, Music, Other).
- Reset: move files back to the target folder and remove empty category folders.

**Demo folder**
A small demo folder exists at `file_organizer/demo_folder` with sample files you can use to test safely.

**Usage**
Run the organizer from the project root and pass the folder path or run without arguments to be prompted:

```bash
python3 file_organizer/file_organizer.py /path/to/target_folder
```

When prompted, choose:
- `o` to organize files in the provided folder
- `r` to reset an organized folder back to its original flat state

**Safety Notes**
- The script moves files (it does not copy). Test using `file_organizer/demo_folder` before using on important data.
- The script only moves regular files (it skips directories).

**Extending**
To add or modify categories, edit the `file_categories` dictionary inside `file_organizer/file_organizer.py`. Add new file extensions to map them to the desired category.

**License**
See the repository LICENSE for usage terms.
