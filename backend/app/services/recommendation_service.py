from app.services.role_matching_service import (
    calculate_role_fit
)


DISPLAY_NAMES = {
    "digital_design": "Digital Design",
    "analog_design": "Analog Design",
    "backend": "Physical Design",
    "mixed_signal": "Mixed Signal",
    "verification": "Verification",
    "eda_tools": "EDA Tools"
}


def generate_recommendation(result):

    domain_scores = result.get(
        "domain_scores",
        {}
    )

    if not domain_scores:
        return {
            "recommended_role": "Unknown",
            "career_fit_score": 0,
            "assessment_confidence": "Low",
            "alternative_roles": [],
            "strengths": [],
            "weaknesses": [],
            "learning_recommendations": [],
            "summary": "Not enough assessment data."
        }

    sorted_high = sorted(
        domain_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    sorted_low = sorted(
        domain_scores.items(),
        key=lambda x: x[1]
    )

    strengths = []

    for domain, score in sorted_high:

        if score >= 70:

            strengths.append(
                DISPLAY_NAMES.get(
                    domain,
                    domain
                )
            )

    weaknesses = []

    for domain, score in sorted_low:

        if score < 70:

            weaknesses.append(
                DISPLAY_NAMES.get(
                    domain,
                    domain
                )
            )

    learning_mapping = {
        "digital_design":
            "Advanced RTL Design and FPGA Development",

        "analog_design":
            "Analog Circuit Design Fundamentals",

        "backend":
            "Physical Design and Timing Closure",

        "mixed_signal":
            "Mixed Signal Design Fundamentals",

        "verification":
            "SystemVerilog and UVM Verification",

        "eda_tools":
            "EDA Automation and Scripting"
    }

    role_matches = calculate_role_fit(
        domain_scores
    )

    recommended_role = role_matches[0][0]

    career_fit_score = role_matches[0][1]

    answered_questions = result.get(
        "total_questions",
        0
    )

    if answered_questions < 10:

        assessment_confidence = "Low"

    elif answered_questions < 30:

        assessment_confidence = "Medium"

    else:

        assessment_confidence = "High"

    alternative_roles = []

    for role, score in role_matches[1:4]:

        alternative_roles.append(
            {
                "role": role,
                "score": score
            }
        )

    learning_recommendations = []

    for domain, score in domain_scores.items():

        if score < 70:

            recommendation = learning_mapping.get(
                domain
            )

            if recommendation:

                learning_recommendations.append(
                    recommendation
                )

    if strengths:

        strengths_text = ", ".join(strengths)

    else:

        strengths_text = "No significant strengths identified"

    if weaknesses:

        weaknesses_text = ", ".join(weaknesses)

    else:

        weaknesses_text = "No major skill gaps identified"

    summary = (
        f"The candidate is most suitable for the role of "
        f"{recommended_role} with a career fit score of "
        f"{career_fit_score}%. "
        f"Assessment confidence is rated as "
        f"{assessment_confidence}. "
        f"Key strengths include {strengths_text}. "
        f"Areas for further development include "
        f"{weaknesses_text}."
    )

    return {
        "recommended_role": recommended_role,
        "career_fit_score": career_fit_score,
        "assessment_confidence": assessment_confidence,
        "alternative_roles": alternative_roles,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "learning_recommendations": learning_recommendations,
        "summary": summary
    }