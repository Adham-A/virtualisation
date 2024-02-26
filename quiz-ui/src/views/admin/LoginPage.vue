<template>
    <div>
        <transition name="auth-transition" mode="out-in">
            <div v-if="isLoading">
                <LoadingSpinner />
                <p>Authentification en cours...</p>
            </div>
            <div v-else-if="!error">
                <h1 class="text-center">Connexion à la page d'administration</h1>
                <div class="d-flex flex-column align-items-center mt-5 register custom_logo_background">
                    <div class="col-6">
                        <input type="text" class="mb-3 form-control" v-model="username" placeholder="Skankhunt42" />
                        <input type="password" class="mb-3 form-control" v-model="password" placeholder="Mot de passe" />
                    </div>
                    <button @click="login" class="col-6 mb-3 btn btn-success" type="button">Se connecter</button>
                </div>
            </div>
            <div v-else>
                <RandomError />
                <p>{{ errorMessage }}</p>
                <button @click="retryLogin" class="form-control btn btn-primary" type="button">Réessayer</button>
            </div>
        </transition>
    </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService.js";
import RandomError from '../../components/RandomError.vue'
import LoadingSpinner from "../../components/LoadingSpinner.vue";

export default {
    name: 'LoginPage',
    components: {
        LoadingSpinner,
        RandomError
    },
    data() {
        return {
            username: '',
            password: '',
            errorMessage: '',
            error: false,
            isLoading: false,
        };
    },

    methods: {
        login() {
            this.isLoading = true;
            quizApiService.login(this.username, this.password)
                .then((response) => {
                    localStorage.setItem("token", response["data"]["token"])
                    this.$router.push('/admin-page')
                })
                .catch((err) => {
                    console.error('ERR:', err)
                    this.error = true
                    this.errorMessage = "Erreur d'authentification."
                })
                .finally(() => {
                    this.isLoading = false;
                }
                );
        },
        retryLogin() {
            this.error = false;
            this.errorMessage = "";
        }
    }
} 
</script>

<style>
.custom_logo_background {
    background-image: url('@/assets/logo_2.jpg');
    background-repeat: no-repeat;
    background-size: contain;
    background-position: initial;
}

.auth-transition-enter-active,
.auth-transition-leave-active {
    transition: opacity 1.25s, transform 1s;
}

auth-transition-enter-from,
.auth-transition-leave-to {
    opacity: 0;
    transform: translateY(-20px);
}
</style>