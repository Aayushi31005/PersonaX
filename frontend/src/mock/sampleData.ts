export const createNodes = (
  activeNode?: string | null
) => [
  {
    id: "landing",
    position: { x: 100, y: 250 },
    data: {
      label: "Landing",
      active: activeNode === "landing",
    },
    type: "custom",
  },

  {
    id: "onboarding",
    position: { x: 450, y: 150 },
    data: {
      label: "Onboarding",
      active: activeNode === "onboarding",
    },
    type: "custom",
  },

  {
    id: "verification",
    position: { x: 850, y: 250 },
    data: {
      label: "Verification",
      active: activeNode === "verification",
    },
    type: "custom",
  },

  {
    id: "dashboard",
    position: { x: 1200, y: 150 },
    data: {
      label: "Dashboard",
      active: activeNode === "dashboard",
    },
    type: "custom",
  },
];

export const edges = [
  {
    id: "e1",
    source: "home",
    target: "login",
    animated: true,
  },

  {
    id: "e2",
    source: "login",
    target: "dashboard",
    animated: true,
  },
];
