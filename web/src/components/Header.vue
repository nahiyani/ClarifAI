<template>
  <div class="banner">
    <header
      class="main-header"
      @mouseover="hover = true"
      @mouseleave="hover = false"
      :class="{ hovered: hover }"
    >
      <div class="header-content">
        <h1 class="site-title">ClarifAI</h1>
        <nav class="menu">
          <ul>
            <li><a href="#">Transcribe</a></li>
            <li><a href="#">Summarize</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </nav>
      </div>
    </header>
  </div>
</template>

<script>
export default {
  data() {
    return {
      hover: false,
    };
  },
};
</script>

<style scoped>
.banner {
  font-family: 'Montserrat', sans-serif;
  background: linear-gradient(
    90deg,
    hsla(197, 100%, 63%, 1) 0%,
    hsla(294, 100%, 55%, 1) 100%
  );
  color: white;
  margin: 0;
  padding: 0;
  min-height: 5vh;
}

.main-header {
  padding: 0.5rem 2rem;
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
  position: sticky;
  top: 0;
  z-index: 100;
  height: 3rem;
}

.main-header.hovered {
  background-color: rgba(255, 255, 255, 0.1);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
}

.site-title {
  font-weight: 600;
  font-size: 2rem;
  margin: 0;
}

.menu ul {
  list-style: none;
  display: flex;
  gap: 1.5rem;
}

.menu a {
  font-size: 0.75rem;
  color: white;
  text-decoration: none;
  font-weight: 500;
  transition: opacity 1s;
}

.menu a:hover {
  opacity: 0.75;
}
</style>