
from pathlib import Path
import argparse
import filecmp
import re
import shutil

ROOT = Path(__file__).resolve().parents[2]

EXTENSIONS = {
    ".java": "Java",
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".cpp": "Cpp",
    ".cc": "Cpp",
    ".c": "C",
    ".kt": "Kotlin",
    ".go": "Go",
    ".rs": "Rust",
    ".sql": "SQL",
}

def difficulty(folder):
    readme = folder / "README.md"
    if not readme.is_file():
        return None

    content = readme.read_text(
        encoding="utf-8", errors="replace"
    )

    # Only accept explicit difficulty metadata.
    match = re.search(
        r"(?:Difficulty|난이도)\s*[:：]\s*"
        r"(Easy|Medium|Hard)\b",
        content,
        re.IGNORECASE
    )

    return match.group(1).capitalize() if match else None

def plan():
    moves = []
    skipped = []

    for folder in sorted(ROOT.iterdir()):
        if not folder.is_dir():
            continue

        if not re.match(r"^\d+[-.]", folder.name):
            continue

        files = sorted(
            p for p in folder.rglob("*") if p.is_file()
        )

        languages = {
            EXTENSIONS[p.suffix.lower()]
            for p in files
            if p.suffix.lower() in EXTENSIONS
        }

        level = difficulty(folder)

        if len(languages) != 1 or level is None:
            skipped.append(folder.name)
            continue

        lang = next(iter(languages))

        for src in files:
            relative = src.relative_to(folder)
            dst = (
                ROOT / "LeetCode" / lang
                / level / folder.name / relative
            )
            moves.append((src, dst))

    return moves, skipped

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    moves, skipped = plan()

    for folder in skipped:
        print(f"SKIPPED (check language/difficulty): {folder}")

    for src, dst in moves:
        print(f"MOVE {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")

        if dst.exists() and not (
            dst.is_file()
            and filecmp.cmp(src, dst, shallow=False)
        ):
            raise SystemExit(
                f"Conflict: {dst.relative_to(ROOT)}"
            )

    if not args.apply:
        print("DRY RUN: No changes made")
        return

    for src, dst in moves:
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            src.unlink()
        else:
            shutil.move(str(src), str(dst))

    # Remove only empty original problem folders.
    for folder in ROOT.iterdir():
        if not folder.is_dir():
            continue
        if not re.match(r"^\d+[-.]", folder.name):
            continue

        dirs = sorted(
            (p for p in folder.rglob("*") if p.is_dir()),
            key=lambda p: len(p.parts),
            reverse=True
        )
        for d in dirs + [folder]:
            if d.is_dir() and not any(d.iterdir()):
                d.rmdir()

    print("LeetCode organization complete")

if __name__ == "__main__":
    main()
