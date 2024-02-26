<script>
import { defineComponent } from 'vue';
import logo from '@/assets/logo.png';

export default defineComponent({
  data() {
    return {
      logo: logo
    };
  }
});
</script>

<script setup>
</script>

<template>
  <div class="header">
    <nav>
      <router-link to="/">Home</router-link>
      <router-link to="/login">Login</router-link>
      <router-link to="/cgus">CGUs</router-link>
      <div class="logo_wrapper">
        <img class="logo" :src="logo" alt="Logo" />
      </div>
    </nav>
  </div>
  <div class="main-content">
    <RouterView />
  </div>
</template>

<style scoped>
.header {
  width: 100%;
  z-index: 1;
  /* border: 5px solid green; */
  /* display: block; */
  height: max-content;
  grid: auto;
  /* margin-bottom: 0.5em; */
}

.logo {
  margin-right: 2%;
  height: 2em;
}

.logo_wrapper {
  margin-left: auto;
}

nav {
  padding: 2px;
  width: 100%;
  font-size: 2em;
  text-align: left;
  padding-left: 1.25em;
  /* border: 5px solid blue !important; */
  background-color: #b8f3ff;
  border-radius: 50px;
  display: flex;
  /* justify-content: center; */
  align-items: center;
}

nav a.router-link-exact-active {
  color: #4c04f4;
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  .header {
    place-items: center;
  }

  .logo {
    margin: 0 2rem 0 0;
  }
}
</style>
