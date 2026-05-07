import InsightCard from
  "../insights/InsightCard";

type Props = {
  simulation: any;
};

export default function InsightsPanel({
  simulation,
}: Props) {

  return (
    <div
      className="
        w-[380px]
        bg-panel
        border-l
        border-white/10
        p-5
        overflow-y-auto
      "
    >

      <div className="mb-6">

        <h2 className="text-2xl font-bold">
          UX Findings
        </h2>

        <p className="text-sm text-white/50 mt-2">
          Persona-driven usability insights
        </p>

      </div>

      {/* RUN ALL BUTTON */}

      <button
        onClick={
          simulation.runAllPersonas
        }

        className="
          w-full
          mb-6
          py-3
          rounded-xl
          bg-purple-600
          hover:bg-purple-500
          transition-all
          font-medium
        "
      >
        Run All Personas
      </button>

      {/* INSIGHTS */}

      {!simulation.report && (
        <div className="text-white/40">
          Run comparative analysis to
          identify UX friction.
        </div>
      )}

      {simulation.report && (
        <div>

          {/* METRICS */}

          <div
            className="
              grid
              grid-cols-2
              gap-3
              mb-6
            "
          >

            <div className="bg-white/5 rounded-xl p-4">
              <p className="text-xs text-white/40">
                Completion
              </p>

              <h3 className="text-xl font-bold mt-1">
                {
                  simulation.report.metrics
                    .completion_rate
                }
              </h3>
            </div>

            <div className="bg-white/5 rounded-xl p-4">
              <p className="text-xs text-white/40">
                Drop-off
              </p>

              <h3 className="text-xl font-bold mt-1">
                {
                  simulation.report.metrics
                    .drop_off_rate
                }
              </h3>
            </div>

          </div>

          {/* INSIGHT CARDS */}

          {simulation.report.insights.map(
            (
              insight: any,
              index: number
            ) => (

              <InsightCard
                key={index}
                severity={
                  insight.severity
                }

                message={
                  insight.message
                }
              />

            )
          )}

        </div>
      )}

    </div>
  );
}