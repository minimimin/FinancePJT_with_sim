import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    proxy: {
      '/exchange-api': {
        target: 'https://www.koreaexim.go.kr',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/exchange-api/, '/site/program/financial/exchangeJSON'),
      },
    },
  },
})
