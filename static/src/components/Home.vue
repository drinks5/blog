<template>
    <div>
    <div class="row">
        <div class="col-sm-9">
            <router-view></router-view>
        </div>

        <div class="col-sm-3">
            <side-bar></side-bar>
        </div>
    </div>
    <hr>
    </div>
</template>


<script>
import SideBar from './SideBar'

export default {
    components: {
        SideBar
    }
}
</script>
