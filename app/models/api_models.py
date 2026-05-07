from pydantic import BaseModel, Field
from typing import List

from app.models.persona import Persona
from app.models.ui_flow import (
    UINode,
    Transition,
)


class SimulationRequest(BaseModel):
    """
    Request payload for a single simulation.
    """

    persona: Persona

    nodes: List[UINode]

    transitions: List[Transition]

    start_node_id: str = Field(
        ...,
        description="Starting node ID"
    )


class BatchSimulationRequest(BaseModel):
    """
    Request payload for batch simulations.
    """

    personas: List[Persona]

    nodes: List[UINode]

    transitions: List[Transition]

    start_node_id: str