def generate_skill_mapping(result):

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

    radar_chart = []

    for domain, score in domain_scores.items():

        radar_chart.append(
            {
                "skill": skill_names.get(
                    domain,
                    domain
                ),
                "score": score
            }
        )

    return {
        "radar_chart": radar_chart
    }