<template>
    <div class="container">
        <div class="row">
            <div class="col-lg-12 text-center">
                <div class="intro-text">
                    <span class="skills">Web Developer - Machine Learning</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default{
    data: function() {
        return {username: 'Lin Lin'}
    }
}
</script>

<style>

hr.star-light,
hr.star-primary {
  padding: 0;
  border: none;
  border-top: solid 5px;
  text-align: center;
  max-width: 250px;
  margin: 25px auto 30px;
}
hr.star-light:after,
hr.star-primary:after {
  content: "\f005";
  font-family: FontAwesome;
  display: inline-block;
  position: relative;
  top: -0.8em;
  font-size: 2em;
  padding: 0 0.25em;
}
hr.star-light {
  border-color: white;
}
hr.star-light:after {
  background-color: #18BC9C;
  color: white;
}
</style>
