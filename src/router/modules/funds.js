/** When your routing table is too long, you can split it into small modules**/

import Layout from '@/layout'

const fundsRouter = {
  path: '/funds',
  component: Layout,
  name: 'funds',
  meta: {
    title: '经费',
    icon: 'education'
  },
  children: [
    {
      path: 'addFunds',
      component: () => import('@/views/accepted-answers/index'),
      name: 'addFunds',
      meta: { title: '新增经费', noCache: true }
    },
    {
      path: 'queryFunds',
      component: () => import('@/views/answers/admin/queryfund.vue'),
      name: 'queryFunds',
      meta: { title: '查询经费', noCache: true }
    },
    // {
    //   path: 'deleteExpenses',
    //   component: () => import('@/views/answers/admin/index_delete.vue'),
    //   name: 'deleteExpenses',
    //   meta: { title: '删除支出', noCache: true }
    // },
    // {
    //   path: 'applyExpenses',
    //   component: () => import('@/views/answers/admin/index_apply.vue'),
    //   name: 'applyExpenses',
    //   meta: { title: '送审支出', noCache: true }
    // },
    // {
    //   path: 'modifyExpenses',
    //   component: () => import('@/views/answers/admin/index_modify.vue'),
    //   name: 'modifyExpenses',
    //   meta: { title: '修改支出', noCache: true }
    // }
  ]
}

export default fundsRouter
