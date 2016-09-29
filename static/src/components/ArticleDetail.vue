<template>

        <h1 class="text-center">
            <a v-link="{ name: 'articleDetail', params: {id: post.id}}">{{ post.title }}</a>
        </h1>
        <p>
        <span class="glyphicon glyphicon-user"><a v-link="{ name: 'articleDetail', params: {id: post.id} }">{{  post.belongto.username }}</a>
        </span>
        <span class="glyphicon glyphicon-time">{{ post.update_date }}</span>
        <span class="glyphicon glyphicon-star"></span><a v-link="{ name: 'articleList', query: {search: post.category.name} }"> {{ post.category.name }}</a>
        <span class="label" v-for="(index, tag) in post.tags" v-bind:class="getTagStyle(index, 'tag-')"><a v-link="{ name: 'articleList', query: {search: tag.name} }"> {{ tag.name }}</a></span>
        </p>
        <hr>
        <img class="img-responsive img-thumbnail" v-bind:src="getStaticUrl(post.background_thumbnail)" alt="">
        <hr>
        {{{ post.content | marked }}}

    <!-- Pager -->
    <ul class="pager">
        <li class="previous">
            <a v-link="{ name: 'articleDetail', params: {id: post.id - 1} }">&larr; Older</a>
        </li>
        <li class="next">
            <a v-link="{ name: 'articleDetail', params: {id: post.id + 1} }">Newer &rarr;</a>
        </li>
    </ul>
</template>


<script>
import { articleUrl, getUrl  } from '../utils/apiurls'
import { getTagStyle} from '../utils/utils'
export default{
    data: function() {
        return {
            post: {'title': '', 'id': '1', 'belongto': {'username': ''}, 'tags': [], 'category': '', 'content': ''},
            apiUrl: articleUrl
        }
    },
    route: {
        data: function (transition) {
            var apiUrl =  this.apiUrl + this.$route.params.id + '/'
            return { post: this.getPost(apiUrl)}
        }
    },
    methods: {
        getPost: function(apiUrl) {
            return this.$http.get(apiUrl).then((response) => {
                return response.data
            })
        },
        getTagStyle: getTagStyle,
        getStaticUrl: getUrl
    }
}
</script>
