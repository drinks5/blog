function getUrl(path) {
    var hostname = 'http://127.0.0.1:8000';
    return hostname + path
}
exports.articleUrl = getUrl('/api/article/' )
exports.categoryUrl = getUrl('/api/category/')
exports.tagsUrl = getUrl('/api/tags/')
exports.getUrl = getUrl
