<template>
    <div>
      <Header />
      <Banner pageTitle="Summarize"/>
      <Footer />
    </div>
  </template>
  
  <script>
  import Header from '../components/Header.vue'
  import Banner from '../components/Banner.vue'
  import Footer from '../components/Footer.vue'
  
  export default {
    components: {
      Header,
      Banner,
      Footer
    }
  }
  </script> 