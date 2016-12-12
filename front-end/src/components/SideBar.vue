<template>
    <div>
    <!-- Blog Sidebar Widgets Column -->
        <!-- Blog Search Well -->
        <div class="alert alert-info" role="alert">
            <div class="input-group">
                <input type="text" class="form-control" v-model="search">
                <span class="input-group-btn">
                    <router-link class="btn btn-primary btn-lg" :to="{ name: 'articleList', query: {search: search}}">
                        <span class="fa fa-search-minus"></span>
                    </router-link>
                </span>
            </div>

            <!-- /.input-group -->
        </div>

        <!-- Blog Categories Well -->
                <h4 class="text-center">Blog Categories</h4>
                <ul class="list-group">
                    <li class="list-group-item" v-for="category in categoryList">
                        <span class="tag tag-default tag-pill float-xs-right"><router-link :to="{ name: 'articleList', query: {search: category.name} }">1</router-link></span>{{category.name}}
                    </li>
                </ul>

        <!-- Blog Tag Well -->
                <h4 class="text-center">Blog Tag</h4>
                <ul class="list-group">
                    <li class="list-group-item" v-for="tag in tagList">
                        <span class="tag tag-default tag-pill float-xs-right"><router-link :to="{ name: 'articleList', query: {search: tag.name} }">1</router-link></span>{{tag.name}}
                    </li>
                </ul>
            <!-- /.row -->
        <!-- Side Widget Well -->
        <div class="alert alert-info" role="alert">
            <h4 class="text-center">Side Widget Well</h4>
            <p>个人博客</p>
        </div>
    </div>
</template>


<script>

import { getTagStyle, getData, getHalf } from '../utils/utils'
import { categoryUrl, tagsUrl } from '../utils/apiurls'

export default{
    data: function() {
        return {
            categoryList: [],
            tagList: [],
            search: '',
            username: 'Lin Lin'
        }
    },
    mounted: function() {
        getData(this, tagsUrl, 'tagList'),
        getData(this, categoryUrl, 'categoryList')
    },
    computed: {
        halfCategory: function() {
            return getHalf(this.categoryList)
        },
        halfTag: function(){
            return getHalf(this.tagList)
        }
    },
    methods: {
        getTagStyle: getTagStyle
    }
}
</script>
