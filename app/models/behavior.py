from pydantic import BaseModel, Field


class BehaviorConfig(BaseModel):
    """
    Simulation-ready behavioral parameters.
    """

    click_delay: float = Field(
        ...,
        ge=0,
        description="Delay between actions in seconds"
    )

    read_probability: float = Field(
        ...,
        ge=0,
        le=1,
        description="Probability of reading content before acting"
    )

    error_probability: float = Field(
        ...,
        ge=0,
        le=1,
        description="Probability of making an incorrect action"
    )

    abandon_threshold: int = Field(
        ...,
        ge=0,
        description="Maximum frustration threshold before abandoning flow"
    )