<template>
  <div class="banner">
    <Header />
    <AutoTyper />
    <CardSection />
  </div>
</template>

<script>
import Header from '../components/Header.vue'
import AutoTyper from '../components/AutoTyper.vue'
import CardSection from '../components/CardSection.vue';

export default {
  components: {
    Header,
    AutoTyper,
    CardSection
  },
}
</script>

  