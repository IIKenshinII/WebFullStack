import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'
import Questions from '../views/Questions.vue'
import QuestionDisplay from '../views/QuestionDisplay.vue'

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
      
    }
  ]
})

export default router
