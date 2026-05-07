from typing import Dict, Tuple

from fastapi import APIRouter

from app.models.api_models import (
    SimulationRequest,
    BatchSimulationRequest,
)
from app.models.ui_flow import (
    UINode,
    Transition,
)

from app.services.simulation_service import (
    execute_batch_simulation,
    execute_simulation,
)

router = APIRouter()


def _build_flow_maps(
    nodes: list[UINode],
    transitions: list[Transition],
) -> Tuple[Dict[str, UINode], Dict[str, Transition]]:
    return (
        {node.id: node for node in nodes},
        {transition.id: transition for transition in transitions},
    )


@router.post("/run")
def run_simulation_api(request: SimulationRequest):
    nodes, transitions = _build_flow_maps(request.nodes, request.transitions)

    result = execute_simulation(
        persona=request.persona,
        nodes=nodes,
        transitions=transitions,
        start_node_id=request.start_node_id,
    )

    return result.model_dump()


@router.post("/batch")
def run_batch_simulation_api(request: BatchSimulationRequest):
    nodes, transitions = _build_flow_maps(request.nodes, request.transitions)

    report = execute_batch_simulation(
        personas=request.personas,
        nodes=nodes,
        transitions=transitions,
        start_node_id=request.start_node_id,
    )

    return report.model_dump()