<template>
  <transition name="fade" mode="out-in">
    <component :is="currentComponent" />
  </transition>
</template>

<script>
import { shallowRef } from 'vue';

export default {
  name: 'FadeTransition',
  data() {
    return {
      currentComponent: null,
    };
  },
  watch: {
    $route(to, from) {
      this.updateCurrentComponent(to, from);
    },
  },
  created() {
    this.updateCurrentComponent(this.$route);
  },
  methods: {
    async updateCurrentComponent(to) {
      const component = await to.meta.transitionComponent();
      this.currentComponent = shallowRef(component.default || component);
    },
  },
};
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.33s ease-in-out, transform 0.50s ease-in-out;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: scale(0);
}

.fade-enter-to,
.fade-leave-from {
  opacity: 1;
  transform: scale(1);
}
</style>
