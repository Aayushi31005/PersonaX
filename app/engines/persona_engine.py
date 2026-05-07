from copy import deepcopy

from app.models.persona import Persona
from app.models.behavior import BehaviorConfig


BASE_BEHAVIOR = {
    "click_delay": 1.0,
    "read_probability": 0.5,
    "error_probability": 0.1,
    "abandon_threshold": 5,
}


def generate_behavior_config(persona: Persona) -> BehaviorConfig:
    """
    Converts persona traits into simulation-ready behavior configuration.
    """

    config = deepcopy(BASE_BEHAVIOR)

    for trait in persona.traits:

        # ---------------------------
        # Impatient Users
        # ---------------------------
        if trait == "impatient":
            config["click_delay"] *= 0.7
            config["abandon_threshold"] -= 2

        # ---------------------------
        # Beginner Users
        # ---------------------------
        elif trait == "beginner":
            config["read_probability"] += 0.3
            config["click_delay"] *= 1.2

        # ---------------------------
        # Careless Users
        # ---------------------------
        elif trait == "careless":
            config["error_probability"] += 0.2

        # ---------------------------
        # Careful Users
        # ---------------------------
        elif trait == "careful":
            config["error_probability"] -= 0.05
            config["read_probability"] += 0.2

        # ---------------------------
        # Analytical Users
        # ---------------------------
        elif trait == "analytical":
            config["read_probability"] += 0.4
            config["click_delay"] *= 1.3

    # ---------------------------
    # Clamp Values
    # ---------------------------

    config["read_probability"] = min(
        max(config["read_probability"], 0),
        1,
    )

    config["error_probability"] = min(
        max(config["error_probability"], 0),
        1,
    )

    config["abandon_threshold"] = max(
        config["abandon_threshold"],
        0,
    )

    return BehaviorConfig(**config)