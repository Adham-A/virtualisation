import axios from 'axios';

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true,
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      'Content-Type': 'application/json',
    };
    if (token != null) {
      headers.authorization = `Bearer ${token}`;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },
  getQuizInfo() {
    return this.call('get', `quiz-info`);
  },
  // Read questions by pos
  getQuestion(position) {
    return this.call('get', `questions?position=${position}`);
  },
  // Read questions by id
  getQuestionById(id) {
    return this.call('get', `questions?id=${id}`);
  },

  postAnswer(playerName, answers) {
    return this.call('post', `participations`, { playerName: playerName, answers: answers });
  },

  login(username, password) {
    return this.call('post', `admin/login`, {username : username, password: password});
  },

  deleteAll() {
    console.log(localStorage.getItem("token"))
    return this.call('delete', `questions/all`, null, localStorage.getItem("token"))
  }
  // Add new questions
  // postNewQuestion(question) {

  // },
  // Delete questions

  // Update questions

  // Manage questions order

  // Retrieve scores
};
