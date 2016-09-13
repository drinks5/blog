<template>
    <div class="row">
        <div class="col-md-9">
            <router-view></router-view>
        </div>

        <div class="col-md-3">
            <side-bar></side-bar>
        </div>
    </div>
    <hr>
</template>


<script>
import SideBar from './SideBar'

export default {
    components: {
        SideBar
    }
}
</script>
