<template>
    <template v-for="post in postList">
        <!-- First Blog Post -->
        <h1 class="text-center">
            <a v-link="{ name: 'articleDetail', params: {id: post.id}}">{{ post.title }}</a>
        </h1>
        <p>
        <span class="glyphicon glyphicon-user"><a v-link="{ name: 'articleDetail', params: {id: post.id} }">{{  post.belongto.username }}</a>
        </span>
        <span class="glyphicon glyphicon-time">{{ post.update_date }}</span>
        <span class="glyphicon glyphicon-star"></span><a v-link="{ name: 'articleList', query: {search: post.category.name} }"> {{ post.category.name }}</a>
        <span class="tag" v-for="(index, tag) in post.tags" v-bind:class="getTagStyle(index, 'tag-')"><a v-link="{ name: 'articleList', query: {search: tag.name} }"> {{ tag.name }}</a></span>
        </p>
        <hr>
        <img class="img-responsive img-thumbnail" v-bind:src="getUrl(post.background_thumbnail)" alt="">
        <hr>
        {{{ post.content | marked }}}
        <a class="btn btn-primary" v-link="{ name: 'articleDetail', params: {id: post.id} }">Read More <span class="glyphicon glyphicon-chevron-right"></span></a>
        <hr>
    </template>

    <!-- Pager -->
    <nav class="blog-pagination">
        <a class="btn btn-outline-primary" v-link="{ name: 'articleList', query:{ page: previous} }" v-bind:class="{ 'disabled': !previous}">Older</a>
        <a class="btn btn-outline-primary" v-link="{ name: 'articleList', query: {page: next} }" v-bind:class="{ 'disabled': !next }">Newer</a>
    </nav>
</template>

<script>
import { articleUrl, getUrl  } from '../utils/apiurls'
import { getTagStyle } from '../utils/utils'
export default{
    data: function() {
        return {
            postList: [],
            apiUrl: articleUrl,
            page: 1,
            count: 0,
            next: null,
            previous: null,
        }
    },
    route: {
        data: function (transition) {
            const search = this.$route.query.search || '';
            const page = transition.to.query.page || this.page;
            const params = {'search': search, 'page': page}
            return this.getPostList(articleUrl, params).then(function(response) {
            return {'postList': response.results, 'count': response.count, 'next': response.next, 'previous': response.previous}})
        }
    },
    methods: {
        getPostList: function(url, params) {
            return this.$http.get(url, {'params':params}).then((response) => {
                return response.data
            })
        },
        getTagStyle: getTagStyle,
        getUrl: getUrl
    }
}
</script>

<style>
a.disabled {
    pointer-events: none;
    color: inherit;
}

/* Pagination */
.blog-pagination {
  margin-bottom: 4rem;
}
.blog-pagination > .btn {
  border-radius: 2rem;
}

</style>
