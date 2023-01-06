<template>
  <div style="margin-top:10%">
    <h1>Résultats du participant {{ name }}<br />Score: {{ score }}</h1><br />

    <ul>
      <li v-for="question, index in questions" :key="question.position" :value="question.position"
        style="border-style: solid;border-color:black;margin-bottom:2%;">
        <p>{{ question.title }} </p><br />
        <p>{{ question.text }}</p><br />
        <img v-bind:src="question.image" style="width: 300px; height: 337px; object-fit: contain" /><br />
        <div v-for="answer, i in question.possibleAnswers" :key="answer.id">
          <p v-if="questionGoodAnswers[index].wasCorrect == true && i + 1 == questionGoodAnswers[index].correctAnswerPosition"
            class="good"> {{ answer.text }}<i class="bi bi-check" style="font-size:2em;color:green;"></i></p>
          <p v-else-if="i + 1 == answers[index]" class="bad"> {{ answer.text }} <i class="bi bi-x"
              style="font-size:2em;color:red;"></i></p>
          <p v-else>{{ answer.text }}</p><br />
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import participationstorageservice from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";
export default {
  data() {
    return {
      name: '',
      nbQuestions: 0,
      answers: [],
      score: '',
      questions: [],
      questionGoodAnswers: []
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    try {
      this.answers = participationstorageservice.getParticipationScore();
      this.name = participationstorageservice.getPlayerName();
      this.nbQuestions = this.answers.length;
      const value = await quizApiService.postAnswers({ 'playerName': this.name, "answers": this.answers });
      this.score = value.data['score'];
      this.questionGoodAnswers = value.data['answersSummaries'];
      this.listAllQuestions();
    } catch (err) {
      console.log(err);
    }
  },
  methods:
  {
    async listAllQuestions() {
      for (let i = 1; i <= this.nbQuestions; i++) {
        try {
          var val = await quizApiService.getQuestion(i);
          let question = { 'title': val.data['title'], 'text': val.data['text'], 'image': val.data['image'], 'possibleAnswers': val.data['possibleAnswers'], 'position': val.data['position'] };
          this.questions.push(question);
        } catch (err) {
          console.log(err);
        }

      }
    }
  }
};
</script>

<style scoped>
ul {
  list-style-type: none;
  height: 600px;
  width: 100%;
}

.good {
  border: 0.5rem solid;
  border-color: green;
}

.bad {
  border: 0.5rem solid;
  border-color: red;
}
</style>