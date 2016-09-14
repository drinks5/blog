<template>
    <!-- Blog Sidebar Widgets Column -->
        <!-- Blog Search Well -->
        <div class="well">
            <h4 class="text-center">Blog Search</h4>
            <div class="input-group">
                <input type="text" class="form-control" v-model="search">
                <span class="input-group-btn">
                    <a class="btn btn-primary btn-lg" v-link="{ name: 'articleList', query: {search: search}}">
                        <span class="glyphicon glyphicon-search"></span>
                    </a>
                </span>
            </div>
            <!-- /.input-group -->
        </div>

        <!-- Blog Categories Well -->
        <div class="well">
            <h4 class="text-center">Blog Categories</h4>
            <div class="row">
                <div class="col-lg-6">
                    <ul class="list-unstyled" v-for="category in categoryList | limitBy halfCategory">
                        <li><a v-link="{name: 'articleList', query: { search: category.name} }">{{ category.name }}</a>
                        </li>
                    </ul>
                </div>
                <!-- /.col-lg-6 -->
                <div class="col-lg-6">
                    <ul class="list-unstyled" v-for="category in categoryList | limitBy halfCategory halfCategory">
                        <li><a v-link="{ name: 'articleList', query: {search: category.name} }">{{ category.name }}</a></li>
                    </ul>
                </div>
                <!-- /.col-lg-6 -->
            </div>
            <!-- /.row -->
        </div>


        <!-- Blog Tag Well -->
        <div class="well">
            <h4 class="text-center">Blog Tag</h4>
                    <li class="list-unstyled tag-cloud" v-bind:class="getTagStyle(index, 'tag-cloud-')" v-for="(index, tag) in tagList">
                        <a v-link="{ name: 'articleList', query: {search: tag.name} }">{{ tag.name }}</a>
                    </li>
            </div>
            <!-- /.row -->
        </div>
        <!-- Side Widget Well -->
        <div class="well">
            <h4 class="text-center">Side Widget Well</h4>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore, perspiciatis adipisci accusamus laudantium odit aliquam repellat tempore quos aspernatur vero.</p>
        </div>
</template>


<script>

import { getTagStyle } from '../utils/utils'
import { categoryUrl, tagsUrl } from '../utils/apiurls'

export default{
    data: function() {
        return {
            categoryList: [],
            tagList: [],
            categoryUrl: categoryUrl,
            tagsUrl: tagsUrl,
            search: '',
            username: 'Lin Lin'
        }
    },
    ready: function() {
        this.getCategoryList(this.categoryUrl),
        this.getTagList(this.tagUrl)
    },
    computed: {
        halfCategory: function() {
            return Math.round(this.categoryList.length/2)
        },
        halfTag: function() {
            return Math.round(this.tagList.length/2)
        }
    },
    methods: {
        getCategoryList: function(categoryUrl) {
            this.$http.get(categoryUrl).then((response) => {
                this.$set('categoryList', response.data)
            })
        },
        getTagList: function(tagUrl) {
            this.$http.get(tagsUrl).then((response) => {
                this.$set('tagList', response.data)
            })
        },
        getTagStyle: getTagStyle
    }
}
</script>

<style>
#tag-cloud {
	width: 200px;
	margin-left: 0;
}
.tag-cloud {
    background-color: #999999;
    -webkit-border-radius: 3px;
	   -moz-border-radius: 3px;
	        border-radius: 3px;
    color: #FFFFFF;
    cursor: pointer;
    display: inline-block;
    font-size: 11.844px;
    font-weight: bold;
    line-height: 21px;
    margin: 2px 3px 2px 2px;
    padding: 1px 4px 2px;
    text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
    vertical-align: baseline;
}
.tag-cloud:after {
    color: #000000;
    content: " ×";
    font-size: 20px;
    font-weight: bold;
    line-height: 16px;
    opacity: 0.2;
	position: relative;
    text-shadow: 0 1px 0 #FFFFFF;
	top: 1px;
}

	/* Colors */

.tag-cloud.tag-cloud-default {
    background-color: #3A87AD;
}
.tag-cloud.tag-cloud-primary {
    background-color: #56789D;
}
.tag-cloud.tag-cloud-success {
    background-color: #468847;
}
.tag-cloud.tag-cloud-info {
    background-color: #333333;
}
.tag-cloud.tag-cloud-warning {
    background-color: #F89406;
}
.tag-cloud.tag-cloud-danger {
    background-color: #B94A48;
}
</style>
