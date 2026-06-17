def get_skill_level(score):

    if score >= 85:
        return "Expert"

    if score >= 70:
        return "Advanced"

    if score >= 50:
        return "Intermediate"

    return "Beginner"


def generate_skill_levels(result):

    domain_scores = result.get(
        "domain_scores",
        {}
    )

    skill_names = {
        "digital_design": "Digital Design",
        "analog_design": "Analog Design",
        "backend": "Backend",
        "mixed_signal": "Mixed Signal",
        "verification": "Verification",
        "eda_tools": "EDA Tools"
    }

    skills = []

    for domain, score in domain_scores.items():

        skills.append(
            {
                "skill": skill_names.get(
                    domain,
                    domain
                ),
                "score": score,
                "level": get_skill_level(score)
            }
        )

    return skills