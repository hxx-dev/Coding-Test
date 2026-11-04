
from pathlib import Path
import argparse
import filecmp
import shutil

ROOT = Path(__file__).resolve().parents[2]

PLATFORMS = {
    "백준", "프로그래머스", "SWEA",
    "구름레벨", "구름LEVEL"
}

LANGUAGES = {
    "Java", "Python", "Python3", "MySQL",
    "SQL", "C", "C++", "Cpp",
    "JavaScript", "TypeScript", "Kotlin"
}

def plan():
    moves = []

    for lang in sorted(LANGUAGES):
        for platform in sorted(PLATFORMS):
            base = ROOT / lang / platform
            if not base.is_dir():
                continue

            for file in sorted(base.rglob("*")):
                if not file.is_file():
                    continue

                parts = list(file.relative_to(base).parts)

                if platform == "프로그래머스":
                    if parts[0].isdigit():
                        parts[0] = "lv" + parts[0]

                target = ROOT / platform / lang / Path(*parts)
                moves.append((file, target))

    return moves

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    moves = plan()
    conflicts = []

    for src, dst in moves:
        print(f"{src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")

        if dst.exists():
            if not dst.is_file() or not filecmp.cmp(
                src, dst, shallow=False
            ):
                conflicts.append((src, dst))

    if conflicts:
        for src, dst in conflicts:
            print(f"CONFLICT: {src} -> {dst}")
        raise SystemExit("Conflicts detected. No changes made.")

    if not args.apply:
        print(f"DRY RUN: {len(moves)} files planned")
        return

    for src, dst in moves:
        dst.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            src.unlink()
        else:
            shutil.move(str(src), str(dst))

    # Delete empty source directories only.
    for lang in LANGUAGES:
        for platform in PLATFORMS:
            base = ROOT / lang / platform
            if not base.is_dir():
                continue

            dirs = sorted(
                [p for p in base.rglob("*") if p.is_dir()],
                key=lambda p: len(p.parts),
                reverse=True
            )
            for folder in dirs + [base]:
                if folder.is_dir() and not any(folder.iterdir()):
                    folder.rmdir()

        lang_dir = ROOT / lang
        if lang_dir.is_dir() and not any(lang_dir.iterdir()):
            lang_dir.rmdir()

    print(f"Migration complete: {len(moves)} files")

if __name__ == "__main__":
    main()
