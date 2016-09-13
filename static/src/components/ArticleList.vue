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
        <span class="glyphicon glyphicon-star"></span><a v-link="{ name: 'articleList', query: {search: post.category.name} }"> {{ post.category.name }}</a>
        <span class="label" v-for="(index, tag) in post.tags" v-bind:class="getTagStyle(index)"><a v-link="{ name: 'articleList', query: {search: tag.name} }"> {{ tag.name }}</a></span>
        </p>
        <hr>
        <img class="img-responsive img-thumbnail" v-bind:src="getUrl(post.backgroupnd_thumbnail)" alt="">
        <hr>
        {{{ post.content | marked }}}
        <a class="btn btn-primary" v-link="{ name: 'articleDetail', params: {id: post.id} }">Read More <span class="glyphicon glyphicon-chevron-right"></span></a>
        <hr>
    </template>

    <!-- Pager -->
    <ul class="pager">
        <li class="previous">
            <a v-link="{ name: 'articleList', query:{ page: page - 1} }">&larr; Older</a>
        </li>
        <li class="next">
            <a v-link="{ name: 'articleList', query: {page: page + 1} }">Newer &rarr;</a>
        </li>
    </ul>
</template>

<script>
import { articleUrl, getUrl  } from '../utils/apiurls'
import { getTagStyle} from '../utils/utils'
export default{
    data: function() {
        return {
            postList: [],
            apiUrl: articleUrl,
            page: 0,
        }
    },
    route: {
        data: function (transition) {
            var search = this.$route.query.search || '';
            console.log(this.$route.query)
            var url = this.apiUrl + '?search=' + search
            return { postList: this.getPostList(url)}
        }
    },
    methods: {
        getPostList: function(apiUrl) {
            return this.$http.get(apiUrl).then((response) => {
                return response.data
            })
        },
        getTagStyle: getTagStyle,
        getUrl: getUrl
    }
}
</script>
