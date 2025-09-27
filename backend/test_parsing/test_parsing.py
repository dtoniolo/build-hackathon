import json
from pathlib import Path

from .. import file_to_metrics

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = BASE_DIR.parent / "template.txt"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def load_file(path: Path) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    template = load_file(TEMPLATE_PATH)

    for example in ["example3.txt"]:
        example_path = BASE_DIR / example
        content = load_file(example_path)

        print(f"\n=== Processing {example} ===")
        try:
            prompt = file_to_metrics.build_prompt(template, content)
            raw_result = file_to_metrics.call_openai(prompt)

            # parse string -> dict
            parsed = json.loads(raw_result)

            # pretty print
            pretty = json.dumps(parsed, indent=2, ensure_ascii=False)
            print(pretty)

            # save to file
            out_file = OUTPUT_DIR / f"{example.replace('.txt', '')}_output.json"
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(pretty)

            print(f"Saved output to {out_file}")

        except Exception as e:
            print(f"Error processing {example}: {e}")


if __name__ == "__main__":
    main()
