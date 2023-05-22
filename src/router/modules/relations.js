/** When your routing table is too long, you can split it into small modules**/

import Layout from '@/layout'

const relationRouter = {
  path: '/relations',
  component: Layout,
  name: 'Relations',
  meta: {
    title: 'Relations',
    icon: 'star'
  },
  children: [
    {
      path: 'ReputationAcceptedRelation',
      component: () => import('@/views/relations/ReputationAcceptedRelation'),
      name: 'ReputationAcceptedRelation',
      meta: { title: 'Reputation Accepted Relation', noCache: true }
    },
    {
      path: 'ReputationScoreRelation',
      component: () => import('@/views/relations/ReputationScoreRelation.vue'),
      name: 'ReputationScoreRelation',
      meta: { title: 'Reputation Score Relation', noCache: true }
    }
  ]
}

export default relationRouter
