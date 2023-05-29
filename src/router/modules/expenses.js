/** When your routing table is too long, you can split it into small modules**/

import Layout from '@/layout'

const expensesRouter = {
  path: '/expenses',
  component: Layout,
  name: 'expenses',
  meta: {
    title: '支出',
    icon: 'search'
  },
  children: [
    {
      path: 'searchExpenses',
      component: () => import('@/views/answers/admin/index_search.vue'),
      name: 'searchExpenses',
      meta: { title: '查询支出', noCache: true }
    },
    {
      path: 'addExpenses',
      component: () => import('@/views/answers/admin/index_add.vue'),
      name: 'addExpenses',
      meta: { title: '增加支出', noCache: true }
    },
    {
      path: 'deleteExpenses',
      component: () => import('@/views/answers/admin/index_delete.vue'),
      name: 'deleteExpenses',
      meta: { title: '删除支出', noCache: true }
    },
    {
      path: 'applyExpenses',
      component: () => import('@/views/answers/admin/index_apply.vue'),
      name: 'applyExpenses',
      meta: { title: '送审支出', noCache: true }
    },
    {
      path: 'modifyExpenses',
      component: () => import('@/views/answers/admin/index_modify.vue'),
      name: 'modifyExpenses',
      meta: { title: '修改支出', noCache: true }
    }
  ]
}

export default expensesRouter

