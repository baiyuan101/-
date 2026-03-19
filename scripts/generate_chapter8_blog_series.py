import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output" / "doc"
CONTENT_DIR = ROOT / "content"

ZH_PATH = OUTPUT_DIR / "chapter-8-philosophy-of-care-education-zh.md"
EN_PATH = OUTPUT_DIR / "chapter-8-philosophy-of-care-education-en.md"

SERIES_SLUG = "the-educational-philosophy-of-care"
SERIES_TITLE = "The Educational Philosophy of Care"
SERIES_TITLE_ZH = "生命关怀的教育哲学"


NOTE_LIBRARY = {
    1: 'David Hume, *A Treatise of Human Nature*, Book 3, Part 2, Section 1. Helpful link: [Wikipedia entry](https://en.wikipedia.org/wiki/A_Treatise_of_Human_Nature).',
    2: 'Peter Singer, *The Most Good You Can Do: How Effective Altruism Is Changing Ideas About Living Ethically* (Yale University Press, 2015), p. 77. Helpful link: [Yale University Press](https://yalebooks.yale.edu/9780300219869/the-most-good-you-can-do/).',
    3: 'C. D. Navarrete, M. M. McDonald, M. L. Mott, and B. Asher, "Virtual Morality: Emotion and Action in a Simulated Three-Dimensional Trolley Problem," *Emotion* 12 (2011): 364-370. Helpful link: [DOI](https://doi.org/10.1037/a0025561).',
    4: 'Michael Numan, "Motivational Systems and the Neural Circuitry of Maternal Behavior in the Rat," *Developmental Psychobiology* 49, no. 1 (2007): 12-21. Helpful link: [PubMed](https://pubmed.ncbi.nlm.nih.gov/17186513/).',
    5: 'Jennifer S. Mascaro, Patrick D. Hackett, and James K. Rilling, "Testicular Volume Is Inversely Correlated with Nurturing-Related Brain Activity in Human Fathers," *PNAS* 110, no. 39 (2013): 15746-15751. Helpful link: [PubMed](https://pubmed.ncbi.nlm.nih.gov/24019499/).',
    6: 'Nel Noddings, *培养有道德的人——从品格教育到关怀伦理* (科学教育出版社, 2017), p. 101. Helpful link: [Teachers College Press](https://www.tcpress.com/educating-moral-people-9780807741689).',
    7: 'Nel Noddings, *培养有道德的人——从品格教育到关怀伦理* (科学教育出版社, 2017), p. 102. Helpful link: [Open Library](https://openlibrary.org/books/OL9390450M/Educating_Moral_People).',
    8: 'Stephen Darwall, *The Second-Person Standpoint: Morality, Respect, and Accountability* (Harvard University Press, 2006). Helpful link: [Harvard University Press](https://www.hup.harvard.edu/books/9780674025240).',
    9: 'Peter Singer, *The Most Good You Can Do: How Effective Altruism Is Changing Ideas About Living Ethically* (Yale University Press, 2015), p. 90. Helpful link: [Yale University Press](https://yalebooks.yale.edu/9780300219869/the-most-good-you-can-do/).',
    11: 'Carol Gilligan, *In a Different Voice* (中央编译出版社, 1999), p. 26. Helpful link: [Wikipedia entry](https://en.wikipedia.org/wiki/In_a_Different_Voice).',
    12: 'Carol Gilligan, *In a Different Voice* (中央编译出版社, 1999), pp. 25-26. Helpful link: [Open Library](https://openlibrary.org/books/OL9044867M/In_a_Different_Voice).',
    13: 'Carol Gilligan, *In a Different Voice* (中央编译出版社, 1999), p. 26. Helpful link: [Wikipedia entry](https://en.wikipedia.org/wiki/In_a_Different_Voice).',
    14: 'Carol Gilligan, *In a Different Voice* (中央编译出版社, 1999), p. 27. Helpful link: [Open Library](https://openlibrary.org/works/OL3412260W/In_a_different_voice).',
    15: 'Richard Yates, *Revolutionary Road*, trans. Hou Xiaoyi (上海译文出版社, 2014). Helpful link: [Wikipedia entry](https://en.wikipedia.org/wiki/Revolutionary_Road).',
    17: 'On Rawls\'s "veil of ignorance" as a thought experiment. Helpful link: [Wikipedia entry](https://en.wikipedia.org/wiki/Original_position).',
    18: 'Stephen Darwall, *The Second-Person Standpoint: Morality, Respect, and Accountability* (Harvard University Press, 2006). Helpful link: [Harvard University Press](https://www.hup.harvard.edu/books/9780674025240).',
    19: 'Stephen D. Brookfield, *批判性思维教与学——帮助学生质疑假设的方法和工具* (中国人民大学出版社, 2017), pp. 28-47. Helpful link: [Barnes & Noble listing](https://www.barnesandnoble.com/w/teaching-for-critical-thinking-stephen-d-brookfield/1111376389).',
    20: 'Stephen D. Brookfield, *批判性思维教与学——帮助学生质疑假设的方法和工具* (中国人民大学出版社, 2017), p. 1. Helpful link: [OverDrive listing](https://www.overdrive.com/media/666237/teaching-for-critical-thinking).',
    21: 'Stephen D. Brookfield, *批判性思维教与学——帮助学生质疑假设的方法和工具* (中国人民大学出版社, 2017), p. 18. Helpful link: [Barnes & Noble listing](https://www.barnesandnoble.com/w/teaching-for-critical-thinking-stephen-d-brookfield/1111376389).',
    22: 'On the rabbit-duck illusion. Helpful link: [Wikipedia entry](https://en.wikipedia.org/wiki/Rabbit%E2%80%93duck_illusion).',
    23: 'David Myers, *Social Psychology*, 11th ed. (Chinese translation), p. 225. Helpful link: [Google Books](https://books.google.com/books/about/Social_Psychology.html?id=fcs1AAAAQBAJ).',
    24: 'David Myers, *Social Psychology*, 11th ed. (Chinese translation), p. 226. Helpful link: [Google Books](https://books.google.com/books/about/Social_Psychology.html?id=fcs1AAAAQBAJ).',
    25: 'Stephen D. Brookfield, *批判性思维教与学——帮助学生质疑假设的方法和工具* (中国人民大学出版社, 2017), p. 50. Helpful link: [Barnes & Noble listing](https://www.barnesandnoble.com/w/teaching-for-critical-thinking-stephen-d-brookfield/1111376389).',
    26: 'Shelley E. Taylor, *Positive Illusions: Creative Self-Deception and the Healthy Mind* (Basic Books, 1989), cited in David Myers, *Social Psychology*, p. 525. Helpful link: [Google Books](https://books.google.com/books/about/Social_Psychology.html?id=fcs1AAAAQBAJ).',
    27: 'David Myers, *Social Psychology*, 11th ed. (Chinese translation), p. 525. Helpful link: [Google Books](https://books.google.com/books/about/Social_Psychology.html?id=fcs1AAAAQBAJ).',
    28: 'S. E. Brodt and P. G. Zimbardo, "Modifying Shyness-Related Social Behavior Through Symptom Misattribution," *Journal of Personality and Social Psychology* 41: 437-449. Helpful link: [Google Scholar search](https://scholar.google.com/scholar?q=Modifying+Shyness-Related+Social+Behavior+Through+Symptom+Misattribution).',
    29: 'Hanlin Ma and Gang Chen, "Research on Self-Deception: Intentionalism vs. Non-intentionalism." Helpful link: [Hanlin Ma publication page](https://baiyuan101.github.io/-/publications/research-on-self-deception-intentionalism-vs-non-intentionalism/).',
}


