<script>
import QuestionDisplay from './QuestionDisplay.vue'
import QuizApiService from '../services/QuizApiService.js'
import ParticipationStorageService from '../services/ParticipationStorageService.js'
import RandomIco from './RandomIco.vue'
import LoadingSpinner from './LoadingSpinner.vue'
import RandomError from './RandomError.vue'

export default {
  components: {
    QuestionDisplay,
    RandomIco,
    LoadingSpinner,
    RandomError
  },
  data() {
    return {
      currentQuestion: {
        questionTitle: '',
        questionText: '',
        questionImage: '',
        possibleAnswers: []
      },
      currentQuestionPosition: 1,
      totalNumberOfQuestion: 0,
      randomIcoKey: 0,
      errorMessage: '',
      error: false,
      isLoading: true,
      answers: []
    }
  },
  /*
    When the component is initialized, retrieve the information needed to display the first question. 
    Note that you will also need to know the total number of questions in the quiz at this time and store it.
  */
  async created() {
    await QuizApiService.getQuizInfo()
      .then((response) => {
        this.totalNumberOfQuestion = response.data.size
      })
      .catch((err) => {
        console.error('ERR:', err)
        this.error = true
        this.errorMessage = 'Impossible de récupérer les données du quizz.'
      })
      .finally(() => {
        this.isLoading = false
      })
    if (!this.error) {
      await this.loadQuestionByPosition()
    }
  },
  methods: {
    async loadQuestionByPosition() {
      this.isLoading = true
      await QuizApiService.getQuestion(this.currentQuestionPosition)
        .then((response) => {
          this.currentQuestion = response.data
        })
        .catch((err) => {
          console.error('ERR:', err)
          this.error = true
          this.errorMessage = 'Impossible de récupérer la question'
        })
        .finally(() => {
          this.isLoading = false
        })
    },
    async answerClickedHandler(answerIndex) {
      this.answers.push(answerIndex);

      // Add a delay using setTimeout
      await new Promise((resolve) => {
        setTimeout(resolve, 500); // Adjust the delay time as needed (in milliseconds)
      });

      const newPos = this.currentQuestionPosition + 1

      if (newPos === this.totalNumberOfQuestion + 1) {
        this.endQuiz()
      } else {
        this.currentQuestionPosition = newPos
        this.loadQuestionByPosition()
      }
      this.randomIcoKey++;
    },
    async endQuiz() {
      this.isLoading = true
      QuizApiService.postAnswer(ParticipationStorageService.getPlayerName(), this.answers)
        .then((response) => {
          const result = response.data.score
          ParticipationStorageService.saveParticipationScore(result)
          this.$router.push('/result-page')
        })
        .catch((error) => {
          console.log(`ERR : ${error}`)
        })
      console.log(`END QUIZ`)
    }
  }
}
</script>

<template>
  <div>
    <transition name="question-transition" mode="out-in">
      <div v-if="isLoading">
        <LoadingSpinner />
        <p>Chargement en cours...</p>
      </div>
      <div v-else-if="error">
        <RandomError />
        <p>{{ errorMessage }}</p>
      </div>
      <div v-else id="question-card" class="d-flex align-items-center flex-column">
        <RandomIco :key="randomIcoKey" class="mb-4" />
        <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
        <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
      </div>
    </transition>
  </div>
</template>

<style>
.question-transition-enter-active,
.question-transition-leave-active {
  transition: opacity 1.25s, transform 1s;
}

question-transition-enter-from,
.question-transition-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}
</style>