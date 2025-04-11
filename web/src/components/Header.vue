<template>
  <div>
    <div class="banner">
      <header class="main-header" 
        @mouseover="hover = true" 
        @mouseleave="hover = false" 
        :class="{ hovered: hover }">
        <div class="header-content">
          <h1 class="site-title">ClarifAI</h1>
          <button class="menu-toggle" :class="{ 'is-open': mobileMenuOpen }" @click="toggleMenu" aria-label="Toggle menu">
            <div class="toggle-icon-container">
              <span :class="{ open: mobileMenuOpen }"></span>
              <span :class="{ open: mobileMenuOpen }"></span>
              <span :class="{ open: mobileMenuOpen }"></span>
            </div>
          </button>
          <nav class="menu" :class="{ open: mobileMenuOpen }">
            <ul>
              <li><a href="#">Transcribe</a></li>
              <li><a href="#">Summarize</a></li>
              <li><a href="#">Contact</a></li>
            </ul>
          </nav>
        </div>
      </header>
    </div>
    
    <div 
      v-if="mobileMenuOpen && isMobileView" 
      class="page-overlay" 
      @click="closeMenu"
    ></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      hover: false,
      mobileMenuOpen: false,
      isMobileView: false,
      resizeObserver: null
    };
  },
  mounted() {
    
    this.checkScreenSize();
    
    this.resizeObserver = new ResizeObserver(this.checkScreenSize);
    this.resizeObserver.observe(document.body);
    
    window.addEventListener('resize', this.checkScreenSize);
  },
  methods: {
    toggleMenu() {
      this.mobileMenuOpen = !this.mobileMenuOpen;
      if (this.mobileMenuOpen) {
        document.body.classList.add('menu-open');
      } else {
        document.body.classList.remove('menu-open');
      }
    },
    closeMenu() {
      this.mobileMenuOpen = false;
      document.body.classList.remove('menu-open');
    },
    checkScreenSize() {
      const wasMobileView = this.isMobileView;
      this.isMobileView = window.innerWidth <= 768;
      
      if (wasMobileView && !this.isMobileView && this.mobileMenuOpen) {
        this.closeMenu();
      }
    }
  },
  beforeUnmount() {
    document.body.classList.remove('menu-open');
    
    if (this.resizeObserver) {
      this.resizeObserver.disconnect();
    }
    window.removeEventListener('resize', this.checkScreenSize);
  }
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
  position: relative;
  z-index: 101;
}

.main-header {
  padding: 0.5rem 2rem;
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
  position: sticky;
  top: 0;
  z-index: 101;
  height: auto;
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
  flex-wrap: wrap;
}

.site-title {
  font-weight: 600;
  font-size: 2rem;
  margin: 0;
}

.menu-toggle {
  display: none;
  justify-content: center;
  align-items: center;
  height: 2rem;
  width: 2rem;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0;
  z-index: 110;
  overflow: visible;
  transition: height 0.3s ease, width 0.3s ease;
}

.menu-toggle.is-open {
  height: 2.5rem;
  width: 2.5rem;
}

.toggle-icon-container {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
}

.menu-toggle span {
  display: block;
  height: 2px;
  width: 1.25rem;
  background-color: white;
  border-radius: 2px;
  transition: transform 0.3s ease, opacity 0.3s ease;
  margin: 3px 0;
  position: absolute;
}

.menu-toggle span:nth-child(1) {
  transform: translateY(-6px);
}

.menu-toggle span:nth-child(3) {
  transform: translateY(6px);
}

.menu-toggle span.open:nth-child(1) {
  transform: rotate(45deg);
}

.menu-toggle span.open:nth-child(2) {
  opacity: 0;
}

.menu-toggle span.open:nth-child(3) {
  transform: rotate(-45deg);
}

.menu {
  display: flex;
}

.menu ul {
  list-style: none;
  display: flex;
  gap: 1.5rem;
  padding: 0;
  margin: 0;
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

.page-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 99;
  cursor: pointer;
  margin-top: 0;
}

@media (max-width: 768px) {
  .menu {
    width: 100%;
    flex-direction: column;
    overflow: hidden;
    max-height: 0;
    transition: max-height 0.3s ease-in-out;
  }
  
  .menu.open {
    max-height: 300px;
  }
  
  .menu ul {
    flex-direction: column;
    gap: 1rem;
    margin-top: 1rem;
  }
  
  .menu-toggle {
    display: flex;
  }
}
</style>