<template>
    <div class="banner-container">
      <h1 class="page-title">{{ pageTitle }}</h1>
      <p class="description">{{ description }}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Banner',
    props: {
      pageTitle: {
        type: String,
        required: true
      },
      description: {
        type: String,
      }
    },
    computed: {
      displayWord() {
        return this.pageTitle;
      },
      displayDescription(){
        return this.description
      }
    }
  }
  </script>
  
  <style>
    .banner-container {
      width: 100%;
      text-align: center;
      background: linear-gradient(90deg, hsla(197, 100%, 63%, 1) 0%, hsla(294, 100%, 55%, 1) 100%);
      padding: 3.5rem 1rem;
      font-family: 'Montserrat', sans-serif;
    }
  
    .page-title {
      font-size: 5rem;
      font-weight: 600;
      color: white;
      margin: 0;
      line-height: 1;
    }
  
    .description {
      font-size: 1.5rem;
      margin-top: 2.5rem;
      width: 75%;
      margin-left: auto;
      margin-right: auto;
      color: white;
    }
  
    @media (max-width: 768px) {
      .page-title {
        font-size: 3.5rem;
        padding: 2rem 1rem;
      }
      .description {
        font-size: 1.3rem;
        width: 80%;
      }
    }
  
    @media (max-width: 480px) {
      .page-title {
        font-size: 2.5rem;
        padding: 1.5rem 1rem;
      }
      .description {
        font-size: 1.1rem;
        width: 90%;
      }
    }
  </style>  