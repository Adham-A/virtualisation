<script>
import QuizApiService from '../../services/QuizApiService';


export default {
	name: "QuestionList",
	data() {
		return {
			questions: [],
			canCreate: false,
		}
	},
	async created() {
		this.getAllQuestions();
	},
	methods: {
		async getAllQuestions() {
			await QuizApiService.getQuizInfo().then((response) => {
				const totalQuestions = response.data.size;
				if(totalQuestions< 10 && totalQuestions>= 0) {
					this.canCreate = true;
				}

				for(let i = 0; i < totalQuestions; i++) {
					this.questions[i] = QuizApiService.getQuestionById(i);
					console.log(this.questions[i])
				}
			})
		}
	}
}
</script>

<template>
	<div id="main" class="d-flex w-50 flex-column">
		<div v-if="canCreate" class="" id="question-creation">
			<button class="align-self-center mb-4 btn w-25 btn-success" @click="startQuiz">Creér une question</button>
		</div>
		<div class="">
			<div v-for="(question) in this.questions" :key="question.id">
				<div class="card">
					<p class="card-title">
						{{question.title}}
					</p>
					<p class="card-body">
						{{question.text}}
					</p>
				</div>
			</div>
		</div>
	</div>
</template>