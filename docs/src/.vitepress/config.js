import { defineConfig } from 'vitepress'
import mathjax3 from 'markdown-it-mathjax3'


const customElements = [
  'math',
  'maction',
  'maligngroup',
  'malignmark',
  'menclose',
  'merror',
  'mfenced',
  'mfrac',
  'mi',
  'mlongdiv',
  'mmultiscripts',
  'mn',
  'mo',
  'mover',
  'mpadded',
  'mphantom',
  'mroot',
  'mrow',
  'ms',
  'mscarries',
  'mscarry',
  'mscarries',
  'msgroup',
  'mstack',
  'mlongdiv',
  'msline',
  'mstack',
  'mspace',
  'msqrt',
  'msrow',
  'mstack',
  'mstack',
  'mstyle',
  'msub',
  'msup',
  'msubsup',
  'mtable',
  'mtd',
  'mtext',
  'mtr',
  'munder',
  'munderover',
  'semantics',
  'math',
  'mi',
  'mn',
  'mo',
  'ms',
  'mspace',
  'mtext',
  'menclose',
  'merror',
  'mfenced',
  'mfrac',
  'mpadded',
  'mphantom',
  'mroot',
  'mrow',
  'msqrt',
  'mstyle',
  'mmultiscripts',
  'mover',
  'mprescripts',
  'msub',
  'msubsup',
  'msup',
  'munder',
  'munderover',
  'none',
  'maligngroup',
  'malignmark',
  'mtable',
  'mtd',
  'mtr',
  'mlongdiv',
  'mscarries',
  'mscarry',
  'msgroup',
  'msline',
  'msrow',
  'mstack',
  'maction',
  'semantics',
  'annotation',
  'annotation-xml'
]

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "War Room",
  description: "Webapp for the War Room India",
  outDir: '../public',
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
          { text: 'App', link: '/warroom/index' },
          { text: 'Demonstration', link: '/warroom/demo.html' },
        ]
      },
      {
        text: 'Intervention models',
        items: [
          { text: 'Treatment outcomes', link: '/tutorial/index.html' }
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
  },
  markdown: {
    config: (md) => {
      md.use(mathjax3);
    }
  },
  vue: {
    template: {
      compilerOptions: {
        isCustomElement: (tag) => customElements.includes(tag),
      }
    }
  }
})
