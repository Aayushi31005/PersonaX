from pydantic import BaseModel, Field
from typing import List


class Persona(BaseModel):
    """
    Represents a user persona with behavioral traits.
    """

    id: str = Field(
        ...,
        description="Unique identifier for the persona"
    )

    name: str = Field(
        ...,
        min_length=1,
        description="Human-readable persona name"
    )

    traits: List[str] = Field(
        default_factory=list,
        description="Behavioral traits associated with the persona"
    )