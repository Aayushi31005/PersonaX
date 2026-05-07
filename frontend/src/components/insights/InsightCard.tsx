import React from "react";

type Props = {
  severity: string;
  message: string;
};

export default function InsightCard({
  severity,
  message,
}: Props) {

  const severityColor = {
    high: "border-red-500",
    medium: "border-yellow-500",
    low: "border-green-500",
  };

  return (
    <div
      className={`
        p-4
        rounded-2xl
        border-l-4
        bg-white/5
        mb-4

        ${
          severityColor[
            severity as keyof typeof severityColor
          ]
        }
      `}
    >

      <p
        className="
          uppercase
          text-xs
          text-white/40
          mb-2
        "
      >
        {severity} Severity
      </p>

      <h3 className="text-sm leading-6">
        {message}
      </h3>

    </div>
  );
}
