<template>
  <div class="container">
    <div class="input-wrapper">
      <input
        type="text"
        v-model="youtubeUrl"
        @keyup.enter="processUrl"
        placeholder="Enter YouTube URL"
        class="search-input"
      />
      <button @click="processUrl" class="search-button">Search</button>
      <button
        v-if="videoId"
        @click="copyToClipboard"
        class="search-button copy-button"
        title="Copy URL to clipboard"
      >
        Copy
      </button>
      <button
        v-if="youtubeUrl"
        @click="clearInput"
        class="clear-button"
        title="Clear input"
      >
        &#10005;
      </button>
    </div>

    <div v-if="error" class="error">{{ error }}</div>

    <transition name="fade-slide">
      <div v-if="copied" class="copied-popup">
        Copied to clipboard!
      </div>
    </transition>

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

        <div class="action-buttons">
          <button
            @click="handleTranscribe"
            class="search-button action-button full-width-button"
          >
            Transcribe
          </button>
        </div>

        <div v-if="isTranscribing" class="transcription-container">
          <div class="transcription-header">
            <p>Transcribing video...</p>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'YoutubeSearchBar',
  data() {
    return {
      youtubeUrl: '',
      videoId: '',
      error: '',
      copied: false,
      isTranscribing: false,
      transcription: ''
    };
  },
  mounted() {
    const storedUrl = localStorage.getItem('youtube_url');
    if (storedUrl) {
      this.youtubeUrl = storedUrl;
      this.processUrl();
      localStorage.removeItem('youtube_url');
    }
  },
  methods: {
    processUrl() {
      if (!this.youtubeUrl) {
        this.error = 'Please enter a YouTube URL';
        this.videoId = '';
        this.$emit('clearTranscription'); 
        return;
      }

      const containsYouTube = /youtube\.com|youtu\.be/.test(this.youtubeUrl);
      const videoId = this.extractVideoId(this.youtubeUrl);

      if (videoId) {
        this.videoId = videoId;
        this.error = '';
        this.scrollToVideo();
      } else {
        this.videoId = '';
        this.$emit('clearTranscription');
        this.error = containsYouTube
          ? 'Invalid YouTube URL, please check and try again'
          : 'Please enter a YouTube URL';
      }
    },

    extractVideoId(url) {
      let regExp = /^.*(?:youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]{11}).*/;
      let match = url.match(regExp);
      if (match && match[1]) {
        return match[1];
      }
      regExp = /^.*youtu.be\/([^#\&\?]{11}).*/;
      match = url.match(regExp);
      return match && match[1] ? match[1] : null;
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
    },

    copyToClipboard() {
      if (this.videoId && this.youtubeUrl) {
        navigator.clipboard.writeText(this.youtubeUrl)
          .then(() => {
            this.copied = true;
            setTimeout(() => {
              this.copied = false;
            }, 2000);
          })
          .catch(err => {
            console.error("Failed to copy:", err);
          });
      }
    },

    clearInput() {
      this.youtubeUrl = '';
      this.videoId = '';
      this.error = '';
      this.transcription = '';
      this.$emit('clearTranscription');
    },

    handleTranscribe() {
      const videoId = this.extractVideoId(this.youtubeUrl);
      if (videoId) {
        this.isTranscribing = true;
        this.transcription = '';

        fetch('http://localhost:5000/transcribe', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ url: this.youtubeUrl })
        })
          .then(response => response.json())
          .then(data => {
            if (data.error) {
              this.error = data.error;
              this.$emit('clearTranscription'); 
            } else {
              this.transcription = data.transcription;
              this.$emit('transcribe', this.transcription);
            }
            this.isTranscribing = false;
          })
          .catch(err => {
            console.error('Error during transcription:', err);
            this.error = 'Failed to transcribe the video.';
            this.isTranscribing = false;
            this.$emit('clearTranscription'); 
          });
      } else {
        this.error = 'Please enter a valid YouTube URL before transcribing';
        this.$emit('clearTranscription');
      }
    },

    setYoutubeUrl(url) {
      this.youtubeUrl = url;
      this.processUrl();
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600&display=swap');

html {
  scroll-behavior: smooth;
}

.container {
  max-width: 90%;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Montserrat', sans-serif;
  background-color: white;
  text-align: center;
}

.input-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
  width: 50%;
  max-width: 50%;
  margin: 0 auto 2rem auto;
}

.search-input {
  width: 100%;
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

.copy-button {
  padding: 0.75rem 1.25rem;
}

.clear-button {
  background: none;
  border: none;
  color: #f87171;
  font-size: 1.5rem;
  cursor: pointer;
  font-family: 'Montserrat', sans-serif;
  padding: 0;
  margin-left: 0.5rem;
}

.clear-button:hover {
  color: #333;
}

.error {
  background-color: #fef2f2;
  color: #e11d48;
  padding: 0.75rem 1.25rem;
  border-radius: 8px;
  margin-bottom: 1.5rem;
  font-weight: 500;
  font-size: 1rem;
  max-width: fit-content;
  margin: 0 auto 1.5rem auto;
  transition: opacity 0.3s ease;
}

.copied-popup {
  position: fixed;
  top: 2.5%;
  left: 0;
  right: 0;
  background-color: #d1fae5;
  color: #065f46;
  padding: 0.75rem 1.25rem;
  border-radius: 8px;
  margin: 0 auto 1rem;
  max-width: fit-content;
  font-weight: 500;
  font-size: 0.95rem;
  z-index: 1000;
  animation: slideUpFade 1.5s ease-in-out forwards;
}

@keyframes slideUpFade {
  0% {
    opacity: 0;
    transform: translateY(10px);
  }
  10% {
    opacity: 1;
    transform: translateY(0);
  }
  90% {
    opacity: 1;
    transform: translateY(0);
  }
  100% {
    opacity: 0;
    transform: translateY(-10px);
  }
}

.video-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.video-wrapper {
  width: 80%;
  position: relative;
  padding-bottom: 45%;
  height: 0;
  overflow: hidden;
  border-radius: 12px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  margin: 0 auto;
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

.action-buttons {
  display: flex;
  justify-content: center;
  margin-top: 1.5rem;
  width: 100%;
}

.action-button.full-width-button {
  width: 50%;
  min-width: 240px;
}

.transcription-container {
  margin-top: 2rem;
}

.transcription-header {
  font-size: 1.2rem;
  font-weight: 500;
  margin-bottom: 1rem;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>