
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