/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["home.html"],
  theme: {
    extend: {
      screens:{
        'sm':'360px',
        'md':'740px',
        'lg':'1220px'
      },
      fontFamily:{
        'cstm':['Poppins','sans-serif'],
      }
    },
  },
  plugins: [],
}

