<template>
    <section ref="cardSection" class="card-section" :class="{ visible: isVisible }">
      <div class="card" v-for="(card, index) in cards" :key="index">
        <p class="description">{{ card.description }}</p>
        <button class="action-button">{{ card.buttonText }}</button>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isVisible: false,
        cards: [
          { description: 'Transcribe YouTube videos, with or without captions present.', buttonText: 'Transcribe' },
          { description: 'Summarize videos using audio, visual stream or both.', buttonText: 'Try Now' },
          { description: 'Clarify long content with just one click.', buttonText: 'Get Started' },
        ],
      };
    },
    mounted() {
      const observer = new IntersectionObserver(
        ([entry]) => {
          if (entry.isIntersecting) this.isVisible = true;
        },
        { threshold: 0.1 }
      );
      observer.observe(this.$refs.cardSection);
    },
  };
  </script>
  
  <style scoped>
  .card-section {
    display: flex;
    justify-content: center;
    align-items: stretch; /* 👈 Ensure equal height */
    gap: 2rem;
    padding: 4rem 2rem;
    opacity: 0;
    transform: translateY(40px);
    transition: all 0.8s ease;
    font-family: 'Montserrat', sans-serif;
  }
  
  .card-section.visible {
    opacity: 1;
    transform: translateY(0);
  }
  
  .card {
    background: white;
    color: #333;
    border-radius: 16px;
    padding: 2rem;
    width: 300px;
    text-align: center;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
    justify-content: space-between; /* 👈 Keep button at bottom */
  }
  
  .card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
  }
  
  .description {
    font-size: 1.2rem;
    margin-bottom: 1.5rem;
    flex-grow: 1;
  }
  
  .action-button {
    background: linear-gradient(90deg, #06b6d4, #c026d3);
    color: white;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1rem;
    transition: background 0.3s ease;
    font-family: 'Montserrat', sans-serif;
  }
  
  .action-button:hover {
    background: linear-gradient(90deg, #0ea5e9, #d946ef);
  }
  </style> 