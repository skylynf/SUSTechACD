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
      component: () => import('@/views/expenses/editor/index_search.vue'),
      name: 'searchExpenses',
      meta: { title: '查询支出', noCache: true , roles: ['admin','editor']}
    },
    {
      path: 'addExpenses',
      component: () => import('@/views/expenses/editor/index_add.vue'),
      name: 'addExpenses',
      meta: { title: '增加支出', noCache: true ,  roles: ['editor']}
    },
    {
      path: 'deleteExpenses',
      component: () => import('@/views/expenses/editor/index_delete.vue'),
      name: 'deleteExpenses',
      meta: { title: '删除支出', noCache: true , roles: ['admin','editor']}
    },
    {
      path: 'applyExpenses',
      component: () => import('@/views/expenses/editor/index_apply.vue'),
      name: 'applyExpenses',
      meta: { title: '送审支出', noCache: true , roles:  ['editor']}

    },
    {
      path: 'modifyExpenses',
      component: () => import('@/views/expenses/editor/index_modify.vue'),
      name: 'modifyExpenses',
      meta: { title: '修改支出', noCache: true , roles: ['editor']}
    },
{
  path: 'searchExpensesAdmin',
    component: () => import('@/views/expenses/admin/index_search_admin.vue'),
  name: 'searchExpensesAdmin',
  meta: { title: '查询待审批支出', noCache: true , roles: ['admin']}
},
  ]
}

export default expensesRouter

