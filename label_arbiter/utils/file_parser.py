
import os
from typing import Dict

def parse_pdf(file_path: str) -> Dict[str, any]:
    """
    Naive approach to read basic info about the PDF.
    In the future, integrate advanced PDF parsing libraries 
    to extract text, references, or structured data.
    """
    # Just an example
    file_stats = os.stat(file_path)
    metadata = {
        "file_name": os.path.basename(file_path),
        "size_bytes": file_stats.st_size
        # "extracted_text": some_pdf_parsing_logic(file_path)
    }
    return metadata


def generate_dir_structure(dir_path, include_files=True, print_it=False):
    """
    Generate a text representation of a directory structure.

    Args:
        dir_path (str): The directory to represent.
        include_files (bool): Whether to include files in the representation.
        print_it (bool): Whether to print the representation.

    Returns:
        str: The text representation of the directory structure.
    """
    if not os.path.exists(dir_path):
        raise ValueError(f"The directory path '{dir_path}' does not exist.")

    def _generate_structure(current_path, prefix=""):
        items = os.listdir(current_path)
        lines = []

        for index, item in enumerate(sorted(items)):
            item_path = os.path.join(current_path, item)
            is_last = index == len(items) - 1
            connector = "└── " if is_last else "├── "

            if os.path.isdir(item_path):
                lines.append(f"{prefix}{connector}{item}/")
                sub_prefix = "    " if is_last else "│   "
                lines.extend(_generate_structure(item_path, prefix + sub_prefix))
            elif include_files:
                lines.append(f"{prefix}{connector}{item}")

        return lines

    # Generate the structure
    representation = "\n".join(_generate_structure(dir_path))

    # Optionally print the structure
    if print_it:
        print(representation)

    return representation