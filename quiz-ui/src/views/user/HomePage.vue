<script>
import quizApiService from "@/services/QuizApiService";
import ResultsTable from "../../components/ResultsTable.vue";

export default {
	methods: {
		startQuiz() {
			this.$router.push('/new-quiz-page');
		}
	},
	components: {
		ResultsTable
	},
	name: "HomePage",
	data() {
		return {
			registeredScores: [],
			participations: [],
			error: false,
			errorMessage: '',
		};
	},
	async created() {
		console.log("Composant Home page 'created'");
		try {
			await quizApiService.getQuizInfo().then((response) => {
				this.registeredScores = response.data;
				this.participations = response.data.scores.sort((a, b) => a[0] - b[0]);
			}).catch((error) => {
				console.error('ERR:', error);
				this.error = true;
				this.errorMessage = 'Impossible de recuperer les donnees des scores';
			});
		} catch (err) {
			console.log(err)
		}
	}
};
</script>

<template>
	<div id="main" class="d-flex w-100 flex-column">
		<h1 class="align-self-center mb-4">Bienvenue à SouthPark</h1>
		<div class="d-flex justify-content-center flex-column" id="participations-container">
			<button class="align-self-center mb-4 btn w-25 btn-success" @click="startQuiz">Démarrer le quiz !</button>
			<div v-if="participations.length > 0" id="w-100">
				<ResultsTable :participations="participations" />
			</div>
		</div>
	</div>
</template>
