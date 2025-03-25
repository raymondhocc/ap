import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3002,
    host: true,
    strictPort: true,
    watch: {
      usePolling: true
    },
    proxy: {
      '/api': {
        target: 'http://api:3003',
        changeOrigin: true,
        secure: false
      }
    }
  }
})
