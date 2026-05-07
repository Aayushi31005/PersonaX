from app.models.persona import Persona
from app.models.behavior import BehaviorConfig
from app.models.ui_flow import UINode, Transition


def test_persona_creation():
    persona = Persona(
        id="p1",
        name="Beginner User",
        traits=["beginner", "careful"]
    )

    assert persona.name == "Beginner User"


def test_behavior_config():
    behavior = BehaviorConfig(
        click_delay=1.5,
        read_probability=0.8,
        error_probability=0.2,
        abandon_threshold=5
    )

    assert behavior.error_probability == 0.2


def test_ui_node():
    node = UINode(
        id="home",
        name="Home Screen",
        elements=["login_button"],
        transitions=["t1"]
    )

    assert node.id == "home"


def test_transition():
    transition = Transition(
        id="t1",
        source="home",
        target="login",
        trigger="click_login"
    )

    assert transition.target == "login"