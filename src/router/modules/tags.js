/** When your routing table is too long, you can split it into small modules**/

import Layout from '@/layout'

const chartsRouter = {
  path: '/tags',
  component: Layout,
  name: 'Tags',
  meta: {
    title: 'Tags',
    icon: 'star'
  },
  children: [
    {
      path: 'TagsMostUpvotes',
      component: () => import('@/views/tags/TagsMostUpvotes'),
      name: 'TagsMostUpvotes',
      meta: { title: 'Most Upvotes Tags', noCache: true }
    },
    {
      path: 'TagsMostViews',
      component: () => import('@/views/tags/TagsMostViews'),
      name: 'TagsMostViews',
      meta: { title: 'Most Views Tags', noCache: true }
    },
    {
      path: 'TagsWithJava',
      component: () => import('@/views/tags/TagsWithJava'),
      name: 'TagsWithJava',
      meta: { title: 'Tags with Java', noCache: true }
    }
  ]
}

export default chartsRouter
