<template>
    <div class="auto-typer">
      <h1><span class="word">{{ currentWord }}</span></h1>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        words: ['Transcribed.', 'Summarized.', 'ClarifAIed.'],
        currentWord: '',
        wordIndex: 0,
        charIndex: 0,
        isDeleting: false,
      };
    },
    mounted() {
      this.type();
    },
    methods: {
      type() {
        const word = this.words[this.wordIndex];
        if (this.isDeleting) {
          this.charIndex--;
        } else {
          this.charIndex++;
        }
  
        this.currentWord = word.substring(0, this.charIndex);
  
        let delay = this.isDeleting ? 100 : 200;
  
        if (!this.isDeleting && this.charIndex === word.length) {
          delay = 1000;
          this.isDeleting = true;
        } else if (this.isDeleting && this.charIndex === 0) {
          this.isDeleting = false;
          this.wordIndex = (this.wordIndex + 1) % this.words.length;
          delay = 500;
        }
  
        setTimeout(this.type, delay);
      },
    },
  };
  </script>
  
  <style scoped>
  .auto-typer {
    font-family: 'Montserrat', sans-serif;
    background: linear-gradient(
      90deg,
      hsla(197, 100%, 63%, 1) 0%,
      hsla(294, 100%, 55%, 1) 100%
    );
    color: white;
    text-align: center;
    font-size: 3rem;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
  }
  
  .word {
    font-weight: 600;
    padding-left: 0.5rem;
    position: relative;
  }
  
  .word::after {
    content: '';
    position: absolute;
    right: -5px;
    top: 0;
    width: 2px;
    height: 100%;
    background-color: white;
    animation: glide-blink 1s infinite;
    transition: right 0.2s ease-in-out;
  }
  
  @keyframes glide-blink {
    0%, 49% {
      opacity: 1;
    }
    50%, 100% {
      opacity: 0;
    }
  }
  </style>    