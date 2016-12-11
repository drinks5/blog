<template>
    <div>
        <post-com v-for="post in postList" :post="post"></post-com>
    <!-- Pager -->
        <nav class="blog-pagination">
            <router-link class="btn btn-outline-primary" :to="{ name: 'articleList', query:{ page: previous} }" v-bind:class="{ 'disabled': !previous}">Older</router-link>
            <router-link class="btn btn-outline-primary" :to="{ name: 'articleList', query: {page: next} }" v-bind:class="{ 'disabled': !next }">Newer</router-link>
        </nav>
    </div>
</template>

<script>
import { articleUrl } from '../utils/apiurls'
import  PostCom from './Article.vue'

export default{
    data: function() {
        return {
            postList: [],
            page: 1,
            count: 0,
            next: null,
            previous: null,
        }
    },
    components: {
        PostCom
    },
    created: function() {
        return this.getPostList()
    },
    watch: function() {
        return {
            '$route': 'getPostList'
        }
    },
    methods: {
        getPostList: function() {
            return this.$http.get(articleUrl, {'params': this.$route.params, 'query': this.$route.query}).then((response) => {
                this.postList = response.data.results;
                this.count = response.data.count;
                this.next = response.data.next;
                this.previous = response.data.previous
            })
        },
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
