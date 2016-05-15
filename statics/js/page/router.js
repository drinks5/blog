/*
* @Author: drinksober
* @Date:   2016-04-28 16:18:06
* @Last Modified by:   drinksober
* @Last Modified time: 2016-04-28 17:20:54
*/

var Foo = Vue.extend({
    template: '<p>This is foo!</p>'
})
var Bar = Vue.extend({
    template: '<p>This is bar!</p>'
})
var App = Vue.extend({})
var router = new VueRouter()
router.map({
    '/': {
        component: Foo
    },
})
router.start(App, '#home')
