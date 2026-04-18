# file_hasher

Recursively hashes every file in a folder using MD5 and SHA256, printing results to the terminal and writing them to a CSV file.

## Requirements

Python 3.6+ (no third-party dependencies).

## Usage

```bash
python file_hasher.py <folder> [--output <csv_file>]
```

### Arguments

| Argument | Description |
|---|---|
| `folder` | Path to the folder to scan (required) |
| `--output` | Output CSV filename (default: `hashes.csv`) |

### Examples

```bash
# Hash all files in /tmp/docs, write results to hashes.csv
python file_hasher.py /tmp/docs

# Specify a custom output file
python file_hasher.py /tmp/docs --output results.csv
```

## Output

**Terminal** — a formatted table with filename, MD5, and SHA256 columns. Files that could not be read are listed separately with the reason.

**CSV** — four columns: `filename`, `path`, `md5`, `sha256`. One row per file.

## Error handling

Files that cannot be read (e.g. permission denied) are skipped and reported at the end of terminal output. They are not included in the CSV.
