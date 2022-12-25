<template>
  <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1><br/>
<QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
</template>

<script>
import QuizApiService from "../services/QuizApiService";
import QuestionDisplay from "./QuestionDisplay.vue"
export default{
  components: { QuestionDisplay },
  data(){
    return {currentQuestion:{questionTitle:"",questionText:"",questionImage:"",possibleAnswers:[]},currentQuestionPosition:1,totalNumberOfQuestion:'',Answers:[]};
  },
  async created() {
        console.log("Question manager");
        var value= await QuizApiService.getQuizInfo();
        this.totalNumberOfQuestion=value.data['size'];
        var val2=await QuizApiService.getQuestion(this.currentQuestionPosition);
        this.currentQuestion.questionTitle=val2.data['title'];
        this.currentQuestion.questionText=val2.data['text'];
        this.currentQuestion.questionImage=val2.data['image'];
        this.currentQuestion.possibleAnswers=val2.data['possibleAnswers'];
        console.log(this.currentQuestion);
        try {
        }
        catch (err) {
            console.log(err);
        }
    },
    methods:{
        async answerClickedHandler(n)
      {
          this.currentQuestionPosition++;
          this.Answers.push(n);
          var val2=await QuizApiService.getQuestion(this.currentQuestionPosition);
          this.currentQuestion.questionTitle=val2.data['title'];
          this.currentQuestion.questionText=val2.data['text'];
          this.currentQuestion.questionImage=val2.data['image'];
          this.currentQuestion.possibleAnswers=val2.data['possibleAnswers'];
          console.log(this.Answers);
      },
      async loadQuestionByPosition()
      {

      },
      async endQuiz()
      {

      }
    },
};
    
</script>