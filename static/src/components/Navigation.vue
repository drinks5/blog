<template>
    <nav class="navbar navbar-dark bg-inverse">
    <ul class="nav navbar-nav">
        <li class="nav-item active">
            <a class="nav-link" v-link="{ name: 'articleList' }">{{ username }}<span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
        <a class="nav-link" v-link="{ name: 'about' }">About</a>
        </li>
        <li class="nav-item">
        <a class="nav-link" v-link="{ name: 'contact' }">Contact</a>
        </li>
    </ul>
    </nav>
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
