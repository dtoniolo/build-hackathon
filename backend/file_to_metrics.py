import pandas as pd
from openai import OpenAI

from dotenv import load_dotenv

from commons import FormData

load_dotenv()

client = OpenAI()


def excel_to_text(excel_path: str) -> str:
    """Reads an Excel file and returns a plain text representation."""
    df = pd.read_excel(excel_path)
    return df.to_csv(index=False)  # simple: CSV-like text


def load_prompt_template(template_path: str) -> str:
    """Loads the template text file."""
    with open(template_path, "r", encoding="utf-8") as f:
        return f.read()


def build_prompt(template: str, content: str) -> str:
    """Fills the {content} placeholder with Excel text."""
    return template.replace("{content}", content)


def call_openai(prompt: str) -> str:
    """Sends the prompt to OpenAI and returns the response text."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # cheap, fast; swap if needed
        temperature=0,
        messages=[
            {"role": "system", "content": "You are a JSON extractor assistant."},
            {"role": "user", "content": prompt},
        ],
        response_format={"type": "json_object"},
    )
    result = response.choices[0].message.content
    return result if result is not None else ""


def parse_excel_to_metrics(
    file_contents: str, template_path: str = "template.txt"
) -> FormData:
    """Parses metrics from an Excel file into FormData."""
    content_text = excel_to_text(file_contents)
    template_text = load_prompt_template(template_path)
    prompt = build_prompt(template_text, content_text)

    result_json = call_openai(prompt)
    return FormData.model_validate_json(result_json)


def parse_text_to_metrics(
    file_content: str, template_path: str = "template.txt"
) -> FormData:
    """Parses metrics from plain text/CSV into FormData."""
    template_text = load_prompt_template(template_path)
    prompt = build_prompt(template_text, file_content)

    result_json = call_openai(prompt)
    return FormData.model_validate_json(result_json)


if __name__ == "__main__":
    # Example usage
    excel_file = "data.xlsx"
    template_file = "template.txt"

    content_text = excel_to_text(excel_file)
    template_text = load_prompt_template(template_file)
    prompt = build_prompt(template_text, content_text)

    result = call_openai(prompt)
    print(result)
