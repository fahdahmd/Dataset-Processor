import logging

from validator import validate_record


logger = logging.getLogger(__name__)


def process_batch(batch):
    """Process one batch of valid records."""

    logger.info(
        "Processing batch containing %d records",
        len(batch)
    )


def process_records(records, batch_size, statistics):
    """Validate, deduplicate, group, and batch records."""

    seen_ids = set()
    batch = []

    for line_number, record in records:
        statistics.increment_total_lines()

        if record is None:
            statistics.increment_invalid_records()

            logger.error(
                "Line %d contains invalid JSON or is empty",
                line_number
            )

            continue

        is_valid, error_message = validate_record(record)

        if not is_valid:
            statistics.increment_invalid_records()

            logger.error(
                "Line %d: %s",
                line_number,
                error_message
            )

            continue

        record_id = record["id"]

        if record_id in seen_ids:
            statistics.increment_duplicate_records()

            logger.warning(
                "Line %d: Duplicate record with id=%s skipped",
                line_number,
                record_id
            )

            continue

        seen_ids.add(record_id)

        statistics.increment_valid_records()

        category = record["category"]
        statistics.add_category(category)

        batch.append(record)

        if len(batch) == batch_size:
            process_batch(batch)
            batch.clear()

    if batch:
        process_batch(batch)