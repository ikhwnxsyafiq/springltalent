def generate_ai_feedback(result):

    domain_scores = result.get(
        "domain_scores",
        {}
    )

    domain_names = {
        "digital_design": "Digital Design",
        "analog_design": "Analog Design",
        "backend": "Physical Design",
        "mixed_signal": "Mixed Signal",
        "verification": "Verification",
        "eda_tools": "EDA Tools"
    }

    strengths = []
    weaknesses = []

    for domain, score in domain_scores.items():

        display_name = domain_names.get(
            domain,
            domain
        )

        if score >= 70:
            strengths.append(display_name)
        else:
            weaknesses.append(display_name)

    if strengths:

        strengths_text = (
            "Candidate demonstrates strong capability in "
            + ", ".join(strengths)
            + "."
        )

    else:

        strengths_text = (
            "No significant strengths identified from the assessment."
        )

    if weaknesses:

        weaknesses_text = (
            "Further development is recommended in "
            + ", ".join(weaknesses)
            + "."
        )

    else:

        weaknesses_text = (
            "Candidate demonstrates balanced performance across evaluated domains."
        )

    roadmap = []

    learning_map = {
        "digital_design":
            "Advanced RTL Design and FPGA Development",

        "analog_design":
            "Analog Circuit Design Fundamentals",

        "backend":
            "Physical Design and Timing Closure",

        "mixed_signal":
            "Mixed Signal Design Methodologies",

        "verification":
            "SystemVerilog and UVM Verification",

        "eda_tools":
            "EDA Automation and Scripting"
    }

    for domain, score in domain_scores.items():

        if score < 70:

            recommendation = learning_map.get(
                domain
            )

            if recommendation:
                roadmap.append(
                    recommendation
                )

    hiring_targets = [
        "Spring Semiconductor",
        "Intel Malaysia",
        "Oppstar Technology",
        "SkyeChip",
        "Infineon Technologies"
    ]

    return {
        "core_strengths": strengths_text,
        "growth_areas": weaknesses_text,
        "roadmap": roadmap,
        "hiring_targets": hiring_targets
    }