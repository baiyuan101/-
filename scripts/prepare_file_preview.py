from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PREVIEW_DIR = ROOT / "public-preview"

# Convert relative directory links like "./about/" to "./about/index.html"
# so local file:// browsing opens the generated page instead of a folder view.
QUOTED_HREF_RE = re.compile(r'href=(["\'])(\./[^"\']*/)\1')
UNQUOTED_HREF_RE = re.compile(r'href=(\./[^\s>]*?/)(?=[\s>])')
QUOTED_SUBPATH_RE = re.compile(r'((?:href|src)=(["\']))((?:\./|\.\./)+)-/([^"\']+)\2')
UNQUOTED_SUBPATH_RE = re.compile(r'((?:href|src)=)((?:\./|\.\./)+)-/([^\s>]+)')


def should_rewrite(target: str) -> bool:
    if target.endswith("index.xml/"):
        return False
    if target.startswith("./css/") or target.startswith("./js/"):
        return False
    return True


def rewrite_html(path: Path) -> None:
    original = path.read_text(encoding="utf-8")

    def strip_quoted_subpath(match: re.Match) -> str:
        attr = match.group(1)
        quote = match.group(2)
        prefix = match.group(3)
        rest = match.group(4)
        return f"{attr}{prefix}{rest}{quote}"

    def strip_unquoted_subpath(match: re.Match) -> str:
        attr = match.group(1)
        prefix = match.group(2)
        rest = match.group(3)
        return f"{attr}{prefix}{rest}"

    def replace_quoted(match: re.Match) -> str:
        quote = match.group(1)
        target = match.group(2)
        if not should_rewrite(target):
            return match.group(0)
        return f'href={quote}{target}index.html{quote}'

    def replace_unquoted(match: re.Match) -> str:
        target = match.group(1)
        if not should_rewrite(target):
            return match.group(0)
        return f'href={target}index.html'

    updated = QUOTED_SUBPATH_RE.sub(strip_quoted_subpath, original)
    updated = UNQUOTED_SUBPATH_RE.sub(strip_unquoted_subpath, updated)
    updated = QUOTED_HREF_RE.sub(replace_quoted, updated)
    updated = UNQUOTED_HREF_RE.sub(replace_unquoted, updated)
    if updated != original:
        path.write_text(updated, encoding="utf-8")


def main() -> int:
    if not PREVIEW_DIR.exists():
        print("public-preview directory not found.")
        return 1

    for html_file in PREVIEW_DIR.rglob("*.html"):
        rewrite_html(html_file)

    print("Prepared file-based preview.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
