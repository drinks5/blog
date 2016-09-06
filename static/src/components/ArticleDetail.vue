<template>

    <h2>
        <a v-link="{ name: 'articleDetail', params: {id: post.id}}">{{ post.title }}</a>
    </h2>
    <p class="lead">
    by <a v-link="{ name: 'articleDetail', params: {id: post.id} }">{{ post.belongto.username }}</a>
    </p>
    <p><span class="glyphicon glyphicon-time"></span>  Posted on {{ post.update_date }}</p>
    <p><span class="glyphicon glyphicon-certificate"></span><template v-for="tag in post.tags">  {{ tag.name }}</template></p>
    <p>{{  post.category.name  }}</p>
    <hr>
    <img class="img-responsive" src="http://127.0.0.1:8000{{ post.backgroupnd_thumbnail }}" alt="">
    <hr>
    {{ post.content }}
    <hr>

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
export default{
    data: function() {
        return {
            post: {'title': '', 'id': '1', 'belongto': {'username': ''}, 'tags': [], 'category': '', 'content': ''},
            detailUrl: 'http://127.0.0.1:8000/api/article/' + this.$route.params.id + '/'
        }
    },
    ready: function() {
        this.getPostList(this.detailUrl)
    },
    methods: {
        getPostList: function(apiUrl) {
            this.$http.get(apiUrl).then((response) => {
                this.$set('post', response.data)
            })
        }
    }
}
</script>
