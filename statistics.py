from collections import defaultdict


class Statistics:
    def __init__(self):
        self.total_lines = 0
        self.valid_records = 0
        self.invalid_records = 0
        self.duplicate_records = 0
        self.records_by_category = defaultdict(int)

    def increment_total_lines(self):
        self.total_lines += 1

    def increment_valid_records(self):
        self.valid_records += 1

    def increment_invalid_records(self):
        self.invalid_records += 1

    def increment_duplicate_records(self):
        self.duplicate_records += 1

    def add_category(self, category):
        self.records_by_category[category] += 1

    def print_summary(self):
        print("\n========== SUMMARY ==========")
        print(f"Total lines read: {self.total_lines}")
        print(f"Valid records: {self.valid_records}")
        print(f"Invalid records: {self.invalid_records}")
        print(f"Duplicate records: {self.duplicate_records}")
        print("\nRecords by category:")

        for category, count in self.records_by_category.items():
            print(f"{category}: {count}")