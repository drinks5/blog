<template>
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" v-link="{ name: 'articleList' }">{{ username }}</a>
            </div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li class="currentPath == '/about' ? 'active': ''">
                        <a v-link="{ name: 'about' }">About</a>
                    </li>
                    <li class="currentPath == '/contact' ? 'active': ''">
                        <a v-link="{ name: 'contact' }">Contact</a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>
</template>

<script>
export default {
  data () {
    return {
      username: 'Lin Lin',
	  currentPath: '',
    }
  }
}
</script>
