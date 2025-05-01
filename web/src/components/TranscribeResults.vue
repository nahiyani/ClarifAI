<template>
    <div class="transcription-results">
      <h2 class="transcription-title">Transcription Result</h2>
      <div v-if="text" class="transcription-text">
        <pre>{{ text }}</pre>
      </div>
      <div v-else class="transcription-empty">
        <p>No transcription available yet.</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'TranscribeResults',
    props: {
      text: {
        type: String,
        default: ''
      }
    }
  }
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&display=swap');
  
  .transcription-results {
    font-family: 'Montserrat', sans-serif;
    background: linear-gradient(
      90deg,
      hsla(197, 100%, 63%, 1) 0%,
      hsla(294, 100%, 55%, 1) 100%
    );
    color: white;
    margin: 1rem auto;
    padding: 1rem 2rem 2rem;
    max-width: 90%;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
  }
  
  .transcription-title {
    font-size: 2rem;
    font-weight: 600;
    margin-bottom: 1rem;
    text-align: center;
    color: white;
  }
  
  .transcription-text {
    white-space: pre-wrap;
    word-break: break-word;
    font-size: 1.25rem;
    line-height: 1.6;
    background-color: rgba(255, 255, 255, 0.1);
    padding: 1rem;
    border-radius: 8px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 500;
  }
  
  .transcription-empty {
    font-size: 1rem;
    color: #eee;
    text-align: center;
    font-style: italic;
  }

  .transcription-text pre {
  font-family: 'Montserrat', sans-serif;
  white-space: pre-wrap;
  word-break: break-word;
  font-size: 1rem;
  line-height: 1.6;
  margin: 0;
  color: white;
}

  </style>