POST_SPECS = [
    {
        "slug": "empathy-as-a-second-person-standpoint",
        "title": "Empathy as a Second-Person Standpoint / 作为第二人称观点的同理心",
        "zh_heading": "作为第二人称观点的同理心——道德哲学的视角",
        "en_heading": "Empathy as a Second-Person Standpoint",
        "summary": "Part I of this bilingual series, adapted from *Life-Care Education Based on Improved Mental Models*, Chapter 8, Section 1. The English column is an AI translation revised for student readers; this part focuses on empathy, Hume, Singer, and the case for a second-person account.",
        "section_number": 1,
        "notes": [1, 2, 3, 4, 5],
        "date": "2026-03-19",
        "tags": ["education", "ethics", "cognitive-science"],
    },
    {
        "slug": "care-as-a-concept-mediated-relationship",
        "title": "Care as a Concept-Mediated Relationship / 关怀：以概念为中介的关系",
        "zh_heading": "关怀——以概念为中介的关系",
        "en_heading": "Care as a Concept-Mediated Relationship",
        "summary": "Part II of this bilingual series, adapted from *Life-Care Education Based on Improved Mental Models*, Chapter 8, Section 2. The English column is an AI translation revised for student readers; this part discusses Noddings, relational feedback, and the structure of care.",
        "section_number": 2,
        "notes": [6, 7, 8, 9],
        "date": "2026-03-18",
        "tags": ["education", "ethics", "writing"],
    },
    {
        "slug": "freedom-and-the-evolution-of-care",
        "title": "Freedom and the Evolution of Care / 自由与关怀的演化",
        "zh_heading": "自由——慎辨性与关怀的演化",
        "en_heading": "Freedom and the Evolution of Care",
        "summary": "Part III of this bilingual series, adapted from *Life-Care Education Based on Improved Mental Models*, Chapter 8, Section 3. The English column is an AI translation revised for student readers; this part addresses how care evolves with changing relationships and practical freedom.",
        "section_number": 3,
        "notes": [],
        "date": "2026-03-17",
        "tags": ["education", "ethics", "writing"],
    },
    {
        "slug": "adaptive-virtue-and-the-aim-of-care-education",
        "title": "Adaptive Virtue and the Aim of Care Education / 关怀教育的宗旨",
        "zh_heading": "关怀教育的宗旨——适应性的德性培养",
        "en_heading": "Adaptive Virtue and the Aim of Care Education",
        "summary": "Part IV of this bilingual series, adapted from *Life-Care Education Based on Improved Mental Models*, Chapter 8, Section 4. The English column is an AI translation revised for student readers; this part compares Gilligan and Kohlberg and frames care education as adaptive virtue.",
        "section_number": 4,
        "notes": [11, 12, 13, 14, 15, 17, 18],
        "date": "2026-03-16",
        "tags": ["education", "ethics", "writing"],
    },
    {
        "slug": "care-education-and-critical-thinking",
        "title": "Care Education and Critical Thinking / 关怀教育与慎辨性思维",
        "zh_heading": "关怀教育与慎辨性思维教育",
        "en_heading": "Critical Thinking and the Education of Care",
        "summary": "Part V of this bilingual series, adapted from *Life-Care Education Based on Improved Mental Models*, Chapter 8, Section 5. The English column is an AI translation revised for student readers; this part covers assumptions, Brookfield, and the pedagogical place of critical thinking in care education.",
        "section_number": 5,
        "notes": [19, 20, 21, 22, 23, 24, 25],
        "date": "2026-03-15",
        "tags": ["education", "teaching", "writing"],
    },
    {
        "slug": "positive-psychology-and-caring-practice",
        "title": "Positive Psychology and Caring Practice / 积极心理学与关怀实践",
        "zh_heading": "积极心理学与关怀实践",
        "en_heading": "Positive Psychology and Caring Practice",
        "summary": "Part VI of this bilingual series, adapted from *Life-Care Education Based on Improved Mental Models*, Chapter 8, Section 6. The English column is an AI translation revised for student readers; this part links care education to action, resilience, self-interpretation, and positive psychology.",
        "section_number": 6,
        "notes": [26, 27, 28, 29],
        "date": "2026-03-14",
        "tags": ["education", "ethics", "cognitive-science"],
    },
    {
        "slug": "care-and-the-four-quotients",
        "title": "Care and the Four Quotients / 关怀教育与四商",
        "zh_heading": "关怀教育与四商的关系及其内在张力",
        "en_heading": "Care and the Four Quotients",
        "summary": "Part VII of this bilingual series, adapted from *Life-Care Education Based on Improved Mental Models*, Chapter 8, Section 7. The English column is an AI translation revised for student readers; this part explores the relation between care and the four quotients together with the tensions internal to care.",
        "section_number": 7,
        "notes": [],
        "date": "2026-03-13",
        "tags": ["education", "ethics", "one-health"],
    },
]


