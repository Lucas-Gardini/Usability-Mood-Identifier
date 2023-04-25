import { createApp } from "vue";
import App from "./App.vue";
import PrimeVue from "primevue/config";

//theme
import "primevue/resources/themes/lara-light-indigo/theme.css";

//core
import "primevue/resources/primevue.min.css";

import "./style.css";

createApp(App).use(PrimeVue).mount("#app");
