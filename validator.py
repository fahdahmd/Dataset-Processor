def validate_record(record):
    """Validate a single record."""

    if not isinstance(record, dict):
        return False, "Record must be a JSON object"

    required_fields = {"id", "text", "category"}
    missing_fields = required_fields - record.keys()

    if missing_fields:
        return False, (
            f"Missing required fields: "
            f"{', '.join(sorted(missing_fields))}"
        )

    if record["id"] is None:
        return False, "id cannot be empty"

    if not isinstance(record["text"], str):
        return False, "text must be a string"

    if not record["text"].strip():
        return False, "text cannot be empty"

    if not isinstance(record["category"], str):
        return False, "category must be a string"

    if not record["category"].strip():
        return False, "category cannot be empty"

    try:
        hash(record["id"])
    except TypeError:
        return False, "id must be hashable"

    return True, ""