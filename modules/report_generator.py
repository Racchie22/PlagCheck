
"""PDF report generation for PlagCheck."""

from io import BytesIO
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable,
)


def generate_pdf_report(
    comparison_type: str,
    source_name: str,
    target_name: str,
    similarity: float,
    matches: list,
) -> bytes:
    """
    Generate a PDF report for a PlagCheck comparison.

    Returns:
        PDF file content as bytes.
    """

    # Validate inputs
    if comparison_type not in {"Text", "Document"}:
        raise ValueError("Invalid comparison type.")

    if not isinstance(source_name, str) or not source_name.strip():
        raise ValueError("Source name cannot be empty.")

    if not isinstance(target_name, str) or not target_name.strip():
        raise ValueError("Target name cannot be empty.")

    if (
        isinstance(similarity, bool)
        or not isinstance(similarity, (int, float))
        or not 0 <= similarity <= 100
    ):
        raise ValueError("Similarity must be between 0 and 100.")

    if not isinstance(matches, list):
        raise TypeError("Matches must be a list.")

    # Create an in-memory PDF
    buffer = BytesIO()

    pdf = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm,
        title="PlagCheck Comparison Report",
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        fontSize=22,
        textColor=colors.HexColor("#183153"),
        alignment=TA_CENTER,
        spaceAfter=8,
    )

    heading_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontSize=13,
        textColor=colors.HexColor("#183153"),
        spaceBefore=12,
        spaceAfter=8,
    )

    normal_style = styles["BodyText"]

    story = []

    # Report heading
    story.append(Paragraph("PlagCheck", title_style))
    story.append(
        Paragraph("Smart Plagiarism Detection System", styles["Italic"])
    )
    story.append(Spacer(1, 8))

    story.append(Paragraph("Comparison Report", heading_style))
    story.append(
        Paragraph(
            f"Generated on: {datetime.now().strftime('%d %B %Y, %I:%M %p')}",
            normal_style,
        )
    )

    story.append(Spacer(1, 12))
    story.append(HRFlowable(width="100%", color=colors.grey))
    story.append(Spacer(1, 10))

    # Comparison details
    story.append(Paragraph("Comparison Details", heading_style))

    details = [
        ["Comparison Type", comparison_type],
        ["Source", source_name],
        ["Compared With", target_name],
        ["Similarity Score", f"{similarity:.2f}%"],
    ]

    details_table = Table(
        details,
        colWidths=[45 * mm, 115 * mm],
    )

    details_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#EAF0F6")),
            ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#183153")),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
            ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.lightgrey),
            ("PADDING", (0, 0), (-1, -1), 8),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ])
    )

    story.append(details_table)
    story.append(Spacer(1, 12))

    # Matching sentences
    story.append(Paragraph("Matching Sentences", heading_style))

    if matches:

        for index, match in enumerate(matches, start=1):

            required_keys = {
                "sentence_a",
                "sentence_b",
                "similarity",
            }

            if not isinstance(match, dict) or not required_keys.issubset(match):
                raise ValueError("Invalid matching sentence data.")

            match_score = match["similarity"]

            if (
                isinstance(match_score, bool)
                or not isinstance(match_score, (int, float))
                or not 0 <= match_score <= 100
            ):
                raise ValueError("Invalid sentence similarity score.")

            story.append(
                Paragraph(
                    f"<b>Match {index} - {match_score:.2f}% similar</b>",
                    normal_style,
                )
            )

            story.append(Spacer(1, 4))

            story.append(
                Paragraph(
                    f"<b>Text 1:</b> {match['sentence_a']}",
                    normal_style,
                )
            )

            story.append(Spacer(1, 4))

            story.append(
                Paragraph(
                    f"<b>Text 2:</b> {match['sentence_b']}",
                    normal_style,
                )
            )

            story.append(Spacer(1, 12))

    else:

        story.append(
            Paragraph(
                "No matching sentences were found.",
                normal_style,
            )
        )

    # Limitation note
    story.append(Paragraph("Important Limitation", heading_style))

    story.append(
        Paragraph(
            "The similarity score indicates textual overlap. "
            "It does not prove that plagiarism has occurred. "
            "PlagCheck uses TF-IDF and cosine similarity, which may "
            "not identify paraphrased content or semantic similarities. "
            "Results should be reviewed by a human.",
            normal_style,
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Generated by PlagCheck",
            ParagraphStyle(
                "Footer",
                parent=normal_style,
                alignment=TA_CENTER,
                textColor=colors.grey,
            ),
        )
    )

    # Build PDF
    pdf.build(story)

    return buffer.getvalue()
