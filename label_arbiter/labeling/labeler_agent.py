# label_arbiter/labeling/labeler_agent.py

"""
LabelerAgent coordinates file parsing, context assembly, and calling
an LLM (via LangGraph or another service) to generate applicable
filing code labels for a given PDF.
"""

from typing import List, Any

class LabelerAgent:
    def __init__(self, llm_client: Any = None):
        """
        :param llm_client: An optional LLM client or orchestration object.
                           Could be a LangGraph pipeline, a direct OpenAI client, etc.
        """
        self.llm_client = llm_client

    def label_file(self, file_path: str) -> List[str]:
        """
        Primary method to extract metadata from the file, assemble a prompt,
        call the LLM, and parse the returned labels.

        :param file_path: Path to the PDF file that needs labeling
        :return: A list of one or more filing code labels
        """
        # 1. Extract metadata from file (placeholder)
        #    In real code, you'd parse PDF contents or project #, participants, etc.
        metadata = self._extract_file_metadata(file_path)

        # 2. Build the prompt for the LLM using the metadata + instructions
        prompt_text = self._build_prompt(metadata)

        # 3. Invoke the LLM (placeholder)
        response = self._invoke_llm(prompt_text)

        # 4. Parse the LLM response to extract labels
        labels = self._parse_llm_response(response)
        return labels

    def _extract_file_metadata(self, file_path: str) -> dict:
        """
        Stub method to parse the file for relevant metadata:
        e.g. project number, participants, or date range.
        Replace with real PDF parsing logic.
        """
        # TODO: Integrate a utility from label_arbiter.utils.file_parser
        # e.g.: metadata = parse_pdf(file_path)
        # For now, return a placeholder
        return {
            "file_name": file_path,
            "project_number": "UNKNOWN",
            "participants": [],
            "dates": []
        }

    def _build_prompt(self, metadata: dict) -> str:
        """
        Combine metadata, instructions, and any relevant context (like
        filing code documentation) into a well-formed LLM prompt.
        """
        # TODO: Load or inject actual instructions for labeling from your docs or config
        instructions = (
            "You are an expert in archiving UCSC construction project files. "
            "Given the following metadata, please suggest any relevant filing code labels. "
            "These labels can be non-mutually exclusive. "
            "Metadata:\n"
        )
        # Build a simple textual representation
        for key, value in metadata.items():
            instructions += f"- {key}: {value}\n"

        return instructions

    def _invoke_llm(self, prompt_text: str) -> str:
        """
        Send the prompt_text to an LLM and return the response.
        This is a stub; integrate your chosen method (LangGraph, OpenAI, etc.).
        """
        # Example placeholder code:
        # response = self.llm_client.run(prompt_text)
        # return response

        # For now, we mock a response
        mock_response = (
            "Likely labels are: [A1, C2, G12]. Explanation: ... (truncated) ..."
        )
        return mock_response

    def _parse_llm_response(self, response: str) -> List[str]:
        """
        Interpret the LLM's raw text response and extract label strings.
        This parsing could range from simple regex to more advanced logic.
        """
        # For now, do a naive parse to find text within brackets
        # (In production, you'd refine or use a structured LLM output)
        # Example: "Likely labels are: [A1, C2, G12]. Explanation: ..."
        labels_section = response.split("[")[-1].split("]")[0]
        labels = [label.strip() for label in labels_section.split(",")]
        return labels
