<template>
    <template v-for="post in postList">
        <!-- First Blog Post -->
        <h1 class="text-center">
            <a v-link="{ name: 'articleDetail', params: {id: post.id}}">{{ post.title }}</a>
        </h1>
        <p>
        <span class="glyphicon glyphicon-user"><a v-link="{ name: 'articleDetail', params: {id: post.id} }">{{  post.belongto.username }}</a>
        </span>
        <span class="glyphicon glyphicon-time"></span>  Posted on {{ post.update_date }}&nbsp
        <span class="glyphicon glyphicon-star"></span>{{  post.category.name  }}&nbsp
        <span class="label" v-for="(index, tag) in post.tags" v-bind:class="getTagStyle(index)">{{ tag.name }}</span>
        </p>
        <hr>
        <img class="img-responsive img-thumbnail" src="http://127.0.0.1:8000{{ post.backgroupnd_thumbnail }}" alt="">
        <hr>
        {{{ post.content | marked }}}
        <a class="btn btn-primary" v-link="{ name: 'articleDetail', params: {id: post.id} }">Read More <span class="glyphicon glyphicon-chevron-right"></span></a>
        <hr>
    </template>

    <!-- Pager -->
    <ul class="pager">
        <li class="previous">
            <a v-link="{ name: 'articleList', params:{ page: page - 1} }">&larr; Older</a>
        </li>
        <li class="next">
            <a v-link="{ name: 'articleList', params: {page: page + 1} }">Newer &rarr;</a>
        </li>
    </ul>
</template>

<script>
export default{
    data: function() {
        return {
            postList: [],
            apiUrl: 'http://127.0.0.1:8000/api/article/?search=',
            page: 0,
            tagStyles: {0: 'default', 1: 'primary', 2: 'success', 3: 'info', 4: 'warning', 5: 'danger'}
        }
    },
    props: ['search'],
    route: {
        data: function (transition) {
            var search = transition.to.params.search;
            var page = transition.to.params.page
            search = search === ':search' ? '': search;
            page= page === ':page' ? '': page;
            return { postList: this.getPostList(this.apiUrl + search + '&page=' + page)}
        }
    },
    methods: {
        getPostList: function(apiUrl) {
            return this.$http.get(apiUrl).then((response) => {
                return response.data
            })
        },

        getTagStyle: function(index) {
            index = index % 6;
            var style = this.tagStyles[index];
            style = 'label-' + style;
            return style
        },
    },
}
</script>
