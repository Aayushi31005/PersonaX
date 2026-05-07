from typing import Dict, List

from app.models.persona import Persona
from app.models.behavior import BehaviorConfig
from app.models.ui_flow import UINode, Transition
from app.models.simulation import (
    InteractionEvent,
    SimulationResult,
)

from app.utils.randomizer import SeededRandom


def run_simulation(
    persona: Persona,
    behavior: BehaviorConfig,
    nodes: Dict[str, UINode],
    transitions: Dict[str, Transition],
    start_node_id: str,
    seed: int = 42,
    max_steps: int = 20,
) -> SimulationResult:
    """
    Simulates user traversal through a UI flow.
    """

    rng = SeededRandom(seed)

    current_node_id = start_node_id

    events: List[InteractionEvent] = []

    current_time = 0.0
    frustration = 0
    steps = 0

    completed = False
    drop_off_node = None

    while steps < max_steps:

        node = nodes[current_node_id]

        # ---------------------------------
        # UX Friction Modeling
        # ---------------------------------

        complexity_penalty = (
            node.complexity * 2
        )

        current_time += (
            behavior.click_delay
            + complexity_penalty
        )

        # ---------------------------------
        # Instruction Dependency
        # ---------------------------------

        reads_content = (
            rng.probability()
            < behavior.read_probability
        )

        if node.instruction_required:
            if reads_content:
                current_time += 2.0
            else:
                frustration += 1

        # ---------------------------------
        # Form Friction
        # ---------------------------------

        dynamic_error_probability = (
            behavior.error_probability
        )

        if node.form_heavy:
            dynamic_error_probability += (
                node.complexity * 0.3
            )

        # ---------------------------------
        # Simulate action success
        # ---------------------------------

        action_success = (
            rng.probability() > dynamic_error_probability
        )

        event = InteractionEvent(
            step=steps,
            node_id=current_node_id,
            action="interact",
            timestamp=round(current_time, 2),
            success=action_success,
            details=(
                "Read content before acting"
                if reads_content
                else "Quick interaction"
            ),
        )

        events.append(event)

        # ---------------------------------
        # Handle failed interaction
        # ---------------------------------

        if not action_success:
            frustration += 1

        if frustration >= behavior.abandon_threshold:
            drop_off_node = current_node_id
            break

        # ---------------------------------
        # End condition
        # ---------------------------------

        if not node.transitions:
            completed = True
            break

        # ---------------------------------
        # Move to next node
        # ---------------------------------

        next_transition_id = node.transitions[0]

        transition = transitions[next_transition_id]

        current_node_id = transition.target

        steps += 1

    return SimulationResult(
        persona_id=persona.id,
        completed=completed,
        total_time=round(current_time, 2),
        steps_taken=steps,
        events=events,
        drop_off_node=drop_off_node,
    )