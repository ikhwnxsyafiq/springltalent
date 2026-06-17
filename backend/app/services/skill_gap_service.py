TARGET_SCORE = 70


def generate_skill_gaps(result):

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

    gaps = []

    for domain, score in domain_scores.items():

        if score >= TARGET_SCORE:
            continue

        gap = TARGET_SCORE - score

        gaps.append(
            {
                "skill": skill_names.get(
                    domain,
                    domain
                ),
                "current_score": score,
                "target_score": TARGET_SCORE,
                "gap": gap
            }
        )

    gaps.sort(
        key=lambda x: x["gap"],
        reverse=True
    )

    return gaps