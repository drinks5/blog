exports.getTagStyle = function(index, preStr){
    var tagStyles = {0: 'default', 1: 'primary', 2: 'success', 3: 'info', 4: 'warning', 5: 'danger'}
    index = index % 6;
    var style = tagStyles[index];
    style = preStr + style;
    return style
}
