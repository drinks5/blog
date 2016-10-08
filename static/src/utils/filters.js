import Markdown from 'marked'
Markdown.setOptions({
  highlight: function (code) {
    return require('highlight.js').highlightAuto(code).value;
  }
});
exports.marked = (text) => {
    return Markdown(text)

}

exports.equal = (left, right) => {
    return left === right
}
