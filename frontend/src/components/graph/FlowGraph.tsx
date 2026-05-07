import ReactFlow, {
  Background,
  Controls,
  MiniMap,
} from "reactflow";

import "reactflow/dist/style.css";

import FlowNode from "./FlowNode";

import {
  createNodes,
  edges,
} from "../../mock/sampleData";

const nodeTypes = {
  custom: FlowNode,
};

type Props = {
  simulation: any;
};

export default function FlowGraph({
  simulation,
}: Props) {

  const nodes =
    createNodes(simulation.activeNode);

  return (
    <div className="w-full h-full relative">

      <button
        onClick={simulation.startSimulation}

        disabled={simulation.isPlaying}

        className="
          absolute
          top-4
          right-4
          z-50
          px-5
          py-2
          rounded-xl
          bg-purple-600
          hover:bg-purple-500
          transition-all
          text-sm
          font-medium
        "
      >
        {simulation.isPlaying
          ? "Simulating..."
          : "Run Simulation"}
      </button>

      <ReactFlow
        nodes={nodes}
        edges={edges}
        nodeTypes={nodeTypes}
        fitView
      >
        <Background />

        <MiniMap />

        <Controls />

      </ReactFlow>

    </div>
  );
}