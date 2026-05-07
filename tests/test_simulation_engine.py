from app.models.persona import Persona
from app.models.behavior import BehaviorConfig
from app.models.ui_flow import UINode, Transition

from app.engines.simulation_engine import run_simulation


def test_basic_simulation():

    persona = Persona(
        id="p1",
        name="Test User",
        traits=[]
    )

    behavior = BehaviorConfig(
        click_delay=1.0,
        read_probability=0.5,
        error_probability=0.1,
        abandon_threshold=3,
    )

    nodes = {
        "home": UINode(
            id="home",
            name="Home",
            transitions=["t1"]
        ),

        "login": UINode(
            id="login",
            name="Login",
            transitions=[]
        ),
    }

    transitions = {
        "t1": Transition(
            id="t1",
            source="home",
            target="login",
            trigger="click_login",
        )
    }

    result = run_simulation(
        persona=persona,
        behavior=behavior,
        nodes=nodes,
        transitions=transitions,
        start_node_id="home",
    )

    assert result.steps_taken >= 0
    assert len(result.events) > 0