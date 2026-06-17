from app.services.result_service import (
    calculate_assessment_result
)

from app.services.recommendation_service import (
    generate_recommendation
)

from app.services.skill_mapping_service import (
    generate_skill_mapping
)

from app.services.skill_level_service import (
    generate_skill_levels
)

from app.services.skill_gap_service import (
    generate_skill_gaps
)

from app.services.ai_feedback_service import (
    generate_ai_feedback
)


def generate_assessment_report(
    db,
    session_id
):

    result = calculate_assessment_result(
        db=db,
        session_id=session_id
    )

    recommendation = generate_recommendation(
        result
    )

    skill_mapping = generate_skill_mapping(
        result
    )

    skill_levels = generate_skill_levels(
        result
    )

    skill_gaps = generate_skill_gaps(
        result
    )

    ai_feedback = generate_ai_feedback(
        result
    )

    result["recommendation"] = recommendation
    result["skill_mapping"] = skill_mapping
    result["skill_levels"] = skill_levels
    result["skill_gaps"] = skill_gaps
    result["ai_feedback"] = ai_feedback

    return result