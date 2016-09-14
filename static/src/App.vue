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
</style>
