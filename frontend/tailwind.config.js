/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "#0B1020",
        panel: "#12172A",
        accent: "#7C3AED",
        success: "#22C55E",
        danger: "#EF4444",
      },
    },
  },
  plugins: [],
};
