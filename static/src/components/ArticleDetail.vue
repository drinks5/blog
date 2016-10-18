<template>
    <div>
        <post-com :post="post"></post-com>
    <!-- Pager -->
    <ul class="pager">
        <li class="previous">
            <router-link :to="{ name: 'articleDetail', params: {id: post.id - 1} }">&larr; Older</router-link>
        </li>
        <li class="next">
            <router-link :to="{ name: 'articleDetail', params: {id: post.id + 1} }">Newer &rarr;</router-link>
        </li>
    </ul>
    </div>
</template>


<script>
import { articleUrl } from '../utils/apiurls'
import PostCom from './Article.vue'

export default{
    data: function() {
        return {
            post: {'title': '', 'id': '1', 'belongto': {'username': ''}, 'tags': [], 'category': '', 'content': ''},
            apiUrl: articleUrl
        }
    },
    components: {
        PostCom
    },
    created: function() {
        this.getPost()
    },
    watch: function() {
        return {
            '$route': 'getPostList'
        }
    },
    methods: {
        getPost: function() {
            let url = articleUrl + (this.$route.params.id || 0) + '/';
            return this.$http.get(url).then((response) => {
                this.post = response.data
            })
        },
    }
}
</script>
