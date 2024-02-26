<script>
import quizApiService from "@/services/QuizApiService";
import AdminNav from "../../components/AdminNav.vue";

export default {
	methods: {
		startQuiz() {
			this.$router.push('/new-quiz-page');
		}
	},
	components: {
		AdminNav,
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
		<AdminNav/>
	</div>
</template>

<style scoped>	#participations-container {
		display: flex !important;
		flex-direction: column !important;
		justify-content: center !important;
	}
</style>