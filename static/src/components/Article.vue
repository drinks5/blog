<template>
    <div>
        <h1 class="text-center">
            <router-link :to="{ name: 'articleDetail', params: {id: post.id}}">{{ post.title }}</router-link>
        </h1>
        <p>
        <span class="glyphicon glyphicon-user"><router-link :to="{ name: 'articleDetail', params: {id: post.id} }">{{  post.belongto.username }}</router-link>
        </span>
        <span class="glyphicon glyphicon-time">{{ post.update_date }}</span>
        <span class="glyphicon glyphicon-star"></span><router-link :to="{ name: 'articleList', query: {search: post.category.name} }"> {{ post.category.name }}</router-link>
        <span class="tag" v-for="(tag, index) in post.tags" v-bind:class="getTagStyle(index, 'tag-')"><router-link :to="{ name: 'articleList', query: {search: tag.name} }"> {{ tag.name }}</router-link></span>
        </p>
        <hr>
        <img class="img-responsive img-thumbnail" v-bind:src="getUrl(post.background_thumbnail)" alt="">
        <hr>
        <div v-html="post.content | marked"></div>
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
    }
}
</script>
