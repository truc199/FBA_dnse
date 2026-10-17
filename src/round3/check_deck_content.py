"""Checks docs/doc_round3/deck_content.md against the limits of the Round 3A deck.

Limits (PROMPT_round3A_build.md, Phase 3.1): action title of at most 15 words; on-slide text of at most
60 words; a table on a main slide of at most 6 rows and 5 columns; speaker notes of about 120 words; an
Executive Summary of at most 150 words (slide 1, on-slide text plus its table); at least one table or
figure on every main slide; a "Source:" line under every table and figure. It also flags phrases the deck
must not use (PROMPT section 8 and the Phase 1 to 2 review).

Words are whitespace-separated tokens that contain a letter or a digit, so "VND 6.6 billion" is three
words and a dash is none.

Run: python src/round3/check_deck_content.py   (exits 1 when a hard limit is broken)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DECK = ROOT / "docs" / "doc_round3" / "deck_content.md"
APPENDIX = ROOT / "docs" / "doc_round3" / "deck_appendix.md"
TABLES = ROOT / "outputs" / "round3" / "tables"
# companion reports: (path, references heading, caption words, source label, forbidden phrases)
REPORTS = [
    (ROOT / "docs" / "doc_round3" / "report_round3A_en.md", "## References", ("Table", "Figure"), "Source:", None),
    (ROOT / "docs" / "doc_round3" / "report_round3A_vi.md", "## Tài liệu tham khảo", ("Bảng", "Hình"), "Nguồn:",
     ["đầu tiên gắn với lương", "không đối thủ nào", "85.000 TK", "ngân hàng ít sản phẩm đầu tư", "86 triệu", "T+1",
      "duy nhất", "miễn phí hoàn toàn", "lãi cao nhất"]),
]
REPORT_ALLOWED = {"2.5": {"85,000 accounts", "85.000 TK"}}  # the what-changed section quotes the Round 2 target
FIELDS = ["Action title", "On-slide text", "Table", "Figure", "Designer notes (tiếng Việt)", "Speaker notes", "Sources"]
LIMITS = {"title": 15, "text": 60, "summary": 150, "rows": 6, "cols": 5}
NOTES_RANGE = (100, 140)
FORBIDDEN = ["first salary-linked", "no competitor offers", "tier interest at most", "85,000 accounts",
             "banks offer little investment", "start after the decision to invest", "86 million", "T+1",
             "the only", "zero-fee", "zero fee", "highest yield", "highest rate", "best rate"]
MANUAL = ["Madrian"]  # allowed only for the payroll channel
ALLOWED = {5: {"85,000 accounts"}}  # the What-changed slide quotes the Round 2 target it replaces (decision D3)


def words(text):
    text = re.sub(r"[*`_>#]", " ", text)
    return [t for t in text.split() if re.search(r"[0-9A-Za-zÀ-ỹ]", t)]


def slides(md):
    parts = re.split(r"^## Slide (\d+): (.+)$", md, flags=re.M)
    out = []
    for i in range(1, len(parts), 3):
        out.append((int(parts[i]), parts[i + 1].strip(), parts[i + 2].split("\n## ")[0]))
    return out


def fields(body):
    pattern = r"^\*\*(" + "|".join(re.escape(f) for f in FIELDS) + r"):\*\*"
    pieces = re.split(pattern, body, flags=re.M)
    return {pieces[i]: pieces[i + 1].strip() for i in range(1, len(pieces), 2)}


def table_shape(text):
    lines = [ln for ln in text.splitlines() if ln.strip().startswith("|")]
    if len(lines) < 2:
        return 0, 0
    cols = len([c for c in lines[0].strip().strip("|").split("|")])
    rows = len([ln for ln in lines[2:] if not re.match(r"^\|[\s:|-]+\|$", ln.strip())])
    return rows, cols


def table_words(text):
    cells = [ln for ln in text.splitlines() if ln.strip().startswith("|") and not re.match(r"^\|[\s:|-]+\|$", ln.strip())]
    return len(words(" ".join(cells).replace("|", " ")))


def citations(paths, heading="## References"):
    """In-text citations without a reference entry (hard), and references never cited (reported)."""
    text = "\n".join(p.read_text(encoding="utf-8") for p in paths if p.exists())
    body, _, refs = text.rpartition("\n" + heading)
    entries = re.findall(r"^- (.+?)\. \(([^)]+)\)\.", refs, flags=re.M)
    known = {}
    for author, year in entries:
        label = year.split(",")[0].strip()
        known.setdefault(author.replace(", & ", ", ").strip(), set()).add(label)
    missing, used = [], set()
    short = {a.split(",")[0] if "," in a and not a.startswith(("DNSE", "National")) else a: a for a in known}
    for alias, author in short.items():
        name = alias if alias in ("DNSE Securities", "National Assembly of Vietnam") else alias.split(" et al")[0]
        name = {"National Assembly of Vietnam": "National Assembly"}.get(name, name)
        for m in re.finditer(re.escape(name) + r"(?: et al\.| (?:&|and|và) [A-Z][\w'’-]+)?,? \(?"
                             r"((?:\d{4}[a-z]?|n\.d\.(?:-[a-z])?)(?:, (?:\d{4}[a-z]?|n\.d\.(?:-[a-z])?))*)", body):
            for lab in (x.strip() for x in m.group(1).split(",")):
                if lab in known[author]:
                    used.add((author, lab))
                else:
                    missing.append(f"{name} ({lab})")
    uncited = sorted(f"{a} ({lab})" for a, labs in known.items() for lab in labs if (a, lab) not in used)
    return sorted(set(missing)), uncited


def table_blocks_match_csv(paths):
    """Each <!-- table: NAME --> block must equal outputs/round3/tables/NAME.csv, cell by cell."""
    import csv
    out = []
    for path in paths:
        if not path.exists():
            continue
        for name, block in re.findall(r"<!-- table: (\S+) -->\n(.*?)\n<!-- /table -->", path.read_text(encoding="utf-8"),
                                      flags=re.S):
            csv_path = TABLES / f"{name}.csv"
            if not csv_path.exists():
                out.append(f"{path.name}: no CSV for table {name}")
                continue
            with open(csv_path, encoding="utf-8-sig") as f:
                want = [[c.strip() for c in row] for row in csv.reader(f)]
            lines = [ln for ln in block.splitlines() if ln.strip().startswith("|")]
            got = [[c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", ln.strip())[1:-1]]
                   for i, ln in enumerate(lines) if i != 1]
            if got != want:
                out.append(f"{path.name}: table {name} differs from its CSV (run src/round3/deck_tables.py)")
    return out


def check_report(path, heading, words_, source, forbidden):
    """Hard problems in a companion report: tables, captions, sources, numbering, citations, wording."""
    md = path.read_text(encoding="utf-8")
    body = md.rpartition("\n" + heading)[0]
    lines = body.splitlines()
    problems = []
    nonblank = [(i, ln.strip()) for i, ln in enumerate(lines) if ln.strip()]
    order = {i: k for k, (i, _) in enumerate(nonblank)}
    table_word, figure_word = words_
    numbers = {table_word: [], figure_word: []}
    for i, s in nonblank:
        k = order[i]
        if s.startswith("<!-- table:"):
            prev = nonblank[k - 1][1] if k else ""
            if not prev.startswith(f"**{table_word} "):
                problems.append(f"{path.name}: {s} has no caption line above it")
            end = next(j for j in range(k, len(nonblank)) if nonblank[j][1] == "<!-- /table -->")
            after = nonblank[end + 1][1] if end + 1 < len(nonblank) else ""
            if not after.startswith(source):
                problems.append(f"{path.name}: {s} has no '{source}' line below it")
        m = re.match(r"^!\[(\S+) (\d+)\. ", s)
        if m:
            numbers[figure_word].append(int(m.group(2)))
            after = nonblank[k + 1][1] if k + 1 < len(nonblank) else ""
            if not after.startswith(source):
                problems.append(f"{path.name}: figure {m.group(2)} has no '{source}' line below it")
        m = re.match(rf"^\*\*{table_word} (\d+)\.", s)
        if m:
            numbers[table_word].append(int(m.group(1)))
    for word, seen in numbers.items():
        if seen != list(range(1, len(seen) + 1)):
            problems.append(f"{path.name}: {word.lower()}s numbered {seen}, not 1 to {len(seen)} in order")
        cited = {int(n) for n in re.findall(rf"\b{word}s? (\d+)\b", body)}
        problems += [f"{path.name}: {word} {n} is cited but has no caption" for n in sorted(cited - set(seen))]
    problems += table_blocks_match_csv([path])
    missing, uncited = citations([path], heading)
    problems += [f"{path.name}: citation without a reference entry: {c}" for c in missing]
    if uncited:
        print(f"{path.name}: references never cited: " + "; ".join(uncited))
    phrases = forbidden if forbidden is not None else FORBIDDEN
    for part in re.split(r"^### ", body, flags=re.M):
        section = part.split(" ", 1)[0]
        for p in phrases:
            # boundary before the phrase, so "86 million" does not match "VND 0.86 million"
            if re.search(rf"(?<![\w.,]){re.escape(p)}", part, flags=re.I) and p not in REPORT_ALLOWED.get(section, set()):
                problems.append(f'{path.name}, section {section}: forbidden "{p}"')
    untranslated = TABLES / "vi" / "untranslated.csv"
    if "_vi" in path.stem and untranslated.exists():
        n = len(untranslated.read_text(encoding="utf-8").splitlines()) - 1
        if n > 0:
            problems.append(f"{path.name}: {n} table cells without a Vietnamese translation (tables/vi/untranslated.csv)")
    print(f"{path.name}: {len(numbers[table_word])} numbered tables, {len(numbers[figure_word])} figures, "
          f"{md.count('<!-- table:')} table blocks")
    return problems


def main():
    md = DECK.read_text(encoding="utf-8")
    problems, rows_out, notes_total = [], [], 0
    for n, name, body in slides(md):
        f = fields(body)
        title = words(f.get("Action title", ""))
        text = words(f.get("On-slide text", ""))
        notes = words(f.get("Speaker notes", ""))
        notes_total += len(notes)
        t_rows, t_cols = table_shape(f.get("Table", ""))
        has_table = t_rows > 0
        has_figure = ".png" in f.get("Figure", "")
        flags = []
        if len(title) > LIMITS["title"]:
            flags.append(f"title {len(title)} > {LIMITS['title']}")
        if n == 1:
            total = len(text) + table_words(f.get("Table", ""))
            warns_summary = f"summary {total} words"
            if total > LIMITS["summary"]:
                flags.append(f"summary {total} > {LIMITS['summary']}")
        elif len(text) > LIMITS["text"]:
            flags.append(f"text {len(text)} > {LIMITS['text']}")
        if t_rows > LIMITS["rows"] or t_cols > LIMITS["cols"]:
            flags.append(f"table {t_rows}x{t_cols} > {LIMITS['rows']}x{LIMITS['cols']}")
        if not (has_table or has_figure):
            flags.append("no table or figure")
        for key in ("Table", "Figure"):
            if (key == "Table" and has_table or key == "Figure" and has_figure) and "Source:" not in f.get(key, ""):
                flags.append(f"{key.lower()} without a Source line")
        for key in FIELDS[:3] + ["Speaker notes"]:
            if key not in f and key != "Table":
                flags.append(f"missing {key}")
        visible = " ".join(f.get(k, "") for k in ("Action title", "On-slide text", "Table", "Figure", "Speaker notes")).lower()
        flags += [f'forbidden "{p}"' for p in FORBIDDEN if p.lower() in visible and p not in ALLOWED.get(n, set())]
        warns = [f'check "{p}" (payroll only)' for p in MANUAL if p.lower() in visible]
        if n == 1:
            warns.append(warns_summary)
        if notes and not NOTES_RANGE[0] <= len(notes) <= NOTES_RANGE[1]:
            warns.append(f"notes {len(notes)} words (aim {NOTES_RANGE[0]}-{NOTES_RANGE[1]})")
        problems += [f"Slide {n}: {x}" for x in flags]
        rows_out.append((n, name, len(title), len(text), f"{t_rows}x{t_cols}" if has_table else "-",
                         "yes" if has_figure else "-", len(notes), "; ".join(flags + warns) or "ok"))
    print(f"{'#':>2}  {'slide':34s} {'title':>5} {'text':>5} {'table':>6} {'fig':>4} {'notes':>6}  check")
    for r in rows_out:
        print(f"{r[0]:>2}  {r[1][:34]:34s} {r[2]:>5} {r[3]:>5} {r[4]:>6} {r[5]:>4} {r[6]:>6}  {r[7]}")
    print(f"\nSpeaker notes: {notes_total} words, about {notes_total / 130:.1f} minutes at 130 words a minute.")
    if len(rows_out) != 15:
        problems.append(f"{len(rows_out)} main slides, expected 15")
    problems += table_blocks_match_csv([DECK, APPENDIX])
    missing, uncited = citations([DECK, APPENDIX])
    problems += [f"citation without a reference entry: {c}" for c in missing]
    if uncited:
        print("References never cited in the deck files: " + "; ".join(uncited))
    for report in REPORTS:
        if report[0].exists():
            problems += check_report(*report)
    if problems:
        print("\nHard limits broken:\n  " + "\n  ".join(problems))
        return 1
    print("All hard limits met.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
