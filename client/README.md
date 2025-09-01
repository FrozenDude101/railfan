# Client

The frontend.

# Requirements

* npm

# Running

With the API project running on `localhost:8000`.
```bash
npm install;
npx openapi-typescript http://localhost:8000/openapi.json -o ./src/lib/api.d.ts;
npm run start;
```
