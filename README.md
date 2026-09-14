# Dataset Processor

A Python pipeline for processing large JSONL datasets efficiently.

The application reads a JSONL file one record at a time, validates records, detects duplicates, groups records by category, processes records in batches, and produces processing statistics.

## Features

* Streams JSONL input line by line
* Validates required fields:

  * `id`
  * `text`
  * `category`
* Handles invalid JSON without stopping the entire program
* Skips invalid records safely
* Detects duplicate records using a `set`
* Counts records by category
* Processes records in configurable batches
* Handles the final partial batch
* Uses Python logging for processing events and errors
* Provides a command-line interface
* Keeps responsibilities separated across multiple modules

## Requirements

* Python 3.10+
* No external Python packages are required

## Project Structure

```text
Dataset-Processor/
├── main.py
├── reader.py
├── validator.py
├── processor.py
├── statistics.py
├── .gitignore
└── README.md
```

### Module Responsibilities

**`main.py`**

Application entry point. Handles command-line arguments, logging configuration, and coordinates the processing pipeline.

**`reader.py`**

Reads the JSONL file one line at a time and parses each JSON record.

**`validator.py`**

Validates individual records and checks required fields and ID hashability.

**`processor.py`**

Coordinates validation, deduplication, category counting, and batch processing.

**`statistics.py`**

Maintains processing statistics and prints the final summary.

## Input Format

The application expects a JSONL file where each line contains one JSON record.

Example:

```json
{"id": 1, "text": "Python is great", "category": "programming"}
{"id": 2, "text": "Hello world", "category": "general"}
{"id": 3, "text": "Asyncio is useful", "category": "programming"}
```

Each valid record must contain:

* `id` — must be present and hashable
* `text` — must not be empty
* `category` — must not be empty

Invalid JSON, empty lines, missing fields, empty values, and other invalid records are logged and skipped.

## Usage

Run the application with:

```bash
python main.py <file_path>
```

Example:

```bash
python main.py data.jsonl
```

The default batch size is `100`.

To specify a different batch size:

```bash
python main.py data.jsonl --batch-size 2
```

## Example Output

```text
INFO: Processing batch containing 2 records
WARNING: Line 3: Duplicate record with id=1 skipped
ERROR: Line 4: Invalid JSON: ...
ERROR: Line 6: Empty line
ERROR: Line 7: text cannot be empty
INFO: Processing batch containing 1 records

========== SUMMARY ==========
Total lines read: 7
Valid records: 3
Invalid records: 3
Duplicate records: 1

Records by category:
programming: 2
general: 1
```

## Processing Flow

```text
JSONL File
    │
    ▼
Reader
    │
    ▼
Validation
    │
    ├── Invalid → Log and Skip
    │
    ▼
Duplicate Check
    │
    ├── Duplicate → Log and Skip
    │
    ▼
Category Statistics
    │
    ▼
Batch Processing
    │
    ▼
Final Summary
```

## Design Considerations

### Streaming

The input file is processed one line at a time using a generator rather than loading the entire dataset into memory.

The input file is streamed line by line, avoiding the need to load the entire dataset into memory. Deduplication still requires storing previously seen IDs

### Deduplication

A Python `set` is used to track previously seen IDs.

Set membership provides average **O(1)** lookup time, making it more efficient than checking every ID in a list.

### Batching

Records are accumulated into fixed-size batches before processing.

Batching can reduce the overhead of repeatedly sending individual records to an external system such as a database, API, or message queue.

### Separation of Responsibilities

The project separates reading, validation, processing, and statistics into different modules.

This makes the code easier to understand, test, maintain, and extend.

