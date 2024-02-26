<template>
  <div class="random-image">
    <img :src="randomImageUrl" alt="Random Image" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      images: ['cartman.ico', 'kenny.png', 'kyle.png', 'stan.png']
    }
  },
  computed: {
    randomImageUrl() {
      const randomIndex = Math.floor(Math.random() * this.images.length)
      return new URL(`/src/assets/favicons/${this.images[randomIndex]}`, import.meta.url)
    }
  }
}
</script>
