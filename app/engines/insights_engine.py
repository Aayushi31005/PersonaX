from collections import Counter
from typing import List

from app.models.simulation import (
    SimulationResult,
    SimulationMetrics,
    Insight,
    InsightsReport,
)


def generate_insights(
    results: List[SimulationResult],
) -> InsightsReport:
    """
    Aggregates simulation results into metrics and UX insights.
    """

    if not results:
        return InsightsReport(
            metrics=SimulationMetrics(
                completion_rate=0,
                average_time=0,
                average_steps=0,
                drop_off_rate=0,
            ),
            insights=[],
        )

    total_runs = len(results)

    completed_runs = sum(
        1 for r in results if r.completed
    )

    completion_rate = completed_runs / total_runs

    average_time = (
        sum(r.total_time for r in results) / total_runs
    )

    average_steps = (
        sum(r.steps_taken for r in results) / total_runs
    )

    drop_off_rate = (
        sum(1 for r in results if r.drop_off_node)
        / total_runs
    )

    # ---------------------------------
    # Detect common drop-off points
    # ---------------------------------

    drop_off_counter = Counter(
        r.drop_off_node
        for r in results
        if r.drop_off_node
    )

    insights = []

    for node_id, count in drop_off_counter.items():

        if count / total_runs >= 0.3:

            insights.append(
                Insight(
                    severity="high",
                    message=(
                        f"Users frequently abandon the flow at '{node_id}'."
                    ),
                    node_id=node_id,
                )
            )

    # ---------------------------------
    # Detect slow flows
    # ---------------------------------

    if average_time > 10:

        insights.append(
            Insight(
                severity="medium",
                message=(
                    "Users spend significant time completing the flow."
                ),
            )
        )

    # ---------------------------------
    # Detect low completion rate
    # ---------------------------------

    if completion_rate < 0.5:

        insights.append(
            Insight(
                severity="high",
                message=(
                    "Flow completion rate is critically low."
                ),
            )
        )

    metrics = SimulationMetrics(
        completion_rate=round(completion_rate, 2),
        average_time=round(average_time, 2),
        average_steps=round(average_steps, 2),
        drop_off_rate=round(drop_off_rate, 2),
    )

    return InsightsReport(
        metrics=metrics,
        insights=insights,
    )