import { Persona, SimulationResult, InsightsReport } from "../types/simulation";

const API_BASE =
  "http://127.0.0.1:8000";

export async function runSimulation() {
  const response = await fetch(
    `${API_BASE}/simulations/run`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        persona: {
          id: "p1",
          name: "Impatient User",
          traits: ["impatient"],
        },
        nodes: [
          {
            id: "landing",
            name: "Landing",
            elements: [],
            transitions: ["t1"],
            complexity: 0.2,
            instruction_required: false,
            form_heavy: false,
          },
          {
            id: "onboarding",
            name: "Complex Onboarding",
            elements: [],
            transitions: ["t2"],
            complexity: 0.9,
            instruction_required: true,
            form_heavy: false,
          },
          {
            id: "verification",
            name: "Identity Verification",
            elements: [],
            transitions: ["t3"],
            complexity: 0.8,
            instruction_required: true,
            form_heavy: true,
          },
          {
            id: "dashboard",
            name: "Dashboard",
            elements: [],
            transitions: [],
            complexity: 0.2,
            instruction_required: false,
            form_heavy: false,
          },
        ],
        transitions: [
          {
            id: "t1",
            source: "landing",
            target: "onboarding",
            trigger: "start",
          },
          {
            id: "t2",
            source: "onboarding",
            target: "verification",
            trigger: "continue",
          },
          {
            id: "t3",
            source: "verification",
            target: "dashboard",
            trigger: "complete",
          },
        ],
        start_node_id: "landing",
      }),
    }
  );

  const data: SimulationResult =
    await response.json();

  return data;
}

export async function runBatchSimulation(personas: Persona[]) {
  const response = await fetch(
    `${API_BASE}/simulations/batch`,
    {
      method: "POST",
      headers: {
        "Content-Type":
          "application/json",
      },
      body: JSON.stringify({
        personas: personas,
        nodes: [
          {
            id: "landing",
            name: "Landing",
            elements: [],
            transitions: ["t1"],
            complexity: 0.2,
            instruction_required: false,
            form_heavy: false,
          },
          {
            id: "onboarding",
            name: "Complex Onboarding",
            elements: [],
            transitions: ["t2"],
            complexity: 0.9,
            instruction_required: true,
            form_heavy: false,
          },
          {
            id: "verification",
            name: "Identity Verification",
            elements: [],
            transitions: ["t3"],
            complexity: 0.8,
            instruction_required: true,
            form_heavy: true,
          },
          {
            id: "dashboard",
            name: "Dashboard",
            elements: [],
            transitions: [],
            complexity: 0.2,
            instruction_required: false,
            form_heavy: false,
          },
        ],
        transitions: [
          {
            id: "t1",
            source: "landing",
            target: "onboarding",
            trigger: "start",
          },
          {
            id: "t2",
            source: "onboarding",
            target: "verification",
            trigger: "continue",
          },
          {
            id: "t3",
            source: "verification",
            target: "dashboard",
            trigger: "complete",
          },
        ],
        start_node_id: "landing",
      }),
    }
  );

  const data: InsightsReport =
    await response.json();

  return data;
}
