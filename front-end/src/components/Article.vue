<template>
    <div>
        <h1 class="text-center">
            <router-link :to="{ name: 'articleDetail', params: {id: post.id}}">{{ post.title }}</router-link>
        </h1>
        <p>
        <span class="fa fa-user"><router-link :to="{ name: 'articleDetail', params: {id: post.id} }">{{  post.belongto.username }}</router-link>
        </span>
        <span class="fa fa-clock-o">{{ post.update_date }}</span>
        <span class="fa fa-archive"></span><router-link :to="{ name: 'articleList', query: {search: post.category.name} }"> {{ post.category.name }}</router-link>
        <span class="fa fa-tags" v-for="(tag, index) in post.tags" v-bind:class="getTagStyle(index, 'tag')"><router-link :to="{ name: 'articleList', query: {search: tag.name} }"> {{ tag.name }}</router-link></span>
        </p>
        <div class="img_" v-if="post.background_thumbnail">
            <hr>
            <img class="img-responsive img-thumbnail" v-bind:src="getUrl(post.background_thumbnail)" alt="">
        </div>
        <div v-html="content"></div>
        <router-link class="btn btn-primary" :to="{ name: 'articleDetail', params: {id: post.id} }">Read More <span class="glyphicon glyphicon-chevron-right"></span></router-link>
        <hr>
    </div>
</template>

<script>

import { articleUrl, getUrl  } from '../utils/apiurls'
import { getTagStyle } from '../utils/utils'
import { marked } from '../utils/filters'

export default{
    props: ['post'],
    methods: {
        getTagStyle: getTagStyle,
        getUrl: getUrl,
        marked: marked
    },
    computed: {
        content: function() {
            return marked(this.post.content)
        }
    }
}
</script>
