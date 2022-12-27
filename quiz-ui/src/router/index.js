import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import Questions from '../views/Questions.vue'
import QuestionDisplay from '../views/QuestionDisplay.vue'
import Result from '../views/Result.vue'
import Login from '../views/Login.vue'
import Adminparam from '../views/Adminparam.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/NewQuizPage',
      name: 'NewQuizPage',
      component: NewQuizPage
      
    },
    {
      path: '/Questions',
      name: 'Questions',
      component: Questions
      
    },
    {
      path: '/QuestionDisplay',
      name: 'QuestionDisplay',
      component: QuestionDisplay
      
    },
    {
      path: '/Result',
      name: 'Result',
      component: Result
      
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login
      
    },
    {
      path: '/Adminparam',
      name: 'Adminparam',
      component: Adminparam
      
    }
  ]
})

export default router
