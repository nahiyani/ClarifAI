<template>
  <div>
    <Header />
    <Banner pageTitle="Transcribe"/>
    <YoutubeSearchBar @transcribe="handleTranscribe" ref="searchBar" />
    <Footer />
  </div>
</template>

<script>
import Header from '../components/Header.vue'
import Banner from '../components/Banner.vue'
import Footer from '../components/Footer.vue'
import YoutubeSearchBar from '../components/YoutubeSearchBar.vue'

export default {
  name: 'TranscribePage',
  components: {
    Header,
    Banner,
    YoutubeSearchBar,
    Footer
  },
  methods: {
    handleTranscribe(youtubeUrl) {
      // Handle the transcription process here
      console.log('Starting transcription for:', youtubeUrl);
      
      // You could also call an API or perform other actions here
      // For now, we're just keeping the URL in the search bar
    }
  }
}
</script>