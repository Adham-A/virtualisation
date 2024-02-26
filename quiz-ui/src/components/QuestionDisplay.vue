<template>
  <div class="d-flex align-items-center flex-column">
    <h2>{{ question.title }}</h2>
    <img v-if="question.image" :src="question.image" height="300" />
    <p class="mt-3">{{ question.text }}</p>
    <div class="w-100 d-flex justify-content-center align-items-center flex-column">
      <div class="w-100 d-flex justify-content-center align-items-center"
        v-for="(answer, index) in question.possibleAnswers" :key="answer.id"
        :class="{ selected: selectedAnswer === index + 1 }">
        <a class="questions-class" @click="handleAnswerClick(index + 1)" :disabled="isAnswerDisabled(index + 1)">{{
          answer.text }}</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'QuestionDisplay',
  props: {
    question: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      selectedAnswer: null,
      answered: false,
    };
  },
  methods: {
    handleAnswerClick(answerIndex) {
      if (!this.answered) {
        this.selectedAnswer = answerIndex;
        this.$emit('answer-selected', answerIndex);
        this.answered = true;
      }
    },
    isAnswerDisabled(answerIndex) {
      return this.answered && this.selectedAnswer !== answerIndex;
    },
  },
};
</script>

<style scoped>
.selected .questions-class {
  background-color: #b2cef1;
}
</style>
