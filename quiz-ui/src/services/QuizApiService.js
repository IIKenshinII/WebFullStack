import axios from "axios";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
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
    return this.call("get", "quiz-info");
  },
  getQuestion(position) {
    // not implemented
    return this.call("get","questions?position="+position);
  },
  postAnswers(answers)
  {
    return this.call("post","participations",answers);
  },
  postLogin(login)
  {
    return this.call("post","login",login);
  },
  deleteAllQuestions(token)
  {
    return this.call("delete","questions/all",null,token);
  },
  deleteQuestion(id,token)
  {
    return this.call("delete","questions/"+id,null,token);
  },
  addQuestion(question,token)
  {
    return this.call("post","questions",question,token);
  },
  updateQuestion(id,question,token)
  {
    return this.call("put","questions/"+id,question,token);
  },
  deleteAllParticipations(token)
  {
    return this.call("delete","participations/all",null,token);
  }
  
};