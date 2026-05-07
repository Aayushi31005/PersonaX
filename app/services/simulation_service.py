from typing import Dict

from app.models.persona import Persona
from app.models.ui_flow import UINode, Transition

from app.engines.persona_engine import (
    generate_behavior_config,
)

from app.engines.simulation_engine import (
    run_simulation,
)

from app.engines.insights_engine import (
    generate_insights,
)

from app.models.simulation import (
    InsightsReport,
)


def execute_simulation(
    persona: Persona,
    nodes: Dict[str, UINode],
    transitions: Dict[str, Transition],
    start_node_id: str,
):
    """
    Full simulation execution pipeline.
    """

    behavior = generate_behavior_config(persona)

    result = run_simulation(
        persona=persona,
        behavior=behavior,
        nodes=nodes,
        transitions=transitions,
        start_node_id=start_node_id,
    )

    return result


def execute_batch_simulation(
    personas,
    nodes,
    transitions,
    start_node_id,
) -> InsightsReport:
    """
    Executes simulations across multiple personas
    and generates aggregated insights.
    """

    results = []

    for persona in personas:
        behavior = generate_behavior_config(persona)

        result = run_simulation(
            persona=persona,
            behavior=behavior,
            nodes=nodes,
            transitions=transitions,
            start_node_id=start_node_id,
        )

        results.append(result)

    report = generate_insights(results)

    return report