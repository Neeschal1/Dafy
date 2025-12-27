/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./App.{js,jsx,ts,tsx}",
    "./src/screens/**/*.{js,ts,jsx,tsx}",
    "./src/components/**/*.{js,ts,jsx,tsx}",
  ],
  presets: [require("nativewind/preset")],
  theme: {
    extend: {
      colors: {
        background: "#F2F1FF",
        primary: "#FA5A2A",
        secondary: "#030721",
        tertiary: "#A4A8B5",
      },
      fontSize: {
        headingtext: "24px",
        
      },
    },
  },
  plugins: [],
};