def parse_sections(path: Path):
    text = path.read_text(encoding="utf-8")
    sections = {}
    current = None
    buffer = []
    for line in text.splitlines():
        if line.startswith("## Endnotes"):
            break
        if line.startswith("## "):
            if current:
                sections[current] = "\n".join(buffer).strip()
            current = line[3:].strip()
            buffer = []
        elif current:
            buffer.append(line)
    if current:
        sections[current] = "\n".join(buffer).strip()
    return sections


def localize_notes(text: str, note_ids: list[int]) -> tuple[str, str]:
    mapping = {old: new for new, old in enumerate(note_ids, start=1)}

    def repl(match: re.Match):
        old = int(match.group(1))
        return f"[{mapping[old]}]" if old in mapping else ""

    localized = re.sub(r"\[\^(\d+)\]", repl, text)
    localized = re.sub(r" +", " ", localized)
    localized = re.sub(r"\n{3,}", "\n\n", localized).strip()

    if not note_ids:
        return localized, ""

    notes_lines = ["## Notes", ""]
    for new, old in enumerate(note_ids, start=1):
        notes_lines.append(f"{new}. {NOTE_LIBRARY[old]}")
    return localized, "\n".join(notes_lines)


def front_matter(spec: dict, order: int) -> str:
    tags = ",\n    ".join(f'"{tag}"' for tag in spec["tags"])
    return (
        "{\n"
        f'  "title": "{spec["title"]}",\n'
        f'  "slug": "{spec["slug"]}",\n'
        f'  "date": "{spec["date"]}",\n'
        f'  "tags": [\n    {tags}\n  ],\n'
        f'  "summary": "{spec["summary"]}",\n'
        f'  "source_note": "From *Life-Care Education Based on Improved Mental Models*, Chapter 8, Section {spec["section_number"]}. The English text on this page is an AI translation revised for web reading.",\n'
        '  "series": "the-educational-philosophy-of-care",\n'
        f'  "series_title": "{SERIES_TITLE}",\n'
        f'  "series_order": {order},\n'
        '  "bilingual_layout": true\n'
        "}\n"
    )


