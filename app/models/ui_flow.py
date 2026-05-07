from pydantic import BaseModel, Field
from typing import List, Optional


class Transition(BaseModel):
    """
    Represents movement between two UI nodes.
    """

    id: str = Field(
        ...,
        description="Unique transition identifier"
    )

    source: str = Field(
        ...,
        description="Source node ID"
    )

    target: str = Field(
        ...,
        description="Target node ID"
    )

    trigger: str = Field(
        ...,
        description="Action triggering the transition"
    )

    condition: Optional[str] = Field(
        default=None,
        description="Optional condition required for transition"
    )


class UINode(BaseModel):
    """
    Represents a UI screen/state in the flow.
    """

    id: str = Field(
        ...,
        description="Unique node identifier"
    )

    name: str = Field(
        ...,
        description="Human-readable screen name"
    )

    elements: List[str] = Field(
        default_factory=list,
        description="Interactive UI elements"
    )

    transitions: List[str] = Field(
        default_factory=list,
        description="Outgoing transition IDs"
    )

    # ---------------------------------
    # UX Complexity Parameters
    # ---------------------------------

    complexity: float = Field(
        0.5,
        ge=0,
        le=1,
        description="Cognitive complexity of screen"
    )

    instruction_required: bool = Field(
        False,
        description="Whether instructions are important"
    )

    form_heavy: bool = Field(
        False,
        description="Whether screen contains difficult forms"
    )