import { motion } from "framer-motion";

type Props = {
  data: {
    label: string;
    active?: boolean;
  };
};

export default function FlowNode({ data }: Props) {

  return (
    <motion.div

      animate={{
        scale: data.active ? 1.08 : 1,
        boxShadow: data.active
          ? "0px 0px 50px rgba(124,58,237,0.8)"
          : "0px 0px 20px rgba(124,58,237,0.15)",
      }}

      transition={{
        duration: 0.4,
      }}

      className={`
        px-6
        py-4
        rounded-2xl
        border
        min-w-[180px]
        text-center
        backdrop-blur-xl
        transition-all
        duration-300

        ${
          data.active
            ? "bg-[#1E1B4B] border-purple-400"
            : "bg-[#12172A] border-white/10"
        }
      `}
    >
      <p className="text-sm text-white/60 mb-1">
        Screen
      </p>

      <h3 className="text-lg font-semibold text-white">
        {data.label}
      </h3>

    </motion.div>
  );
}