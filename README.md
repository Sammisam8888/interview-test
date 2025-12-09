# interview-test (Next.js conversion)

This folder contains a minimal Next.js conversion of the original React utilities found in this workspace. The original logic has been preserved and exported as ES modules.

Quick start

1. Open a terminal and change into this folder:

```cmd
cd "f:\\OPM Corporation\\interview-test"
```

2. Install dependencies and run the dev server:

```cmd
npm install
npm run dev
```

3. Visit http://localhost:3000 to view the page. The API endpoint is at http://localhost:3000/api/profile

Files added/changed
- `package.json` — scripts and Next.js dependencies
- `pages/index.js` — Next.js page rendering the profile
- `pages/api/profile.js` — API route exposing profile data
- `profile.js` — converted to ES module exports
- `lib/analysis.js` — JS port of the `analysis.py` utilities
