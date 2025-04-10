<template>
    <footer class="footer">
      <div class="footer-content">
        <p class="footer-text">
          &copy; 2025 ClarifAI. Some rights reserved.
        </p>
        <div class="social-icons">
          <a href="https://www.facebook.com" class="social-icon" aria-label="Facebook">
            <img src="../assets/facebook-logo.png" alt="Facebook">
          </a>
          <a href="https://x.com" class="social-icon" aria-label="X">
            <img src="../assets/x-logo.png" alt="X">
          </a>
          <a href="https://www.instagram.com" class="social-icon" aria-label="Instagram">
            <img src="../assets/instagram-logo.png" alt="Instagram">
          </a>
        </div>
      </div>
    </footer>
  </template> 
  
  <script>
  export default {
    name: 'Footer'
  }
  </script>
  
  <style scoped>
  .footer {
    background: linear-gradient(90deg, hsla(197, 100%, 63%, 1) 0%, hsla(294, 100%, 55%, 1) 100%);
    color: white;
    padding: 2rem;
    font-family: 'Montserrat', sans-serif;
    text-align: center;
    border-top: 2px solid #fff;
  }
  
  .footer-content {
    max-width: 80%;
    margin: 0 auto;
  }
  
  .footer-text {
    font-size: 1rem;
    font-weight: bold;
    margin-bottom: 1.5rem;
  }
  
  .social-icons {
    display: flex;
    justify-content: center;
    gap: 1rem;
  }
  
  .social-icon {
    display: inline-block;
    width: 24px;
    height: 24px;
    transition: transform 0.3s ease;
  }
  
  .social-icon img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }
  
  .social-icon:hover {
    transform: scale(1.1);
  }
  
  .social-icon:focus {
    outline: 2px solid #fff;
  }
  </style>  