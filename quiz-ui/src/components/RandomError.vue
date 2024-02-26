<template>
  <div>
    <div class="d-flex justify-content-center mb-3 random-image">
      <img :src="randomImageUrl" width="128" alt="Random Image" />
    </div>
    <p class="text-center">
      <i class="error-icon bi bi-x-octagon"></i>
    </p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      images: ['sad-stan.png', 'sad-kyle.png']
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
