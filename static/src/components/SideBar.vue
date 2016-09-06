<template>
    <!-- Blog Sidebar Widgets Column -->
        <!-- Blog Search Well -->
        <div class="well">
            <h4>Blog Search</h4>
            <div class="input-group">
                <input type="text" class="form-control" v-model="search">
                <span class="input-group-btn">
                    <a class="btn btn-default" v-link="{ name: 'articleList', exact:true, params: {search: search}}">
                        <span class="glyphicon glyphicon-search"></span>
                    </a>
                </span>
            </div>
            <!-- /.input-group -->
        </div>

        <!-- Blog Categories Well -->
        <div class="well">
            <h4>Blog Categories</h4>
            <div class="row">
                <div class="col-lg-6">
                    <ul class="list-unstyled" v-for="category in categoryList | limitBy halfCategory">
                        <li><a v-link="{name: 'articleList', params: { categoryId: category.id} }">{{ category.name }}</a>
                        </li>
                    </ul>
                </div>
                <!-- /.col-lg-6 -->
                <div class="col-lg-6">
                    <ul class="list-unstyled" v-for="category in categoryList | limitBy halfCategory halfCategory">
                        <li><a href="#">{{ category.name }}</a></li>
                    </ul>
                </div>
                <!-- /.col-lg-6 -->
            </div>
            <!-- /.row -->
        </div>


        <!-- Blog Tag Well -->
        <div class="well">
            <h4>Blog Tag</h4>
                    <ul class="list-unstyled" v-for="tag in tagList">
                        <li><a href="#">{{ tag.name }}</a>
                        </li>
                    </ul>
            </div>
            <!-- /.row -->
        </div>
        <!-- Side Widget Well -->
        <div class="well">
            <h4>Side Widget Well</h4>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore, perspiciatis adipisci accusamus laudantium odit aliquam repellat tempore quos aspernatur vero.</p>
        </div>
</template>


<script>
export default{
    data: function() {
        return {
            categoryList: [],
            categoryUrl: 'http://127.0.0.1:8000/api/category/',

            tagUrl: 'http://127.0.0.1:8000/api/tags/',
            tagList: [],
            username: 'Lin Lin'
        }
    },
    props: {
        search: String
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
            this.$http.get(tagUrl).then((response) => {
                this.$set('tagList', response.data)
            })
        }
    }
}
</script>
