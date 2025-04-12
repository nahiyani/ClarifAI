<template>
  <div>
    <Header />
    <Banner pageTitle="Contact" description="Whether you have a question, need support, or have feedback to improve the 
    site — we’re here for you. Fill out the form below and a member of our team will get back to you shortly!"/>
    <ContactForm />
    <Footer />
  </div>
</template>

<script>
import Header from '../components/Header.vue'
import Banner from '../components/Banner.vue'
import Footer from '../components/Footer.vue'
import ContactForm from '../components/ContactForm.vue';

export default {
  components: {
    Header,
    Banner,
    ContactForm,
    Footer
  }
}
</script>  