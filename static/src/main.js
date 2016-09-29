import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'


import filters from './utils/filters';
import App from './App'

Vue.use(VueResource)
Vue.use(VueRouter)
Vue.http.headers.common['Authorization'] = 'Token da5306b3507304e95d6098204da1aa4549072dcc';
const router = new VueRouter()


//实例化Vue的filter
Object.keys(filters).forEach(k => Vue.filter(k, filters[k]));

router.map({
    '/': {
        name: 'home',
        component: function(resolve){
            require(['./components/Home.vue'],resolve);
        }
    },
    '/article': {
        name: 'article',
        component: function(resolve){
            require(['./components/Home.vue'],resolve);
        },
        subRoutes: {
            '/list': {
                name: 'articleList',
                component: function(resolve){
                    require(['./components/ArticleList.vue'],resolve);
                }
            },
            '/detail/:id': {
                name: 'articleDetail',
                component: function(resolve){
                    require(['./components/ArticleDetail.vue'],resolve);
                }
            },
            '/edit': {
                name: 'articleEdit',
                component: function(resolve){
                    require(['./components/ArticleEdit.vue'], resolve);
                }
            },
            '/edit/:id': {
                name: 'articleEdit',
                component: function(resolve){
                    require(['./components/ArticleEdit.vue'], resolve);
                }
            },
        }
    },
    '/about': {
		name: 'about',
        component: function(resolve){
            require(['./components/About.vue'],resolve);
        }
    },
    '/contact': {
		name: 'contact',
        component: function(resolve){
            require(['./components/Contact.vue'],resolve);
        }
    },
    '/': {
		name: 'contact',
        component: function(resolve){
            require(['./components/Contact.vue'],resolve);
        }
    },
})
router.redirect({
    '/': '/article/list'
})

router.start(App, '#app')
