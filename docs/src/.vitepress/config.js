import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "War Room",
  description: "Webapp for the War Room India",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Interventions', link: '/tutorial/index.html' },
      { text: 'Documents', link: '/docs/index.html' }
    ],
    sidebar: [
      {
        text: 'War Room',
        items: [
          { text: 'App', link: '/warroom/index.html' },
        ]
      },
      {
        text: 'Intervention models',
        items: [
          { text: 'Competing rates', link: '/tutorial/index.html' }
        ]
      },
      {
        text: 'TB dynamics',
        items: [
          { text: 'Overview', link: '/docs/index.html' },
          { text: 'Active TB', link: '/docs/activeTB.html' },
          { text: 'Transmission', link: '/docs/transmission.html' },
          { text: 'Latent TB', link: '/docs/ltbi.html' },
          { text: 'Diagnosis and treatments', link: '/docs/dx.html' }
        ]
      },
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})
