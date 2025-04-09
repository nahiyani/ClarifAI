<template>
  <div class="banner">
    <Header />
    <AutoTyper />
    <CardSection />
    <YoutubeEmbed />
  </div>
</template>

<script>
import Header from '../components/Header.vue'
import AutoTyper from '../components/AutoTyper.vue'
import CardSection from '../components/CardSection.vue';
import YoutubeEmbed from '../components/YoutubeEmbed.vue';

export default {
  components: {
    Header,
    AutoTyper,
    CardSection,
    YoutubeEmbed
  },
}
</script>

  