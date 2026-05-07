import Sidebar from "../components/layout/Sidebar";
import Topbar from "../components/layout/Topbar";
import MainCanvas from "../components/layout/MainCanvas";
import InsightsPanel from "../components/layout/InsightsPanel";

import {
  useSimulation,
} from "../hooks/useSimulation";

export default function Dashboard() {

  const simulation =
    useSimulation();

  return (
    <div className="h-screen flex bg-background text-white">

      <Sidebar />

      <div className="flex-1 flex flex-col">

        <Topbar />

        <MainCanvas
          simulation={simulation}
        />

      </div>

      <InsightsPanel
        simulation={simulation}
      />

    </div>
  );
}