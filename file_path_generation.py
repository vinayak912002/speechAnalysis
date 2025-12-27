import os
from pathlib import Path

def collect_file_paths(folder_path):
    """
    Recursively collect all file paths in a folder as absolute paths.
    
    Args:
        folder_path: Path to the folder (string or Path object)
    
    Returns:
        List of absolute file paths (strings with forward slashes)
    """
    folder = Path(folder_path)
    
    # Convert to absolute path
    folder = folder.resolve()
    
    # Ensure the folder exists
    if not folder.exists():
        raise ValueError(f"Folder does not exist: {folder_path}")
    
    if not folder.is_dir():
        raise ValueError(f"Path is not a directory: {folder_path}")
    
    # Collect all files recursively
    file_paths = []
    
    for item in folder.rglob('*'):
        if item.is_file():
            # Convert to absolute path string with forward slashes
            path_str = item.resolve().as_posix()
            file_paths.append(path_str)
    
    # Sort for consistent output
    file_paths.sort()
    
    return file_paths

# Example usage
if __name__ == "__main__":
    # Example: Specify a folder path (can be relative or absolute)
    folder_path = r"archive\Actor_02"  # Replace with your actual folder path
    
    try:
        files = collect_file_paths(folder_path)
        
        # Print in the required format
        print("[")
        for file_path in files:
            print(f"   '{file_path}',")
        print("]")
        
    except ValueError as e:
        print(f"Error: {e}")