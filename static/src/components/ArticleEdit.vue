<template>
<form enctype="multipart/form-data">
  <fieldset class="form-group">
    <label for="title">Title</label>
    <input type="title" class="form-control" placeholder="Title" v-model="title">
  </fieldset>
  <fieldset class="form-group">
    <label for="category">Category select</label>
    <select class="form-control" v-model="selectedCategory">
        <template v-for="category in categoryList">
        <option :value="category.id" selected=equal(category.name, selectedCategory)>{{ category.name }}</option>
        </template>
    </select>
  </fieldset>
  <fieldset class="form-group">
    <label for="tags">Tags select</label>
    <multiselect :selected="selectedTagList" :options="tagList" 
        :multiple="true" :searchable="searchable" :taggable="true" 
        @tag="addTag" @update="updateSelectedTagging" 
        tag-placeholder="Add this as new tag" 
        placeholder="Type to search or add tag" label="name" key="id">
    </multiselect>
  </fieldset>

  <fieldset class="form-group">
    <label for="content">Content</label>
    <textarea class="form-control" v-model="content" rows="20"></textarea>
<div id="editor">function foo(items) {
    var x = "All this is syntax highlighted";
    return x;
}</div>
    
  </fieldset>
  <fieldset class="form-group">
    <label for="background">Background</label>
    <input type="file" class="form-control-file" v-el:background>
    <small class="text-muted" v-if="!background"></small>
  </fieldset>
  <button type="submit" class="btn btn-primary" @click="editArticle">Submit</button>
</form>

</template>

<script>
import Multiselect from 'vue-multiselect'
import { getData, postData } from '../utils/utils'
import { categoryUrl, tagsUrl, articleUrl } from '../utils/apiurls'

export default {
    components: { Multiselect },
    data () {
        return {
        formData: new FormData(),
        title: '',
        content: '',
        tagList: [],
        categoryList: [],
        selectedTagList: [],
        selectedCategory: '',
        }
    },

    ready: function() {
        if(this.$route.params.id){
            const url = articleUrl + this.$route.params.id + '/'
            this.$http.get(url).then(function(response){
                this.$set('title', response.data.title);
                this.$set('content', response.data.content)
                this.$set('selectedTagList', response.data.tags.map(tag => tag.name))
                this.$set('selectedCategory', response.data.category.name)
            }
            )
        }
        getData(this, tagsUrl, 'tagList'),
        getData(this, categoryUrl, 'categoryList')
    },
    methods: {
        addTag (newTag) {
            var para = {'name': newTag}
            tag = postData(this, tagsUrl, para)
            this.selectedTagList.push(tag)
            this.tagList.push(tag)
        },
        updateSelectedTagging (value) {
        this.selectedTagList = value
        },

        editArticle () {
            var tagIdList = this.selectedTagList.map(x => x.id)
            var url = articleUrl
            if(this.$route.params.id) {
                url = url + this.$route.params.id + '/'
            }
            this.formData.append('background', this.$els.background.files[0])
            this.formData.append('title', this.title)
            this.formData.append('content', this.content)
            postData(this, url, this.formData).then((response) => (this.$router.go('/article/detail/' + this.$route.params.id)))
        },
        equal (left, right) {
            return left === right
        }
    }
}
</script>

