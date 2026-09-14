import argparse
import logging

from processor import process_records
from reader import read_records
from statistics import Statistics


def main():
    parser = argparse.ArgumentParser(
        description="Process a JSONL dataset."
    )

    parser.add_argument(
        "file_path",
        help="Path to the JSONL file"
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        default=100,
        help="Number of records processed per batch"
    )

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s"
    )

    statistics = Statistics()

    records = read_records(args.file_path)

    process_records(
        records=records,
        batch_size=args.batch_size,
        statistics=statistics
    )

    statistics.print_summary()


if __name__ == "__main__":
    main()