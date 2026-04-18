#!/usr/bin/env python3
import argparse
import csv
import hashlib
import os
import sys


def hash_file(path):
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            md5.update(chunk)
            sha256.update(chunk)
    return md5.hexdigest(), sha256.hexdigest()


def main():
    parser = argparse.ArgumentParser(description="Hash all files in a folder.")
    parser.add_argument("folder", help="Path to the folder to scan")
    parser.add_argument("--output", default="hashes.csv", help="Output CSV file (default: hashes.csv)")
    args = parser.parse_args()

    folder = os.path.abspath(args.folder)
    if not os.path.isdir(folder):
        print(f"Error: '{folder}' is not a directory.", file=sys.stderr)
        sys.exit(1)

    results = []
    errors = []

    for root, _, files in os.walk(folder):
        for name in sorted(files):
            path = os.path.join(root, name)
            try:
                md5, sha256 = hash_file(path)
                results.append((name, path, md5, sha256))
            except (OSError, PermissionError) as e:
                errors.append((path, str(e)))

    header = f"{'Filename':<40} {'MD5':<32}  {'SHA256'}"
    print(header)
    print("-" * len(header))
    for name, path, md5, sha256 in results:
        print(f"{name:<40} {md5:<32}  {sha256}")

    if errors:
        print(f"\nSkipped {len(errors)} file(s) due to errors:")
        for path, reason in errors:
            print(f"  {path}: {reason}")

    with open(args.output, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["filename", "path", "md5", "sha256"])
        writer.writerows(results)

    print(f"\nResults written to {args.output}")


if __name__ == "__main__":
    main()
