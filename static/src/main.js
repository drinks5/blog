import Vue from 'vue'

import App from './App'
import Navigation from './components/Navigation'
import Home from './components/Home'
import About from './components/About'
import Contact from './components/Contact'

import Articles from './components/Articles'
import ArticleDetail from './components/ArticleDetail'

import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

Vue.use(VueResource)
Vue.use(VueRouter)

const router = new VueRouter()

router.map({
    '/home': {
		name: 'home',
        component: Home,
        subRoutes: {
            '/list': {
				name: 'articleList',
                component: Articles
                },
            '/detail/:id': {
				name: 'articleDetail',
                component: ArticleDetail
                }
            }
    },
    '/about': {
		name: 'about',
        component: About
    },
    '/contact': {
		name: 'contact',
        component: Contact
    }
})
router.redirect({
    '/home': '/home/list',
    '*': '/home/list'
})

router.start(App, '#app')
