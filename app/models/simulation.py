from pydantic import BaseModel, Field
from typing import List, Optional


class InteractionEvent(BaseModel):
    """
    Represents a single user interaction during simulation.
    """

    step: int = Field(
        ...,
        description="Sequential step number"
    )

    node_id: str = Field(
        ...,
        description="Current UI node"
    )

    action: str = Field(
        ...,
        description="Action performed by user"
    )

    timestamp: float = Field(
        ...,
        description="Simulated timestamp in seconds"
    )

    success: bool = Field(
        ...,
        description="Whether action succeeded"
    )

    details: Optional[str] = Field(
        default=None,
        description="Additional event details"
    )


class SimulationResult(BaseModel):
    """
    Final output of a simulation run.
    """

    persona_id: str = Field(
        ...,
        description="Persona identifier"
    )

    completed: bool = Field(
        ...,
        description="Whether user completed the flow"
    )

    total_time: float = Field(
        ...,
        ge=0,
        description="Total simulated interaction time"
    )

    steps_taken: int = Field(
        ...,
        ge=0,
        description="Total interaction steps"
    )

    events: List[InteractionEvent] = Field(
        default_factory=list,
        description="Interaction event log"
    )

    drop_off_node: Optional[str] = Field(
        default=None,
        description="Node where user abandoned flow"
    )


class Insight(BaseModel):
    """
    Human-readable UX insight.
    """

    severity: str = Field(
        ...,
        description="Insight severity level"
    )

    message: str = Field(
        ...,
        description="Human-readable insight description"
    )

    node_id: Optional[str] = Field(
        default=None,
        description="Related UI node"
    )


class SimulationMetrics(BaseModel):
    """
    Aggregated simulation metrics.
    """

    completion_rate: float = Field(
        ...,
        ge=0,
        le=1,
    )

    average_time: float = Field(
        ...,
        ge=0,
    )

    average_steps: float = Field(
        ...,
        ge=0,
    )

    drop_off_rate: float = Field(
        ...,
        ge=0,
        le=1,
    )


class InsightsReport(BaseModel):
    """
    Final analytics output.
    """

    metrics: SimulationMetrics

    insights: List[Insight] = Field(
        default_factory=list
    )