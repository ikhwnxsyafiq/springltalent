from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    session_id: int,
    report_data: dict
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer
    )

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

    # =====================
    # PAGE 1
    # =====================

    elements.append(
        Paragraph(
            "SPRINGTALENT",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(
            "Talent Assessment Report",
            styles["Heading2"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            f"Assessment Session ID: {session_id}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Overall Score: {report_data.get('overall_score', 0)}%",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Correct Answers: {report_data.get('correct_answers', 0)}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Questions: {report_data.get('total_questions', 0)}",
            styles["Normal"]
        )
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

    for skill in skill_levels:

        elements.append(
            Paragraph(
                f"{skill['skill']} - "
                f"Score: {skill['score']} - "
                f"Level: {skill['level']}",
                styles["Normal"]
            )
        )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "Domain Scores",
            styles["Heading2"]
        )
    )

    for domain, score in domain_scores.items():

        elements.append(
            Paragraph(
                f"{domain}: {score}%",
                styles["Normal"]
            )
        )

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

    for gap in skill_gaps:

        elements.append(
            Paragraph(
                f"{gap['skill']} | "
                f"Current: {gap['current_score']} | "
                f"Target: {gap['target_score']} | "
                f"Gap: {gap['gap']}",
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