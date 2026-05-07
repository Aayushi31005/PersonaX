export type InteractionEvent = {
  step: number;
  node_id: string;
  action: string;
  timestamp: number;
  success: boolean;
  details?: string;
};

export type SimulationResult = {
  persona_id: string;
  completed: boolean;
  total_time: number;
  steps_taken: number;
  drop_off_node?: string | null;
  events: InteractionEvent[];
};

export type Persona = {
  id: string;
  name: string;
  traits: string[];
};

export type UXInsight = {
  severity: string;
  message: string;
  node_id?: string | null;
};

export type SimulationMetrics = {
  completion_rate: number;
  average_time: number;
  average_steps: number;
  drop_off_rate: number;
};

export type InsightsReport = {
  metrics: SimulationMetrics;
  insights: UXInsight[];
};
