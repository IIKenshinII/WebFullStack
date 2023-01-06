<template>
  <h1 class="cent2">Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1><br />
  <QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
</template>

<script>
import QuizApiService from "../services/QuizApiService";
import QuestionDisplay from "./QuestionDisplay.vue"
import participationStorageService from "@/services/ParticipationStorageService";
export default {
  components: { QuestionDisplay },
  data() {
    return { currentQuestion: { questionTitle: "", questionText: "", questionImage: "", possibleAnswers: [] }, currentQuestionPosition: 1, totalNumberOfQuestion: 0, Answers: [] };
  },
  async created() {
    console.log("Question manager");
    var value = await QuizApiService.getQuizInfo();
    this.totalNumberOfQuestion = value.data['size'];
    this.loadQuestionByPosition();
    try {
    }
    catch (err) {
      console.log(err);
    }
  },
  methods: {
    async answerClickedHandler(n) {
      this.currentQuestionPosition++;
      this.Answers.push(n);
      if (this.currentQuestionPosition > this.totalNumberOfQuestion) {
        this.endQuiz();
      }
      else {
        this.loadQuestionByPosition();
      }

      //console.log(this.Answers);
    },
    async loadQuestionByPosition() {
      var val2 = await QuizApiService.getQuestion(this.currentQuestionPosition);
      this.currentQuestion.questionTitle = val2.data['title'];
      this.currentQuestion.questionText = val2.data['text'];
      this.currentQuestion.questionImage = val2.data['image'];
      this.currentQuestion.possibleAnswers = val2.data['possibleAnswers'];
    },
    async endQuiz() {
      participationStorageService.saveParticipationScore(this.Answers);
      this.$router.push('/Result');
    }
  },
};

</script>

<style>
.cent2 {

  margin-left: 30%;
  margin-right: 30%;
  margin-top: 5%;
  margin-bottom: 1%;
  background-color: rgba(253, 253, 253, 0.788);

}
</style>