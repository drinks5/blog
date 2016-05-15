/*
* @Author: drinksober
* @Date:   2016-04-28 16:15:58
* @Last Modified by:   drinksober
* @Last Modified time: 2016-04-28 17:28:29
*/

var archive_url = '/api/article/'
var demo =new Vue({
    el: '#post_list',
    data: {
        post_list: null
    },
    ready: function () {
        this.$http({url: archive_url, method:'GET'}).then(function (response) {
            this.post_list = response.data
        })
    },
})