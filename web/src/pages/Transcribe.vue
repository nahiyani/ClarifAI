<template>
  <div>
    <Header />
    <Banner pageTitle="Transcribe" />
    <YoutubeSearchBar @transcribe="handleTranscribe" ref="searchBar" />
    <TranscribeResults v-if="transcription" :text="transcription" />
    <Footer />
  </div>
</template>

<script>
import Header from '../components/Header.vue'
import Banner from '../components/Banner.vue'
import Footer from '../components/Footer.vue'
import YoutubeSearchBar from '../components/YoutubeSearchBar.vue'
import TranscribeResults from '../components/TranscribeResults.vue'

export default {
  name: 'TranscribePage',
  components: {
    Header,
    Banner,
    YoutubeSearchBar,
    TranscribeResults,
    Footer
  },
  data() {
    return {
      transcription: ''
    }
  },
  methods: {
    handleTranscribe(transcriptionText) {
      console.log('Received transcription:', transcriptionText);
      this.transcription = transcriptionText;
    }
  }
}
</script>