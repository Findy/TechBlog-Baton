module.exports = {
  content: [
    "./_drafts/**/*.html",
    "./_includes/**/*.html",
    "./_layouts/**/*.html",
    "./_posts/*.md",
    "./*.md",
    "./*.html",
  ],
  theme: {
    theme: {
      extend: {},
    },
  },
  plugins: [
    require("tailwindcss"),
    require("autoprefixer"),
    ...(process.env.JEKYLL_ENV == "production"
      ? [require("cssnano")({ preset: "default" })]
      : []),
  ],
}
