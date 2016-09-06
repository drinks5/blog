<template>
    <div class="row">
        <div class="col-md-9">
            <router-view :search.sync=search></router-view>
        </div>

        <div class="col-md-3">
            <side-bar :search.sync=search></side-bar>
        </div>
    </div>
    <hr>
</template>


<script>
import SideBar from './SideBar'

export default {
    data: function() {
        return {
            search: ''
        }
    },
    components: {
        SideBar
    }
}
</script>
