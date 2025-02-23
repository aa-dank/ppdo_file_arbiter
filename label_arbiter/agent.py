# agent.py

"""
LabelerAgent coordinates file parsing, context assembly, and calling
an LLM (via LangGraph or another service) to generate applicable
filing code labels for a given PDF.
"""
import openai
import os
from jinja2 import Environment, FileSystemLoader
from typing import List, Any
from utils.file_parser import parse_pdf

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
        # Use parse_pdf to get basic metadata
        metadata = parse_pdf(file_path)
        # You could extend this dictionary with project_number, participants, etc. if known
        # for now just return the parse_pdf result or add fields
        metadata["project_number"] = "UNKNOWN"
        metadata["participants"]   = []
        metadata["dates"]          = []
        return metadata

    def _build_prompt(self, metadata: dict) -> str:
        # Suppose you placed the templates in "labeling/templates"
        template_dir = os.path.join(os.path.dirname(__file__), "labeling")
        env = Environment(loader=FileSystemLoader(template_dir))

        template = env.get_template("prompt_template.jinja2")
        prompt_text = template.render(metadata=metadata)
        return prompt_text

    def _invoke_llm(self, prompt_text: str) -> str:
        openai.api_key = os.getenv("OPENAI_API_KEY", "<fallback_or_error_handling>")
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt_text,
            max_tokens=256,
            temperature=0.7,
        )
        return response.choices[0].text.strip()

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
