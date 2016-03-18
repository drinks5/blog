/*
* @Author: drinks
* @Date:   2016-03-16 22:48:35
* @Last Modified by:   drinks
* @Last Modified time: 2016-03-17 10:10:27
*/

  // import Vue from 'vue';
  // import VueRouter from 'vue-router';
  // Vue.use(VueRouter);

// var archive_url = '/article/archive/'
// var demo = new Vue({
//     el: '#post_list',
//     data: {
//         post_list: null
//     },
//     created: function() {
//         this.fetchData()
//     },
//     methods: {
//         fetchData: function() {
//             var self = this
//             var res = $.get(archive_url, function() {
//                 self.post_list = res.responseJSON
//             })
//         }
//     }
// })
// 定义组件

var Foo = Vue.extend({
    template: '<p>This is foo!</p>'
})

var Bar = Vue.extend({
    template: '<p>This is bar!</p>'
})

var App = Vue.extend({})

var router = new VueRouter()

router.map({
    '/article/1/': {
        component: Foo
    },
})

router.start(App, '#home')
