import os
from docx import Document
from docx.shared import Pt, Inches
from fpdf import FPDF  # fpdf2

# --- CONFIG ---
FONT_NAME_DOCX = "Calibri"   # DOCX uses Calibri
FONT_SIZE = 10
MARGIN = 0.5  # inches

DOCX_ROOT = r"C:\Users\arnab\Desktop\Career\knowledge_base\Automation\Docx"
PDF_ROOT = r"C:\Users\arnab\Desktop\Career\knowledge_base\Automation\PDF"

# Use Arial.ttf (present on all Windows systems)
UNICODE_FONT_PATH = r"C:\Windows\Fonts\arial.ttf"

def md_to_docx(md_file, output_dir):
    with open(md_file, "r", encoding="utf-8") as f:
        text = f.read()

    lines = text.splitlines()
    doc = Document()

    for section in doc.sections:
        section.top_margin = Inches(MARGIN)
        section.bottom_margin = Inches(MARGIN)
        section.left_margin = Inches(MARGIN)
        section.right_margin = Inches(MARGIN)

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.startswith("#"):
            doc.add_heading(line.lstrip("#").strip(), level=1)
        elif line.startswith("- "):
            para = doc.add_paragraph(line[2:].strip(), style="List Bullet")
            run = para.runs[0]; run.font.name = FONT_NAME_DOCX; run.font.size = Pt(FONT_SIZE)
        elif line[0].isdigit() and line[1:3] == ". ":
            para = doc.add_paragraph(line[3:].strip(), style="List Number")
            run = para.runs[0]; run.font.name = FONT_NAME_DOCX; run.font.size = Pt(FONT_SIZE)
        else:
            para = doc.add_paragraph(line)
            run = para.runs[0]; run.font.name = FONT_NAME_DOCX; run.font.size = Pt(FONT_SIZE)

    filename = os.path.splitext(os.path.basename(md_file))[0] + ".docx"
    out_path = os.path.join(output_dir, filename)
    doc.save(out_path)
    return out_path


def combine_docx_to_pdf(docx_files, output_pdf):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=10)

    # Register and use Arial.ttf
    pdf.add_font("ArialUnicode", "", UNICODE_FONT_PATH)
    pdf.set_font("ArialUnicode", size=FONT_SIZE)

    for docx_file in docx_files:
        doc = Document(docx_file)
        pdf.add_page()
        pdf.set_font("ArialUnicode", size=FONT_SIZE)

        num_counter = 1
        for para in doc.paragraphs:
            text = para.text.strip()
            if not text:
                continue
            style = para.style.name
            if style.startswith("List Bullet"):
                pdf.multi_cell(0, 10, f"• {text}")  # bullet works with Arial.ttf
            elif style.startswith("List Number"):
                pdf.multi_cell(0, 10, f"{num_counter}. {text}")
                num_counter += 1
            else:
                pdf.multi_cell(0, 10, text)

    pdf.output(output_pdf)


def process_folder(md_folder):
    parent_name = os.path.basename(md_folder.rstrip("\\/"))
    docx_out_dir = os.path.join(DOCX_ROOT, parent_name)
    pdf_out_dir = PDF_ROOT
    os.makedirs(docx_out_dir, exist_ok=True)
    os.makedirs(pdf_out_dir, exist_ok=True)

    docx_files = []
    for root, _, files in os.walk(md_folder):
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)
                docx_path = md_to_docx(md_path, docx_out_dir)
                docx_files.append(docx_path)

    pdf_path = os.path.join(pdf_out_dir, f"{parent_name}.pdf")
    combine_docx_to_pdf(docx_files, pdf_path)
    print(f"✅ Done. PDF saved at: {pdf_path}")


if __name__ == "__main__":
    md_folder = input("Enter the path to your .md folder: ").strip()
    process_folder(md_folder)