def write_series_files():
    series_dir = CONTENT_DIR / "blog" / "series"
    series_dir.mkdir(parents=True, exist_ok=True)

    (series_dir / "_index.md").write_text(
        '{\n'
        '  "title": "Blog Series",\n'
        '  "description": "Extended note sequences and chapter-based series."\n'
        '}\n\n'
        'Series pages for longer writing projects and thematic sequences.\n',
        encoding="utf-8",
    )

    (series_dir / f"{SERIES_SLUG}.md").write_text(
        '{\n'
        f'  "title": "{SERIES_TITLE} / {SERIES_TITLE_ZH}",\n'
        f'  "slug": "{SERIES_SLUG}",\n'
        '  "summary": "A bilingual, section-by-section series based on Hanlin Ma\'s Chapter 8 in *Life-Care Education Based on Improved Mental Models*. The English side is an AI translation revised for web reading."\n'
        '}\n',
        encoding="utf-8",
    )


def main():
    zh_sections = parse_sections(ZH_PATH)
    en_sections = parse_sections(EN_PATH)

    blog_dir = CONTENT_DIR / "blog"
    blog_dir.mkdir(parents=True, exist_ok=True)
    write_series_files()

    for order, spec in enumerate(POST_SPECS, start=1):
        zh_body = zh_sections[spec["zh_heading"]]
        en_body = en_sections[spec["en_heading"]]
        zh_local, notes_md = localize_notes(zh_body, spec["notes"])
        en_local, _ = localize_notes(en_body, spec["notes"])

        body = (
            f"### {spec['zh_heading']}\n\n"
            f"{zh_local}\n\n"
            "<!--ENGLISH-->\n\n"
            f"### {spec['en_heading']}\n\n"
            f"{en_local}\n"
        )
        if notes_md:
            body += f"\n<!--NOTES-->\n\n{notes_md}\n"

        (blog_dir / f"{spec['slug']}.md").write_text(
            front_matter(spec, order) + "\n" + body,
            encoding="utf-8",
        )

    print("Generated blog series content.")


if __name__ == "__main__":
    main()
