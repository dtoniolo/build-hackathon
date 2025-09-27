import pandas as pd
from openai import OpenAI

from dotenv import load_dotenv
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
            {"role": "user", "content": prompt}
        ],
        response_format={ "type": "json_object" }
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # Example usage
    excel_file = "data.xlsx"
    template_file = "template.txt"

    content_text = excel_to_text(excel_file)
    template_text = load_prompt_template(template_file)
    prompt = build_prompt(template_text, content_text)

    result = call_openai(prompt)
    print(result)
