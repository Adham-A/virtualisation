

<script>
import ParticipationStorageService from '../../services/ParticipationStorageService';
import QuizApiService from '../../services/QuizApiService';
import ResultsTable from '../../components/ResultsTable.vue';

export default {
	name: 'result-page',
	components : {
		ResultsTable,
	},
	data() {
		return { 
			totalQuestions: 0,
			participations: [],
      error: false,
			errorMessage: '',
		}
	},
	computed: {
		getName() {
			return ParticipationStorageService.getPlayerName();
		},
		getScore() {
			const score = ParticipationStorageService.getParticipationScore();
			return score >= 0 ? score : 'No Score' ;
		}
	},
	async created() {
		await QuizApiService.getQuizInfo().then((response) => {
			this.totalQuestions = response.data.size; 
			this.participations = response.data.scores;
			console.log(response);
		}).catch((err) => {
			console.error('ERR:', err);
      this.error = true;
			this.errorMessage = 'Impossible de recuperer les donnees des scores';
		}); 
	},
 }
</script>

<template>
  <div class="result">
		<div v-if="error">
      <RandomError />
      <p class="text-center">
        <i class="error-icon bi bi-x-octagon"></i>
      </p>
      <p>{{ errorMessage }}</p>
    </div>
		<div v-else>
			<h1>Result Page</h1>
			<div id="container">
				<div id="scoreboard"> 
					<div class="shadow rounded w-100 mb-5 p-3 card player-card">
						<div class="card-body">
							<h2 class="card-title">Score actuel</h2>
							<p class="card-subtitle">Player : {{ getName }}</p>
							<p  class="font-weight-bold">Score : {{ getScore }}/{{ this.totalQuestions }}</p>
						</div>
					</div>
					<div class="shadow rounded w-100 p-3 card player-card"> 
						<div class="card-body">
							<h2 class="card-title">Meilleur score</h2>
							<p class="card-subtitle">Player : {{ this.participations[0].playerName }}</p>
							<p class="font-weight-bold">Score : {{ this.participations[0].score }}/{{ this.totalQuestions }}</p>
						</div>	
					</div>
				</div>
				<div class="w-100">
					<ResultsTable :participations="participations" />
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped>  
.result {
	width: 100%;
}

#container {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
}

#scoreboard {
	display: flex;
	flex-direction: column;
	width: 50%;
}


.player-card {
	color: #443266;
	background-color: #c3c3e5;
}  
 
p {
	max-width: 100%;
	font-size: 20px;
	word-wrap: break-word;
}
</style>
