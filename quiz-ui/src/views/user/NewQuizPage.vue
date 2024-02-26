<template>
  <div>
    <h1>Nouveau participant</h1>
    <div>
      <form class="d-flex align-items-center flex-column" @submit.prevent="launchNewQuiz">
        <p v-if="showErrorMessage" class="text-danger">Un pseudo vide vraiment ?</p>
        <p v-else class="text-center">Entrer votre pseudo :</p>
        <input
          type="text"
          class="w-75"
          placeholder="Cartman"
          v-model="username"
          @keydown.enter="launchNewQuiz"
        />

        <button @click="launchNewQuiz" type="button" class="w-100 mt-3 btn btn-primary btn-lg">
          Commencer le questionnaire
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import participationStorageService from '@/services/ParticipationStorageService'
// ...
export default {
  name: 'NewQuizPage',
  data() {
    return {
      username: '',
      showErrorMessage: false
    }
  },
  methods: {
    launchNewQuiz() {
      if (this.username.trim() === '') {
        this.showErrorMessage = true
      } else {
        participationStorageService.savePlayerName(this.username)
        const playerName = participationStorageService.getPlayerName()
        console.log('Launch New Quiz with', playerName)
        this.$router.push('/quiz-page')
      }
    }
  }
}
</script>

<style scoped>
h1 {
  margin-bottom: 2%;
}
</style>
