from pathlib import Path

ENTRY_TEXT = "Ice bin full. Production stopped. You have pressed the ice button six times since it filled."


def write_entry() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY_TEXT, encoding="utf-8")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
