import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"
WHITELIST_FILE = ROOT / "data" / "tag-whitelist.json"

REQUIRED_FIELDS = {
    "publication": ["title", "authors", "year", "venue", "type", "publication_section", "tags"],
    "blog": ["title", "date", "tags"],
    "talk": ["title", "date", "tags"],
    "episode": ["title", "date", "format", "tags", "show_notes"],
}
ALLOWED_PUBLICATION_SECTIONS = {"articles", "books", "other"}


def detect_kind(path: Path):
    rel = path.relative_to(CONTENT_DIR).as_posix()
    if path.name == "_index.md":
        return None
    if rel.startswith("publications/"):
        return "publication"
    if rel.startswith("blog/"):
        return "blog"
    if rel.startswith("lectures/media/series/"):
        return None
    if rel.startswith("lectures/media/"):
        return "episode"
    if rel.startswith("lectures/series/"):
        return None
    if rel.startswith("lectures/"):
        return "talk"
    return None


def extract_front_matter(text: str):
    stripped = text.lstrip("\ufeff")
    if not stripped.startswith("{"):
        raise ValueError("content file does not start with JSON front matter")

    depth = 0
    in_string = False
    escaped = False

    for index, char in enumerate(stripped):
        if escaped:
            escaped = False
            continue
        if char == "\\":
            escaped = True
            continue
        if char == '"':
            in_string = not in_string
            continue
        if in_string:
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                front_matter = stripped[: index + 1]
                body = stripped[index + 1 :].lstrip()
                return json.loads(front_matter), body

    raise ValueError("could not find the end of JSON front matter")


def expect_list(value, field_name, errors, rel_path):
    if not isinstance(value, list) or not value:
        errors.append(f"{rel_path}: '{field_name}' must be a non-empty list")
        return []
    return value


def validate_tags(data, allowed_tags, errors, rel_path):
    tags = data.get("tags")
    if tags is None:
        return
    tag_list = expect_list(tags, "tags", errors, rel_path)
    for tag in tag_list:
        if tag not in allowed_tags:
            errors.append(f"{rel_path}: tag '{tag}' is not in the whitelist")


def validate_publication(data, errors, rel_path):
    authors = data.get("authors")
    if authors is not None:
        expect_list(authors, "authors", errors, rel_path)

    section = data.get("publication_section")
    if section not in ALLOWED_PUBLICATION_SECTIONS:
        errors.append(
            f"{rel_path}: 'publication_section' must be one of {sorted(ALLOWED_PUBLICATION_SECTIONS)}"
        )

    published_in_chinese = data.get("published_in_chinese")
    if published_in_chinese is not None and not isinstance(published_in_chinese, bool):
        errors.append(f"{rel_path}: 'published_in_chinese' must be a boolean when present")

    ai_translation_pdf = data.get("ai_translation_pdf")
    if ai_translation_pdf is not None:
        if not isinstance(ai_translation_pdf, str) or not ai_translation_pdf.strip():
            errors.append(f"{rel_path}: 'ai_translation_pdf' must be a non-empty string when present")
        if section != "articles":
            errors.append(f"{rel_path}: 'ai_translation_pdf' is only supported for article entries")


def validate_talk(data, errors, rel_path):
    materials = data.get("materials")
    if materials is None:
        return
    if not isinstance(materials, list):
        errors.append(f"{rel_path}: 'materials' must be a list when present")
        return
    for item in materials:
        if not isinstance(item, dict) or "label" not in item or "url" not in item:
            errors.append(f"{rel_path}: each material link must have 'label' and 'url'")


def validate_episode(data, errors, rel_path):
    fmt = data.get("format")
    if fmt and fmt not in {"audio", "video"}:
        errors.append(f"{rel_path}: 'format' must be 'audio' or 'video'")


def main():
    allowed_tags = set(json.loads(WHITELIST_FILE.read_text(encoding="utf-8"))["allowed_tags"])
    errors = []
    used_tags = set()

    for path in sorted(CONTENT_DIR.rglob("*.md")):
        kind = detect_kind(path)
        if kind is None:
            continue

        rel_path = path.relative_to(ROOT).as_posix()
        data, _ = extract_front_matter(path.read_text(encoding="utf-8"))

        for field in REQUIRED_FIELDS[kind]:
            value = data.get(field)
            if value in (None, "", []):
                errors.append(f"{rel_path}: missing required field '{field}'")

        validate_tags(data, allowed_tags, errors, rel_path)
        used_tags.update(data.get("tags", []))

        if kind == "publication":
            validate_publication(data, errors, rel_path)
        elif kind == "talk":
            validate_talk(data, errors, rel_path)
        elif kind == "episode":
            validate_episode(data, errors, rel_path)

    for tag in sorted(used_tags):
        tag_page = CONTENT_DIR / "tag" / f"{tag}.md"
        if not tag_page.exists():
            errors.append(
                f"content/tag/{tag}.md: missing tag landing page for '{tag}'"
            )

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Content validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
