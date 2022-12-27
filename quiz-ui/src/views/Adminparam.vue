<template>
  <div class="paddingright">
    <div class="btn-group dropdown">
      <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-auto-close="false"
        data-bs-toggle="dropdown" aria-expanded="false">
        Ajouter une question
      </button>
      <ul class="dropdown-menu">
        <li>
          <form v-on:submit.prevent>
            <div class="form-group">
              <label>Question en JSON:</label>
              <textarea v-model="question" type="text" class="form-control" placeholder="question" autocomplete="on"
                @keydown.enter="addQuestion"></textarea>
            </div>
            <div class="space">
              <button type="button" class="btn btn-primary" @click="addQuestion">add</button><br />
            </div>
          </form>
        </li>
      </ul>
    </div>
    <div class="btn-group dropdown">
      <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false"
        data-bs-auto-close="false">
        Modifier une question
      </button>
      <ul class="dropdown-menu">
        <li>
          <form v-on:submit.prevent>
            <div class="form-group">
              <input v-model="idMod" type="text" class="form-control" placeholder="Enter id to modify" autocomplete="on"
                @keydown.enter="login">
            </div>
            <div class="space">
              <button type="button" class="btn btn-primary" @click="getQuestion">send</button><br />
              <textarea v-model="questionMod" type="text" class="form-control" placeholder="question"
                autocomplete="on"></textarea>
              <button type="button" class="btn btn-primary" @click="modifyQuestion">modify</button><br />
            </div>
          </form>
        </li>
      </ul>
    </div>
    <div class="btn-group dropdown">
      <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false"
        data-bs-auto-close="false">
        Supprimer une question
      </button>
      <ul class="dropdown-menu">
        <li>
          <form v-on:submit.prevent>
            <div class="form-group">
              <label>Id à supprimer</label>
              <input v-model="idDelete" type="text" class="form-control" placeholder="id" autocomplete="on"
                @keydown.enter="deleteQuestion">
            </div>
            <div class="space">
              <button type="button" class="btn btn-primary" @click="deleteQuestion">Login</button><br />
            </div>
          </form>
        </li>
      </ul>
    </div>
    <button type="button" class="btn btn-primary text-nowrap " @click="deleteAllQuestions">Supprimer toutes les
      questions</button><br />
  </div>
  <button type="button" class="btn btn-primary text-nowrap " @click="deleteAllParticipations">Supprimer toutes les
    participations</button><br />
</template>
<script>
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";
export default {
  data() {
    return {
      question: '',
      idDelete: '',
      idMod: '',
      questionMod: ''
    };
  },
  async created() {
    try {
    } catch (err) {
      console.log(err);
    }
  },
  methods: {
    async deleteQuestion() {
      try {
        var val = await quizApiService.deleteQuestion(this.idDelete, participationStorageService.getToken());
      } catch (error) {

      }

    },
    async deleteAllQuestions() {
      try {
        var val = await quizApiService.deleteAllQuestions(participationStorageService.getToken());
      } catch (error) {

      }

    },
    async deleteAllParticipations() {
      try {
        var val = await quizApiService.deleteAllParticipations(participationStorageService.getToken());
      } catch (error) {

      }

    },
    async addQuestion() {
      try {

        var val = await quizApiService.addQuestion(JSON.parse(this.question), participationStorageService.getToken());
      } catch (err) {
        console.log(err)
      }

    },
    async getQuestion() {
      try {
        var val = await quizApiService.getQuestionid(this.idMod);
        this.questionMod = JSON.stringify(val.data);
      } catch (err) {
        console.log(err)
      }
    },
    async modifyQuestion() {
      try {
        console.log(this.questionMod);
        var val = await quizApiService.updateQuestion(this.idMod, JSON.parse(this.questionMod), participationStorageService.getToken());
      } catch (err) {
        console.log(err)
      }

    }

  }
};

</script>
<style scope>
.paddingright {
  display: flex;
  justify-content: space-between;
  column-gap: 50px;
}

textarea {
  width: 300px;
  height: 300px;
}
</style>
  