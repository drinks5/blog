import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'


import filters from './utils/filters';
import App from './App'
import Navigation from './components/Navigation'
import Home from './components/Home'
import About from './components/About'
import Contact from './components/Contact'

import ArticleList from './components/ArticleList'
import ArticleDetail from './components/ArticleDetail'

Vue.use(VueResource)
Vue.use(VueRouter)

const router = new VueRouter()


//实例化Vue的filter
Object.keys(filters).forEach(k => Vue.filter(k, filters[k]));

router.map({
    '/home': {
		name: 'home',
        component: Home,
        subRoutes: {
            '/list/:search': {
				name: 'articleList',
                component: ArticleList
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
    },
})
router.redirect({
    '/': '/home/list'
})

router.start(App, '#app')
