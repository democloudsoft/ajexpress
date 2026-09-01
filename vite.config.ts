import path from 'path';
import {defineConfig} from 'vite';

export default defineConfig(() => {
  return {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, '.'),
      },
    },
    build: {
      rollupOptions: {
        input: {
          main: path.resolve(__dirname, 'index.html'),
          about: path.resolve(__dirname, 'about.html'),
          services: path.resolve(__dirname, 'services.html'),
          flights: path.resolve(__dirname, 'flights.html'),
          hotels: path.resolve(__dirname, 'hotels.html'),
          tours: path.resolve(__dirname, 'tours.html'),
          visa: path.resolve(__dirname, 'visa.html'),
          umrah: path.resolve(__dirname, 'umrah.html'),
          booking: path.resolve(__dirname, 'booking.html'),
          blog: path.resolve(__dirname, 'blog.html'),
          contact: path.resolve(__dirname, 'contact.html'),
          faq: path.resolve(__dirname, 'faq.html'),
          privacy: path.resolve(__dirname, 'privacy-policy.html'),
          terms: path.resolve(__dirname, 'terms-and-conditions.html'),
        }
      }
    },
    server: {
      hmr: process.env.DISABLE_HMR !== 'true',
      watch: process.env.DISABLE_HMR === 'true' ? null : {},
    },
  };
});
