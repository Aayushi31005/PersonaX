from app.models.persona import Persona
from app.engines.persona_engine import generate_behavior_config


def test_impatient_persona():
    persona = Persona(
        id="p1",
        name="Impatient User",
        traits=["impatient"]
    )

    config = generate_behavior_config(persona)

    assert config.click_delay < 1.0
    assert config.abandon_threshold < 5


def test_beginner_persona():
    persona = Persona(
        id="p2",
        name="Beginner User",
        traits=["beginner"]
    )

    config = generate_behavior_config(persona)

    assert config.read_probability > 0.5


def test_careful_persona():
    persona = Persona(
        id="p3",
        name="Careful User",
        traits=["careful"]
    )

    config = generate_behavior_config(persona)

    assert config.error_probability < 0.1


def test_multiple_traits():
    persona = Persona(
        id="p4",
        name="Complex Persona",
        traits=["beginner", "analytical"]
    )

    config = generate_behavior_config(persona)

    assert config.read_probability <= 1.0