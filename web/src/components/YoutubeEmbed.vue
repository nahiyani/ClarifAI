<template>
    <div class="container">
      <h1 class="title">YouTube Video Finder</h1>
  
      <div class="input-wrapper">
        <input 
          type="text" 
          v-model="youtubeUrl" 
          @keyup.enter="processUrl"
          placeholder="Enter YouTube URL" 
          class="search-input"
        />
        <button @click="processUrl" class="search-button">Search</button>
      </div>
  
      <div v-if="error" class="error">{{ error }}</div>
  
      <transition name="fade">
        <div v-if="videoId" class="video-container">
          <div class="video-wrapper">
            <iframe 
              :src="`https://www.youtube.com/embed/${videoId}`" 
              frameborder="0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen
            ></iframe>
          </div>
        </div>
      </transition>
    </div>
  </template>
  
  <script>
  export default {
    name: 'YouTubeVideoFinder',
    data() {
      return {
        youtubeUrl: '',
        videoId: '',
        error: ''
      }
    },
    methods: {
      processUrl() {
        if (!this.youtubeUrl) {
          this.error = 'Please enter a YouTube URL';
          this.videoId = '';
          return;
        }
  
        try {
          const videoId = this.extractVideoId(this.youtubeUrl);
  
          if (videoId) {
            this.videoId = videoId;
            this.error = '';
            this.scrollToVideo();
          } else {
            this.error = 'Invalid YouTube URL. Please check and try again.';
            this.videoId = '';
          }
        } catch (err) {
          this.error = 'An error occurred while processing the URL.';
          console.error(err);
          this.videoId = '';
        }
      },
  
      extractVideoId(url) {
        let regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
        let match = url.match(regExp);
  
        if (match && match[2].length === 11) {
          return match[2];
        }
  
        regExp = /^.*(youtu.be\/)([^#\&\?]*).*/;
        match = url.match(regExp);
  
        if (match && match[2].length === 11) {
          return match[2];
        }
  
        return null;
      },
  
      scrollToVideo() {
        setTimeout(() => {
          const videoElement = document.querySelector('iframe');
          if (videoElement) {
            videoElement.scrollIntoView({ 
              behavior: 'smooth',
              block: 'center'
            });
          }
        }, 300);
      }
    }
  }
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&display=swap');
  
  html {
    scroll-behavior: smooth;
  }
  
  .container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 2rem;
    font-family: 'Montserrat', sans-serif;
    background-color: white;
    text-align: center;
    min-height: 100vh;
  }
  
  .title {
    font-size: 2.5rem;
    font-weight: bold;
    padding: 1rem;
    border-radius: 12px;
    background: linear-gradient(90deg, hsla(197, 100%, 63%, 1) 0%, hsla(294, 100%, 55%, 1) 100%);
    color: white;
    margin-bottom: 2rem;
  }
  
  .input-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 0.75rem;
    max-width: 700px;
    margin: 0 auto 2rem auto;
  }
  
  .search-input {
    flex: 1;
    padding: 0.75rem 1rem;
    border-radius: 15px;
    border: 2px solid transparent;
    background-image: linear-gradient(white, white), 
                      linear-gradient(90deg, hsla(197, 100%, 63%, 1), hsla(294, 100%, 55%, 1));
    background-origin: border-box;
    background-clip: padding-box, border-box;
    font-size: 1rem;
    color: black;
    font-family: 'Montserrat', sans-serif;
    outline: none;
    transition: border-color 0.3s ease;
  }
  
  .search-input:focus {
    border-color: transparent;
  }
  
  .search-button {
    background: linear-gradient(90deg, hsla(197, 100%, 63%, 1), hsla(294, 100%, 55%, 1));
    color: white;
    font-weight: bold;
    border: none;
    padding: 0.75rem 1.25rem;
    border-radius: 12px;
    cursor: pointer;
    font-family: 'Montserrat', sans-serif;
    font-size: 1rem;
    transition: background 0.3s ease;
  }
  
  .search-button:hover {
    background: linear-gradient(90deg, hsla(197, 100%, 58%, 1), hsla(294, 100%, 50%, 1));
  }
  
  .error {
    color: #f87171; /* soft red */
    margin-bottom: 1.5rem;
    font-weight: 500;
  }
  
  .video-container {
    display: flex;
    justify-content: center;
  }
  
  .video-wrapper {
    width: 100%;
    max-width: 800px;
    position: relative;
    padding-bottom: 56.25%;
    height: 0;
    overflow: hidden;
    border-radius: 12px;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  }
  
  .video-wrapper iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: 0;
    border-radius: 12px;
  }
  
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s ease;
  }
  .fade-enter-from, .fade-leave-to {
    opacity: 0;
  }
  </style>