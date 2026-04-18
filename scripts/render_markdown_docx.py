from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


INPUT_PATH = Path(
    r"C:\Users\jewoo\Documents\Playground\moodle-install\codex-collaboration-tutorial-en-generic-elearning.md"
)
OUTPUT_PATH = Path(
    r"C:\Users\jewoo\Documents\Playground\moodle-install\codex-collaboration-tutorial-en-generic-elearning.docx"
)


HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
BULLET_RE = re.compile(r"^\s*-\s+(.*)$")
NUMBER_RE = re.compile(r"^\s*(\d+)\.\s+(.*)$")


def add_field_run(paragraph, field_code: str):
    run = paragraph.add_run()
    fld_char_begin = OxmlElement("w:fldChar")
    fld_char_begin.set(qn("w:fldCharType"), "begin")

    instr_text = OxmlElement("w:instrText")
    instr_text.set(qn("xml:space"), "preserve")
    instr_text.text = field_code

    fld_char_separate = OxmlElement("w:fldChar")
    fld_char_separate.set(qn("w:fldCharType"), "separate")

    placeholder = OxmlElement("w:t")
    placeholder.text = "Right-click to update field."

    fld_char_end = OxmlElement("w:fldChar")
    fld_char_end.set(qn("w:fldCharType"), "end")

    run._r.append(fld_char_begin)
    run._r.append(instr_text)
    run._r.append(fld_char_separate)
    run._r.append(placeholder)
    run._r.append(fld_char_end)
    return run


def set_cell_text(cell, text, bold=False):
    cell.text = ""
    paragraph = cell.paragraphs[0]
    run = paragraph.add_run(text)
    run.bold = bold
    run.font.size = Pt(10.5)


def set_cell_shading(cell, fill: str):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def configure_page(section):
    section.top_margin = Inches(0.85)
    section.bottom_margin = Inches(0.75)
    section.left_margin = Inches(0.9)
    section.right_margin = Inches(0.9)
    section.header_distance = Inches(0.35)
    section.footer_distance = Inches(0.35)


def ensure_styles(document: Document):
    styles = document.styles

    normal = styles["Normal"]
    normal.font.name = "Aptos"
    normal.font.size = Pt(10.5)

    heading1 = styles["Heading 1"]
    heading1.font.name = "Aptos Display"
    heading1.font.size = Pt(18)
    heading1.font.bold = True
    heading1.font.color.rgb = RGBColor(23, 54, 93)

    heading2 = styles["Heading 2"]
    heading2.font.name = "Aptos Display"
    heading2.font.size = Pt(14)
    heading2.font.bold = True
    heading2.font.color.rgb = RGBColor(31, 78, 121)

    heading3 = styles["Heading 3"]
    heading3.font.name = "Aptos"
    heading3.font.size = Pt(11.5)
    heading3.font.bold = True
    heading3.font.color.rgb = RGBColor(55, 55, 55)

    if "Code Block" not in styles:
        code_style = styles.add_style("Code Block", WD_STYLE_TYPE.PARAGRAPH)
        code_style.base_style = styles["Normal"]
        code_style.font.name = "Consolas"
        code_style.font.size = Pt(9.5)
        code_style.paragraph_format.left_indent = Inches(0.2)
        code_style.paragraph_format.right_indent = Inches(0.1)
        code_style.paragraph_format.space_before = Pt(6)
        code_style.paragraph_format.space_after = Pt(6)

    if "Body Text Tight" not in styles:
        tight_style = styles.add_style("Body Text Tight", WD_STYLE_TYPE.PARAGRAPH)
        tight_style.base_style = styles["Normal"]
        tight_style.font.name = "Aptos"
        tight_style.font.size = Pt(10.5)
        tight_style.paragraph_format.space_before = Pt(0)
        tight_style.paragraph_format.space_after = Pt(4)


def add_header_footer(section, document_title: str):
    header = section.header
    header_para = header.paragraphs[0]
    header_para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = header_para.add_run(document_title)
    run.font.name = "Aptos"
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(91, 103, 112)

    footer = section.footer
    footer_para = footer.paragraphs[0]
    footer_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = footer_para.add_run("Page ")
    run.font.size = Pt(9)
    add_field_run(footer_para, "PAGE")


def set_paragraph_border(paragraph):
    p_pr = paragraph._p.get_or_add_pPr()
    p_bdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "D9E2F3")
    p_bdr.append(bottom)
    p_pr.append(p_bdr)


def add_inline_runs(paragraph, text: str):
    parts = re.split(r"(`[^`]+`)", text)
    for part in parts:
        if not part:
            continue
        if part.startswith("`") and part.endswith("`") and len(part) >= 2:
            run = paragraph.add_run(part[1:-1])
            run.font.name = "Consolas"
            run.font.size = Pt(9.5)
        else:
            paragraph.add_run(part)


