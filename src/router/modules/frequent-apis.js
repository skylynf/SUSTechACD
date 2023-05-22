/** When your routing table is too long, you can split it into small modules**/

import Layout from '@/layout'

const frequentRouter = {
  path: '/frequentApis',
  component: Layout,
  name: 'FrequentApis',
  meta: {
    title: 'Frequent Apis',
    icon: 'search'
  },
  children: [
    {
      path: 'frequentlyDiscussedClasses',
      component: () => import('@/views/frequent-apis/FrequentlyDiscussedClasses.vue'),
      name: 'FrequentlyDiscussedClasses',
      meta: { title: 'Frequent Classes', noCache: true }
    },
    {
      path: 'frequentlyDiscussedMethods',
      component: () => import('@/views/frequent-apis/FrequentlyDiscussedMethods.vue'),
      name: 'FrequentlyDiscussedMethods',
      meta: { title: 'Frequent Methods', noCache: true }
    }
  ]
}

export default frequentRouter

