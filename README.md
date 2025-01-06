# JSON_Keys_Editor

A script that allows users to interactively edit and clean JSON files by iterating over specified keys, deleting selected subkeys, and saving the updated file.

## Overview

This tool is particularly useful for cleaning and restructuring JSON data without manual editing. It enables the users to:

- Select a JSON file via an interactive dialog box.
- Specify the keys to iterate through and modify.
- Delete subkeys from dictionaries or lists.
- Save the modified JSON file to a chosen location.

## Requirements

- Python 3: Ensure Python 3 is installed.
- tkinter library: Included with standard Python installations for GUI dialogs.

## Files

- `JSON_Keys_Editor.py`

## Usage

1. **Run the Script**:
   Launch the `JSON_Editor.py` script.

2. **Select a JSON File**:
   Use the file dialog to choose a JSON file for editing.

3. **Specify Keys to Iterate**:
   Provide the key(s) to process, separated by commas (e.g., `metadata, data`).

4. **Edit Subkeys**:
   - For dictionary keys, choose specific subkeys to delete or clear all subkeys.
   - For list keys, specify subkeys to remove from each list entry or clear the list entirely.

5. **Save the Updated File**:
   Use the save dialog to select a destination and name for the updated JSON file.

## Important Notes

- **No Escaped Unicode**: The script saves files without escaping Unicode characters.
- **Key Preservation**: Unmodified keys and their data remain unchanged.
- **`ALL` Option**: Using the `ALL` option deletes all subkeys from the specified dictionary or list. Use this feature cautiously.

## Example Workflow

1. **Input JSON**:
    ```json
    {
        "metadata": {
            "author": "John Doe",
            "version": "1.0",
            "description": "Sample JSON file"
        },
        "data": [
            {"id": 1, "value": "abc", "timestamp": "2025-01-05T12:00:00"},
            {"id": 2, "value": "xyz", "timestamp": "2025-01-05T13:00:00"}
        ]
    }
    ```
2. **Key Selection**:
    - User selects `metadata` and deletes subkey `version`.
    - User selects `data` and deletes subkey `timestamp` from all entries.
3. **Output JSON**:
    ```json
    {
        "metadata": {
            "author": "John Doe",
            "description": "Sample JSON file"
        },
        "data": [
            {"id": 1, "value": "abc"},
            {"id": 2, "value": "xyz"}
        ]
    }
    ```

## License

This project is governed by the CC BY-NC 4.0 license. For comprehensive details, refer to the LICENSE file included in this project.
