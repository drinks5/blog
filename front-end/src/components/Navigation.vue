<template>
    <div>
    <nav class="navbar navbar-dark bg-inverse">
    <ul class="nav navbar-nav">
        <li class="nav-item active">
            <router-link :to="{ name: 'articleList' }" class="nav-link">{{ username }}<span class="sr-only">(current)</span></router-link>
        </li>
        <li class="nav-item">
            <router-link :to="{ name: 'about' }" class="nav-link">About</router-link>
        </li>
        <li class="nav-item">
            <router-link :to="{ name: 'contact' }" class="nav-link">Contact</router-link>
        </li>
    </ul>
    </nav>
    </div>
</template>

<script>
export default {
  data () {
    return {
      username: 'Lin Lin',
    }
  }
}
</script>

<style>
footer {
    margin: 50px 0;
}
</style>
