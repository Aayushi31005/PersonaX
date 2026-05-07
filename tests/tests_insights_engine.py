from app.models.simulation import (
    SimulationResult,
    InteractionEvent,
)

from app.engines.insights_engine import (
    generate_insights,
)


def test_generate_insights():

    results = [
        SimulationResult(
            persona_id="p1",
            completed=False,
            total_time=12,
            steps_taken=4,
            drop_off_node="login",
            events=[],
        ),

        SimulationResult(
            persona_id="p2",
            completed=False,
            total_time=11,
            steps_taken=5,
            drop_off_node="login",
            events=[],
        ),

        SimulationResult(
            persona_id="p3",
            completed=True,
            total_time=8,
            steps_taken=3,
            events=[],
        ),
    ]

    report = generate_insights(results)

    assert report.metrics.completion_rate >= 0
    assert len(report.insights) > 0