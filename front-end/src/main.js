/* @flow */

import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'

import filters from './utils/filters'
import App from './App'

Vue.use(VueResource)
Vue.use(VueRouter)

const Home = resolve => require(['./components/Home.vue'], resolve)
const ArticleList = resolve => require(['./components/ArticleList.vue'], resolve)
const ArticleDetail = resolve => require(['./components/ArticleDetail.vue'], resolve)
const ArticleEdit = resolve => require(['./components/ArticleEdit.vue'], resolve)
const About = resolve => require(['./components/About.vue'], resolve)
const Contact = resolve => require(['./components/Contact.vue'], resolve)
const routes = [
    { 
        path: '/',
        name: 'home',
        component: Home,
        redirect: { name: 'articleList' }
    },
    {
        path: '/article',
        name: 'article',
        component: Home,
        children: [
            {
                path: '/article/list',
                name: 'articleList',
                component: ArticleList
            },
            {
                path: 'detail/:id(\\d+)',
                name: 'articleDetail',
                component: ArticleDetail
            },
        ]
    },
    {
        path: '/article/edit/:id(\\d+)?',
        name: 'articleEdit',
        component: ArticleEdit
    },
    {
        path: '/about',
		name: 'about',
        component: About
    },
    {
        path: '/contact',
		name: 'contact',
        component: Contact
    }
]

const router = new VueRouter({ mode: 'history', routes: routes })

const app = new Vue({
    router,
    render: h => h(App)
}).$mount('#app')
