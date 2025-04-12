<template>
    <div>
      <div v-if="showSuccess" class="toast success-toast">
        <span class="icon"></span> Message sent successfully!
      </div>
  
      <form class="form" @submit.prevent="submitForm" novalidate>
        <div class="form-group">
          <label for="firstName">First Name</label>
          <input
            id="firstName"
            v-model="form.firstName"
            type="text"
            :class="{'input': true, 'is-invalid': errors.firstName}"
          />
          <p v-if="errors.firstName" class="error">{{ errors.firstName }}</p>
        </div>
  
        <div class="form-group">
          <label for="lastName">Last Name</label>
          <input
            id="lastName"
            v-model="form.lastName"
            type="text"
            :class="{'input': true, 'is-invalid': errors.lastName}"
          />
          <p v-if="errors.lastName" class="error">{{ errors.lastName }}</p>
        </div>
  
        <div class="form-group">
          <label for="email">Email Address</label>
          <input
            id="email"
            v-model="form.email"
            type="email"
            :class="{'input': true, 'is-invalid': errors.email}"
          />
          <p v-if="errors.email" class="error">{{ errors.email }}</p>
        </div>
  
        <div class="form-group">
          <label for="subject">Subject</label>
          <input
            id="subject"
            v-model="form.subject"
            type="text"
            :class="{'input': true, 'is-invalid': errors.subject}"
          />
          <p v-if="errors.subject" class="error">{{ errors.subject }}</p>
        </div>
  
        <div class="form-group">
          <label for="message">Message</label>
          <textarea
            id="message"
            v-model="form.message"
            rows="3"
            ref="messageInput"
            @input="autoGrow"
            :class="{'input': true, 'is-invalid': errors.message}"
          ></textarea>
          <p v-if="errors.message" class="error">{{ errors.message }}</p>
        </div>
  
        <button type="submit" class="submit-button">Send</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { reactive, ref } from 'vue'
  
  const form = reactive({
    firstName: '',
    lastName: '',
    email: '',
    subject: '',
    message: ''
  })
  
  const errors = reactive({
    firstName: '',
    lastName: '',
    email: '',
    subject: '',
    message: ''
  })
  
  const showSuccess = ref(false)
  const messageInput = ref(null)
  
  const autoGrow = () => {
    const el = messageInput.value
    if (el) {
      el.style.height = 'auto'
      el.style.height = el.scrollHeight + 'px'
    }
  }
  
  const validateEmail = (email) => {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return re.test(email)
  }
  
  const submitForm = () => {
    Object.keys(errors).forEach(key => errors[key] = '')
    let hasError = false
  
    if (!form.firstName) {
      errors.firstName = 'First name is required'
      hasError = true
    }
    if (!form.lastName) {
      errors.lastName = 'Last name is required'
      hasError = true
    }
    if (!form.email) {
      errors.email = 'Email is required'
      hasError = true
    } else if (!validateEmail(form.email)) {
      errors.email = 'Please enter a valid email address'
      hasError = true
    }
    if (!form.subject) {
      errors.subject = 'Subject is required'
      hasError = true
    }
    if (!form.message) {
      errors.message = 'Message is required'
      hasError = true
    }
  
    if (!hasError) {
      showSuccess.value = true
  
      // Clear form after submission
      Object.keys(form).forEach(key => form[key] = '')
  
      // Hide toast after 2 seconds
      setTimeout(() => {
        showSuccess.value = false
      }, 2000)
    }
  }
  </script>
  
  <style scoped>
  * {
    box-sizing: border-box;
  }

  .form {
    width: 50vw;
    max-width: none;
    margin: 0 auto;
    padding: 2rem;
    font-family: 'Montserrat', sans-serif;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    overflow: hidden;
  }

  .form-group {
    display: flex;
    flex-direction: column;
  }

  label {
    font-weight: 600;
    margin-bottom: 0.5rem;
    background: linear-gradient(90deg, hsla(197, 100%, 63%, 1) 0%, hsla(294, 100%, 55%, 1) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    position: relative;
  }

  label::after {
    content: ' *';
    color: #dc3545;
    font-weight: bold;
    position: relative;
  }

  .input {
    width: 100%;
    box-sizing: border-box;
    font-family: 'Montserrat', sans-serif;
    padding: 0.75rem;
    border: 1px solid #ccc;
    border-radius: 0.5rem;
    font-size: 1rem;
    transition: border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
  }

  .input:focus {
    border-color: #9f43e3;
    box-shadow: 0 0 0 3px rgba(159, 67, 227, 0.25);
    outline: none;
  }

  textarea.input {
    resize: none;
    overflow: hidden;
    font-size: 0.85rem;
  }

  .is-invalid {
    border-color: #9f43e3 !important;
    box-shadow: 0 0 0 3px rgba(159, 67, 227, 0.25);
  }

  .error {
    color: #dc3545;
    margin-top: 0.25rem;
    font-size: 0.9rem;
    font-weight: bold;
  }

  .submit-button {
    width: 25vw;
    align-self: center;
    font-family: 'Montserrat', sans-serif;
    background: linear-gradient(90deg, hsla(197, 100%, 63%, 1) 0%, hsla(294, 100%, 55%, 1) 100%);
    color: white;
    font-weight: bold;
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 0.75rem;
    cursor: pointer;
    font-size: 1rem;
    transition: background 0.3s ease;
  }

  .submit-button:hover {
    background: linear-gradient(90deg, hsla(197, 100%, 63%, 1) 0%, hsla(294, 100%, 55%, 1) 100%);
  }

  .success-toast {
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

  .success-toast .icon {
    font-size: 1.2rem;
  }

  @keyframes fadeSlide {
    0% {
      opacity: 0;
      transform: translateX(-50%) translateY(-20px);
    }
    15% {
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }
    85% {
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }
    100% {
      opacity: 0;
      transform: translateX(-50%) translateY(-10px);
    }
  }
</style>