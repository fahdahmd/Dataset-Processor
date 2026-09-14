import json


def read_records(file_path):
    """Read a JSONL file one line at a time."""

    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):

            if not line.strip():
                yield line_number, None, "Empty line"
                continue

            try:
                record = json.loads(line)
                yield line_number, record, None

            except json.JSONDecodeError as error:
                yield line_number, None, f"Invalid JSON: {error}"