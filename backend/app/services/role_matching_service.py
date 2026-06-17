ROLE_MATRIX = {
    "RTL Design Engineer": {
        "digital_design": 0.40,
        "verification": 0.25,
        "eda_tools": 0.20,
        "backend": 0.15
    },

    "Verification Engineer": {
        "verification": 0.50,
        "digital_design": 0.20,
        "eda_tools": 0.15,
        "backend": 0.15
    },

    "Physical Design Engineer": {
        "backend": 0.50,
        "eda_tools": 0.25,
        "digital_design": 0.15,
        "verification": 0.10
    },

    "Mixed Signal Engineer": {
        "mixed_signal": 0.50,
        "analog_design": 0.30,
        "eda_tools": 0.20
    },

    "Analog IC Design Engineer": {
        "analog_design": 0.60,
        "mixed_signal": 0.25,
        "eda_tools": 0.15
    },

    "EDA Engineer": {
        "eda_tools": 0.50,
        "backend": 0.20,
        "verification": 0.15,
        "digital_design": 0.15
    }
}


def calculate_role_fit(domain_scores):

    role_scores = {}

    for role, weights in ROLE_MATRIX.items():

        score = 0

        for domain, weight in weights.items():

            domain_score = domain_scores.get(
                domain,
                0
            )

            score += (
                domain_score * weight
            )

        role_scores[role] = round(
            score,
            2
        )

    sorted_roles = sorted(
        role_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_roles