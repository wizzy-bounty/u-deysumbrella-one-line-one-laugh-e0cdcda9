import os
from pathlib import Path


def entry_path() -> Path:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / "entry.txt"


def main() -> None:
    line = "My umbrella has one job, yet somehow my socks attend every storm."
    entry_path().write_bytes(line.encode("utf-8"))


if __name__ == "__main__":
    main()
