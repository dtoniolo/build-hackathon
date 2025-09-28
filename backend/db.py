import json

from pydantic import BaseModel

from commons import FormData, SubmissionState


class Report(BaseModel):
    form_data: FormData
    state: SubmissionState


DB_FILE_PATH = "db.json"


def load_db() -> list[Report]:
    with open(DB_FILE_PATH) as file:
        file_contents = file.read()
    parsed_json = json.loads(file_contents)
    if not isinstance(parsed_json, list):
        raise TypeError("The data stored in the db file should be a list.")
    return [Report.parse_obj(item) for item in parsed_json]


def save_db(db: list[Report]) -> None:
    dicts = [item.model_dump() for item in db]
    with open(DB_FILE_PATH, "w") as file:
        json.dump(dicts, file)
