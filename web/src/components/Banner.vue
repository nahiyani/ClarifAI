<template>
    <h1 class="page-title">{{ pageTitle }}</h1>
</template>

<script>
export default {
  name: 'Banner',
  props: {
    pageTitle: {
      type: String,
      required: true
    }
  },
  computed: {
    displayWord() {
      return this.pageTitle;
    }
  }
}
</script>

<style>

.page-title{
  font-size: 2.5rem;
  font-weight: bold;
  background: linear-gradient(90deg, hsla(197, 100%, 63%, 1) 0%, hsla(294, 100%, 55%, 1) 100%);
  color: white;
  width: 100%;
  text-align: center;
}


</style>