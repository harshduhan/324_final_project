from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable

EXPECTED_FILES = [
    "BJP_2009.txt",
    "BJP_2014.txt",
    "INC_2009.txt",
    "INC_2014.txt",
]
VALID_PATTERN = re.compile(r"^(?P<party>[A-Za-z]+)_(?P<year>\d{4})\.txt$")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def count_words(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def count_lines(text: str) -> int:
    return len(text.splitlines())


def summarize_file(path: Path) -> dict:
    text = read_text(path)
    words = count_words(text)
    lines = count_lines(text)
    chars = len(text)
    blank = not text.strip()
    return {
        "name": path.name,
        "chars": chars,
        "lines": lines,
        "words": words,
        "blank": blank,
    }


def find_duplicate_like_files(paths: Iterable[Path]) -> list[tuple[str, list[str]]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for path in paths:
        normalized = re.sub(r" \(\d+\)(?=\.txt$)", "", path.name)
        groups[normalized].append(path.name)
    return [(base, names) for base, names in groups.items() if len(names) > 1]


def validate_dataset(data_dir: Path, strict: bool = False) -> int:
    print(f"Validating dataset in: {data_dir.resolve()}")

    if not data_dir.exists():
        print("ERROR: data directory does not exist.")
        return 1
    if not data_dir.is_dir():
        print("ERROR: provided path is not a directory.")
        return 1

    txt_files = sorted(data_dir.glob("*.txt"))
    if not txt_files:
        print("ERROR: no .txt files found.")
        return 1

    print(f"Found {len(txt_files)} text file(s).\n")

    issues: list[str] = []

    found_names = {p.name for p in txt_files}
    missing = [name for name in EXPECTED_FILES if name not in found_names]
    if missing:
        issues.append(f"Missing expected files: {', '.join(missing)}")

    duplicate_like = find_duplicate_like_files(txt_files)
    for base, names in duplicate_like:
        issues.append(f"Possible duplicate files for {base}: {', '.join(names)}")

    malformed = [p.name for p in txt_files if not VALID_PATTERN.match(p.name)]
    if malformed:
        issues.append(
            "Files not matching '<PARTY>_<YEAR>.txt' naming convention: "
            + ", ".join(malformed)
        )

    print("File summary:")
    for path in txt_files:
        stats = summarize_file(path)
        flag = " [BLANK]" if stats["blank"] else ""
        print(
            f"- {stats['name']}: {stats['words']} words, "
            f"{stats['lines']} lines, {stats['chars']} chars{flag}"
        )
        if stats["blank"]:
            issues.append(f"Blank file detected: {stats['name']}")
        elif stats["words"] < 100:
            issues.append(f"Suspiciously short file: {stats['name']} ({stats['words']} words)")

    by_party: dict[str, list[str]] = defaultdict(list)
    by_year: dict[str, list[str]] = defaultdict(list)
    for path in txt_files:
        match = VALID_PATTERN.match(path.name)
        if match:
            by_party[match.group("party")].append(match.group("year"))
            by_year[match.group("year")].append(match.group("party"))

    if by_party:
        print("\nCoverage by party:")
        for party, years in sorted(by_party.items()):
            print(f"- {party}: {', '.join(sorted(years))}")

    if by_year:
        print("\nCoverage by year:")
        for year, parties in sorted(by_year.items()):
            print(f"- {year}: {', '.join(sorted(parties))}")

    print("\nValidation result:")
    if issues:
        for issue in issues:
            print(f"- {issue}")
        print("\nDataset validation completed with warnings.")
        return 1 if strict else 0

    print("- No issues detected.")
    print("\nDataset validation passed.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Validate manifesto text dataset files and report basic coverage/stats."
    )
    parser.add_argument(
        "--data-dir",
        default="data",
        help="Path to directory containing manifesto .txt files (default: data)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return a non-zero exit code if any warnings are found.",
    )
    args = parser.parse_args()

    exit_code = validate_dataset(Path(args.data_dir), strict=args.strict)
    sys.exit(exit_code)
