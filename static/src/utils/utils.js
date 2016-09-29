exports.getTagStyle = function(index, preStr){
    var tagStyles = {0: 'default', 1: 'primary', 2: 'success', 3: 'info', 4: 'warning', 5: 'danger'}
    index = index % 6;
    var style = tagStyles[index];
    style = preStr + style;
    return style
}

exports.getData = function(vm, url, data=null) {
    vm.$http.get(url).then((response) => {
        data ? vm.$set(data, response.data) : response.data
    })
}

exports.postData = function(vm, url, data) {
    let method = vm.$route.params.id  ? 'put' : 'post'
    return vm.$http[method](url, data).then((response) => {
        response.data
    })
}

exports.getHalf = function(list) {
    return Math.round(list.length / 2)
}
