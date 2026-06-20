from io import BytesIO
import os

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle,
    Image
)

from app.models.candidate import Candidate

DOMAIN_LABELS = {
    "digital_design": "Digital Design",
    "analog_design": "Analog Design",
    "backend": "Physical Design",
    "mixed_signal": "Mixed Signal",
    "verification": "Verification",
    "eda_tools": "EDA Tools"
}


def generate_pdf_report(
    session_id: int,
    report_data: dict,
    candidate: Candidate = None
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    recommendation = report_data.get(
        "recommendation",
        {}
    )

    skill_levels = report_data.get(
        "skill_levels",
        []
    )

    skill_gaps = report_data.get(
        "skill_gaps",
        []
    )

    domain_scores = report_data.get(
        "domain_scores",
        {}
    )

    ai_feedback = report_data.get(
        "ai_feedback",
        {}
    )

    # =====================
    # PAGE 1
    # =====================

    logo_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "assets",
            "logo_springsemi.png"
        )
    )

    if os.path.exists(logo_path):
        elements.append(
            Image(
                logo_path,
                width=220,
                height=80
            )
        )

    elements.append(Spacer(1, 10))

    elements.append(
        Paragraph(
            "SPRINGTALENT",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(
            "IC Design Talent Assessment Report",
            styles["Heading2"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )
    # =====================
    # Candidate Information
    # =====================

    if candidate:

        elements.append(
            Paragraph(
                "Candidate Information",
                styles["Heading2"]
            )
        )

        candidate_table = Table(
            [
                ["Field", "Value"],
                ["Full Name", candidate.full_name],
                ["Email", candidate.email or "-"],
                ["University", candidate.university or "-"],
                ["Programme", candidate.programme or "-"],
                ["CGPA",candidate.cgpa or "-"],
                ["Graduation Year", candidate.graduation_year or "-"]
            ],
            colWidths=[150, 290]
        )
        
        candidate_table.setStyle(
            TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0B4F9C")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold")
            ])
        )

        elements.append(candidate_table)

        elements.append(
            Spacer(1, 20)
        )
    # =====================
    # Assessment Summary
    # =====================

    assessment_table = Table(
        [
            ["Assessment Summary", ""],
            ["Session ID", str(session_id)],
            ["Overall Score", f"{report_data.get('overall_score', 0)}%"],
            ["Correct Answers", str(report_data.get('correct_answers', 0))],
            ["Total Questions", str(report_data.get('total_questions', 0))]
        ],
        colWidths=[200, 240]
    )

    assessment_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0B4F9C")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("SPAN", (0, 0), (1, 0)),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold")
        ])
    )

    elements.append(
        assessment_table
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "Executive Summary",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Recommended Role: {recommendation.get('recommended_role', '-')}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Career Fit Score: {recommendation.get('career_fit_score', 0)}%",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Assessment Confidence: {recommendation.get('assessment_confidence', '-')}",
            styles["Normal"]
        )
    )

    elements.append(
        PageBreak()
    )

    # =====================
    # PAGE 2
    # =====================

    elements.append(
        Paragraph(
            "Skill Matrix",
            styles["Heading1"]
        )
    )

    skill_table_data = [
        ["Skill", "Score", "Level"]
    ]

    for skill in skill_levels:

        skill_table_data.append([
            skill.get("skill", "-"),
            str(skill.get("score", 0)),
            skill.get("level", "-")
        ])

    skill_table = Table(
        skill_table_data,
        colWidths=[220, 80, 120]
    )

    skill_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0B4F9C")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ])
    )

    elements.append(skill_table)

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "Domain Scores",
            styles["Heading2"]
        )
    )

    domain_table_data = [
        ["Domain", "Score"]
    ]

    for domain, score in domain_scores.items():

        domain_table_data.append([
            DOMAIN_LABELS.get(domain, domain),
            f"{score}%"
        ])

    domain_table = Table(
        domain_table_data,
        colWidths=[300, 120]
    )

    domain_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0B4F9C")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ])
    )

    elements.append(domain_table)

    elements.append(
        PageBreak()
    )

    # =====================
    # PAGE 3
    # =====================

    elements.append(
        Paragraph(
            "Career Recommendation",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            recommendation.get(
                "summary",
                "-"
            ),
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "Alternative Roles",
            styles["Heading2"]
        )
    )

    for role in recommendation.get(
        "alternative_roles",
        []
    ):

        elements.append(
            Paragraph(
                f"{role['role']} ({role['score']}%)",
                styles["Normal"]
            )
        )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "Learning Recommendations",
            styles["Heading2"]
        )
    )

    for item in recommendation.get(
        "learning_recommendations",
        []
    ):

        elements.append(
            Paragraph(
                item,
                styles["Normal"]
            )
        )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "Skill Gap Analysis",
            styles["Heading2"]
        )
    )

    gap_table_data = [
        ["Skill", "Current", "Target", "Gap"]
    ]

    for gap in skill_gaps:

        gap_table_data.append([
            gap.get("skill", "-"),
            str(gap.get("current_score", 0)),
            str(gap.get("target_score", 0)),
            str(gap.get("gap", 0))
        ])

    gap_table = Table(
        gap_table_data,
        colWidths=[170, 80, 80, 80]
    )

    gap_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0B4F9C")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ])
    )

    elements.append(gap_table)

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "AI Career Feedback",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Core Strengths:</b><br/>{ai_feedback.get('core_strengths', '-')}",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 10)
    )

    elements.append(
        Paragraph(
            f"<b>Growth Areas:</b><br/>{ai_feedback.get('growth_areas', '-')}",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "Learning Roadmap",
            styles["Heading2"]
        )
    )

    for item in ai_feedback.get(
        "roadmap",
        []
    ):

        elements.append(
            Paragraph(
                f"• {item}",
                styles["Normal"]
            )
        )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "Hiring Targets",
            styles["Heading2"]
        )
    )

    for company in ai_feedback.get(
        "hiring_targets",
        []
    ):

        elements.append(
            Paragraph(
                f"• {company}",
                styles["Normal"]
            )
        )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "Recruiter Notes",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            "__________________________",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            "__________________________",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            "__________________________",
            styles["Normal"]
        )
    )

    doc.build(elements)

    buffer.seek(0)

    return buffer