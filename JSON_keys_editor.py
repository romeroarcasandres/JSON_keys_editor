import json
import tkinter as tk
from tkinter import filedialog, simpledialog

# Create a Tkinter root window (it won't be shown)
root = tk.Tk()
root.withdraw()

# Prompt the user to select the JSON file
file_path = filedialog.askopenfilename(title="Select a JSON file", filetypes=[("JSON files", "*.json")])

# Check if the user selected a file
if file_path:
    # Open and load the selected JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Prompt the user to enter the key(s) to iterate
    keys_to_iterate = simpledialog.askstring(
        "Input Required",
        "Enter the key(s) to iterate, separated by commas:")

    if keys_to_iterate:
        keys_to_iterate = [key.strip() for key in keys_to_iterate.split(',')]

        for key in keys_to_iterate:
            if key in data:
                if isinstance(data[key], dict):  # Handle dictionaries like "metadata"
                    subkeys_to_delete = simpledialog.askstring(
                        "Input Required",
                        f"For '{key}' (dictionary), enter the subkey(s) to delete, separated by commas, or type 'ALL' to delete all subkeys:")

                    if subkeys_to_delete:
                        if subkeys_to_delete.strip().upper() == 'ALL':
                            data[key] = {}
                        else:
                            subkeys_to_delete = [subkey.strip() for subkey in subkeys_to_delete.split(',')]
                            for subkey in subkeys_to_delete:
                                if subkey in data[key]:
                                    del data[key][subkey]

                elif isinstance(data[key], list):  # Handle lists
                    subkeys_to_delete = simpledialog.askstring(
                        "Input Required",
                        f"For '{key}' (list), enter the subkey(s) to delete, separated by commas, or type 'ALL' to delete all subkeys:")

                    if subkeys_to_delete:
                        if subkeys_to_delete.strip().upper() == 'ALL':
                            data[key] = []
                        else:
                            subkeys_to_delete = [subkey.strip() for subkey in subkeys_to_delete.split(',')]
                            for entry in data[key]:
                                if isinstance(entry, dict):
                                    for subkey in subkeys_to_delete:
                                        if subkey in entry:
                                            del entry[subkey]

        # Prompt the user to select the location to save the updated file
        save_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")], title="Save the updated JSON")

        # Check if the user chose a save location
        if save_path:
            # Write the updated JSON data to the selected file, ensure no Unicode escaping
            with open(save_path, 'w', encoding='utf-8') as output_file:
                json.dump(data, output_file, ensure_ascii=False, indent=4)

            print(f"Updated JSON file saved to: {save_path}")
        else:
            print("Save operation was cancelled.")
    else:
        print("No keys provided to iterate.")
else:
    print("No file selected.")
