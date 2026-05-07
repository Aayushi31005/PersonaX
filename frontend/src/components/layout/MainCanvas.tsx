import FlowGraph from "../graph/FlowGraph";

type Props = {
  simulation: any;
};

export default function MainCanvas({
  simulation,
}: Props) {

  return (
    <div className="flex-1 p-4">

      <div
        className="
          h-full
          rounded-2xl
          bg-panel
          border
          border-white/10
          overflow-hidden
        "
      >

        <FlowGraph
          simulation={simulation}
        />

      </div>

    </div>
  );
}