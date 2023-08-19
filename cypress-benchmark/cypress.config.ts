import { defineConfig } from "cypress";

export default defineConfig({
  e2e: {
    experimentalOriginDependencies: true,
    modifyObstructiveCode: false,
    videoCompression: 15,
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
