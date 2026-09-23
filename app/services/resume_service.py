from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from app.schemas.resume import ResumeRequest


OUTPUT_DIR = Path("generated")
OUTPUT_DIR.mkdir(exist_ok=True)


def generate_resume(data: ResumeRequest) -> Path:

    output_path = OUTPUT_DIR / "resume.pdf"

    pdf = canvas.Canvas(
        str(output_path),
        pagesize=A4
    )

    width, height = A4

    # Name
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(50, height - 60, data.name)

    # Contact information
    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, height - 85, data.email)
    pdf.drawString(50, height - 100, data.phone)

    # Summary
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, height - 140, "Summary")

    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, height - 160, data.summary)

    pdf.save()

    return output_path
