# This function moves and copies files from the static folder to the public folder.
import os
import shutil


SOURCE_DIR = os.path.expanduser(
    "~/bootdev/static_site/BD_Static_Site/static"
)
TARGET_DIR = os.path.expanduser(
    "~/bootdev/static_site/BD_Static_Site/public"
)

def list_directory_contents(path, label):
    print(f"\n{label}: {path}")

    if not os.path.exists(path):
        print("  (does not exist)")
        return

    for root, dirs, files in os.walk(path):
        indent = "  " * (root.count(os.sep) - path.count(os.sep))
        print(f"{indent}{os.path.basename(root)}/")
        for f in files:
            print(f"{indent}  {f}")

def move_contents():
    print("\n===== STARTING COPY OPERATION =====")

    print(f"Resolved SOURCE_DIR: {SOURCE_DIR}")
    print(f"Resolved TARGET_DIR: {TARGET_DIR}")

    list_directory_contents(SOURCE_DIR, "SOURCE (before)")
    list_directory_contents(TARGET_DIR, "TARGET (before)")

    clear_directory(TARGET_DIR)
    copy_recursive(SOURCE_DIR, TARGET_DIR)

    list_directory_contents(TARGET_DIR, "TARGET (after)")

    print("\n===== COPY OPERATION COMPLETE =====")


def clear_directory(path):
    #"""Delete all contents of a directory, but not the directory itself."""
    if not os.path.exists(path):
        print(f"Target does not exist, nothing to clear: {path}")
        return

    print(f"\nClearing target directory: {path}")

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            print(f"  Deleting file: {item_path}")
            os.remove(item_path)
        else:
            print(f"  Deleting directory: {item_path}")
            shutil.rmtree(item_path)
    
def copy_recursive(src, dst):
    #"""Recursively copy files and folders from src to dst."""
    
    if not os.path.exists(src):
        print(f"Source path does not exist: {src}")
        return

    if not os.path.exists(dst):
        print(f"Creating directory: {dst}")
        os.makedirs(dst)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} → {dst_path}")
            shutil.copy2(src_path, dst_path)
        elif os.path.isdir(src_path):
            print(f"Entering directory: {src_path}")
            copy_recursive(src_path, dst_path)

if __name__ == "__main__":
    move_contents()