def add_cover_page(document: Document, title: str, subtitle: str):
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
    paragraph.paragraph_format.space_before = Pt(80)
    run = paragraph.add_run(title)
    run.font.name = "Aptos Display"
    run.font.size = Pt(24)
    run.bold = True
    run.font.color.rgb = RGBColor(23, 54, 93)

    sub = document.add_paragraph()
    sub.alignment = WD_ALIGN_PARAGRAPH.LEFT
    sub.paragraph_format.space_after = Pt(22)
    run = sub.add_run(subtitle)
    run.font.name = "Aptos"
    run.font.size = Pt(13)
    run.italic = True
    run.font.color.rgb = RGBColor(68, 84, 106)

    banner = document.add_paragraph()
    banner.paragraph_format.space_after = Pt(10)
    banner_run = banner.add_run("Prepared as a reusable build and packaging guide for interactive e-learning content.")
    banner_run.font.name = "Aptos"
    banner_run.font.size = Pt(10.5)
    banner_run.font.color.rgb = RGBColor(85, 85, 85)

    table = document.add_table(rows=4, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.style = "Table Grid"
    labels = [
        ("Document Type", "Technical tutorial / workflow guide"),
        ("Format", "Formal Word document (.docx)"),
        ("Primary Scope", "Interactive e-learning content, SCORM packaging, and web deployment"),
        ("Generated", datetime.now().strftime("%B %d, %Y")),
    ]
    for row, (label, value) in zip(table.rows, labels):
        set_cell_text(row.cells[0], label, bold=True)
        set_cell_text(row.cells[1], value)
        set_cell_shading(row.cells[0], "EAF0F9")

    document.add_paragraph("")
    note = document.add_paragraph(style="Body Text Tight")
    add_inline_runs(
        note,
        "This Word version is based on the canonical source file "
        f"`{INPUT_PATH.name}` and is intended for formal sharing, workshop handouts, and project documentation.",
    )
    document.add_page_break()


def add_toc(document: Document):
    heading = document.add_paragraph("Table of Contents", style="Heading 1")
    heading.paragraph_format.space_after = Pt(6)
    para = document.add_paragraph()
    add_field_run(para, r'TOC \\o "1-3" \\h \\z \\u')
    document.add_page_break()


def add_intro_box(document: Document):
    table = document.add_table(rows=1, cols=1)
    table.style = "Table Grid"
    cell = table.rows[0].cells[0]
    set_cell_shading(cell, "F4F7FB")
    para = cell.paragraphs[0]
    para.style = document.styles["Body Text Tight"]
    add_inline_runs(
        para,
        "Reader note: this document is designed as a practical, reusable playbook. "
        "The headings used in the explanatory sections intentionally match the headings used in the prompt templates. "
        "That alignment is a core methodological point, not only a formatting preference.",
    )
    document.add_paragraph("")


def add_code_block(document: Document, code_lines: list[str]):
    para = document.add_paragraph(style="Code Block")
    set_paragraph_border(para)
    for idx, line in enumerate(code_lines):
        run = para.add_run(line)
        run.font.name = "Consolas"
        run.font.size = Pt(9.5)
        if idx < len(code_lines) - 1:
            run.add_break(WD_BREAK.LINE)


def flush_paragraph_buffer(document: Document, buffer: list[str]):
    if not buffer:
        return
    text = " ".join(line.strip() for line in buffer if line.strip())
    if text:
        para = document.add_paragraph(style="Normal")
        para.paragraph_format.space_after = Pt(6)
        add_inline_runs(para, text)
    buffer.clear()


def render_markdown_body(document: Document, lines: list[str]):
    buffer: list[str] = []
    in_code = False
    code_lines: list[str] = []

    for raw_line in lines:
        line = raw_line.rstrip("\n")
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_paragraph_buffer(document, buffer)
            if not in_code:
                in_code = True
                code_lines = []
            else:
                in_code = False
                add_code_block(document, code_lines)
                code_lines = []
            continue

        if in_code:
            code_lines.append(line)
            continue

        if not stripped:
            flush_paragraph_buffer(document, buffer)
            continue

        heading_match = HEADING_RE.match(stripped)
        if heading_match:
            flush_paragraph_buffer(document, buffer)
            level = min(len(heading_match.group(1)), 3)
            text = heading_match.group(2).strip()
            para = document.add_paragraph(text, style=f"Heading {level}")
            if level == 1:
                para.paragraph_format.space_before = Pt(10)
            continue

        if stripped in {"---", "***"}:
            flush_paragraph_buffer(document, buffer)
            divider = document.add_paragraph("")
            set_paragraph_border(divider)
            continue

        bullet_match = BULLET_RE.match(line)
        if bullet_match:
            flush_paragraph_buffer(document, buffer)
            para = document.add_paragraph(style="List Bullet")
            add_inline_runs(para, bullet_match.group(1).strip())
            continue

        number_match = NUMBER_RE.match(line)
        if number_match:
            flush_paragraph_buffer(document, buffer)
            para = document.add_paragraph(style="List Number")
            add_inline_runs(para, number_match.group(2).strip())
            continue

        buffer.append(line)

    flush_paragraph_buffer(document, buffer)


def extract_title_and_subtitle(lines: list[str]) -> tuple[str, str, list[str]]:
    title = "Codex Collaboration Tutorial"
    subtitle = "Formal documentation export"
    body_start = 0

    for idx, line in enumerate(lines):
        heading_match = HEADING_RE.match(line.strip())
        if heading_match and len(heading_match.group(1)) == 1:
            title = heading_match.group(2).strip()
            body_start = idx + 1
            break

    for idx in range(body_start, len(lines)):
        heading_match = HEADING_RE.match(lines[idx].strip())
        if heading_match and len(heading_match.group(1)) == 2:
            subtitle = heading_match.group(2).strip()
            body_start = idx + 1
            break

    body_lines = lines[body_start:]
    return title, subtitle, body_lines


def build_docx():
    lines = INPUT_PATH.read_text(encoding="utf-8").splitlines()
    title, subtitle, body_lines = extract_title_and_subtitle(lines)

    document = Document()
    configure_page(document.sections[0])
    ensure_styles(document)
    document.core_properties.title = title
    document.core_properties.subject = subtitle
    document.core_properties.author = "Codex"
    document.core_properties.comments = "Generated from the canonical markdown tutorial source."

    add_cover_page(document, title, subtitle)

    section = document.sections[-1]
    configure_page(section)
    add_header_footer(section, title)
    add_toc(document)
    add_intro_box(document)
    render_markdown_body(document, body_lines)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    document.save(str(OUTPUT_PATH))
    print(OUTPUT_PATH)


if __name__ == "__main__":
    build_docx()
