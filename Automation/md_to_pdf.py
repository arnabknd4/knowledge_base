import os
import markdown
from docx import Document
from docx.shared import Pt, Inches
from fpdf import FPDF

# --- CONFIG ---
FONT_NAME = "Calibri"
FONT_SIZE = 10
MARGIN = 0.5  # inches

DOCX_ROOT = r"C:\Users\arnab\Desktop\Career\knowledge_base\Automation\Docx"
PDF_ROOT = r"C:\Users\arnab\Desktop\Career\knowledge_base\Automation\PDF"

def md_to_docx(md_file, output_dir):
    """Convert a single .md file to .docx"""
    with open(md_file, "r", encoding="utf-8") as f:
        text = f.read()

    html = markdown.markdown(text)
    doc = Document()

    # Set narrow margins
    for section in doc.sections:
        section.top_margin = Inches(MARGIN)
        section.bottom_margin = Inches(MARGIN)
        section.left_margin = Inches(MARGIN)
        section.right_margin = Inches(MARGIN)

    # Add content
    p = doc.add_paragraph()
    run = p.add_run(html)
    run.font.name = FONT_NAME
    run.font.size = Pt(FONT_SIZE)

    # Save DOCX
    filename = os.path.splitext(os.path.basename(md_file))[0] + ".docx"
    out_path = os.path.join(output_dir, filename)
    doc.save(out_path)
    return out_path


def combine_docx_to_pdf(docx_files, output_pdf):
    """Combine multiple DOCX files into one PDF"""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.set_font(FONT_NAME, size=FONT_SIZE)

    for docx_file in docx_files:
        doc = Document(docx_file)
        pdf.add_page()
        for para in doc.paragraphs:
            pdf.multi_cell(0, 10, para.text)

    pdf.output(output_pdf)


def process_folder(md_folder):
    """Main pipeline: MD → DOCX → PDF, preserving parent folder names"""
    parent_name = os.path.basename(md_folder.rstrip("\\/"))

    # Create output subfolders
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

    # Combine into single PDF
    pdf_path = os.path.join(pdf_out_dir, f"{parent_name}.pdf")
    combine_docx_to_pdf(docx_files, pdf_path)
    print(f"✅ Done. PDF saved at: {pdf_path}")


# --- RUN ---
if __name__ == "__main__":
    md_folder = input("Enter the path to your .md folder: ").strip()
    process_folder(md_folder)
