<template>
    <navigation></navigation>
    <div class="container">
        <router-view></router-view>
        <footer-com></footer-com>
    </div>
</template>

<script>
import Navigation from './components/Navigation'
import FooterCom from './components/FooterCom'
import Home from './components/Home'

export default {
    components: {
        FooterCom, Navigation, Home
  }
}
</script>


<style>

.logo {
  width: 100px;
  height: 100px
}

body {
    padding-top: 70px; /* Required padding for .navbar-fixed-top. Remove if using .navbar-static-top. Change if height of navigation changes. */
}

footer {
    margin: 50px 0;
}
</style>
