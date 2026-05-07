import { useEffect, useState } from "react";

import {
  runSimulation,
} from "../services/api";

import {
  Persona,
  SimulationResult,
} from "../types/simulation";

import {
  InsightsReport,
} from "../types/simulation";

import {
  runBatchSimulation,
} from "../services/api";

const personaBatch: Persona[] = [
  {
    id: "p1",
    name: "Impatient User",
    traits: ["impatient"],
  },
  {
    id: "p2",
    name: "Analytical Researcher",
    traits: ["analytical"],
  },
  {
    id: "p3",
    name: "Casual Browser",
    traits: ["casual"],
  },
];

export function useSimulation() {

  const [activeNode, setActiveNode] =
    useState<string | null>(null);

  const [isPlaying, setIsPlaying] =
    useState(false);

  const [result, setResult] =
    useState<SimulationResult | null>(null);

  const [report, setReport] =
    useState<InsightsReport | null>(
      null
    );

  async function startSimulation() {

    setIsPlaying(true);

    const simulationResult =
      await runSimulation();

    setResult(simulationResult);
  }

  async function runAllPersonas() {

    const batchReport =
      await runBatchSimulation(
        personaBatch
      );

    setReport(batchReport);
  }

  useEffect(() => {

    if (!result) return;

    let currentStep = 0;

    const interval = setInterval(() => {

      if (
        currentStep >= result.events.length
      ) {

        clearInterval(interval);

        setIsPlaying(false);

        return;
      }

      const event =
        result.events[currentStep];

      setActiveNode(event.node_id);

      currentStep++;

    }, 1200);

    return () => clearInterval(interval);

  }, [result]);

  return {
    activeNode,
    isPlaying,
    startSimulation,
    result,
    report,
    runAllPersonas,
  };
}