/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from '@/plugins'

// Components
import App from '@/App.vue'

// Composables
import { createApp, h } from 'vue'

const app = createApp({
    render: () => h(App),
})
app.config.compilerOptions.delimiters = ['[[',']]'];
registerPlugins(app)

app.mount('#app')
