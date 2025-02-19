"""
Main entry point for the label_arbiter application.
Coordinates reading a file path from arguments (or config),
invokes the LabelerAgent for labeling,
and prints out or logs the resulting labels.
"""

import sys
from label_arbiter.labeling.labeler_agent import LabelerAgent

def main():
    """
    Orchestrates the labeling process. 
    Usage examples:
      1) python label_arbiter/main.py /path/to/document.pdf
      2) python label_arbiter/main.py data/test_files/sample.pdf
    """

    # 1. Get file path from CLI arguments or set a default
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        print("Usage: python label_arbiter/main.py /path/to/document.pdf")
        print("No file provided. Exiting.")
        sys.exit(1)

    # 2. Instantiate the LabelerAgent (in the future, pass in an actual LLM client)
    agent = LabelerAgent()

    # 3. Get labels from the agent
    labels = agent.label_file(file_path)

    # 4. Print or log the results
    print(f"\nFile: {file_path}")
    print(f"Predicted Labels: {labels}\n")

if __name__ == "__main__":
    main()