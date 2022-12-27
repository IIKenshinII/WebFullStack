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
                @keydown.enter="addQuestion"/>
            </div>
            <div class="space">
              <button type="button" class="btn btn-primary" @click="addQuestion">add</button><br />
              <p v-if="isWrong" style="color:red;">Mot de passe incorrect</p>
            </div>
          </form>
        </li>
      </ul>
    </div>
    <div class="btn-group dropdown">
      <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
        Modifier une question
      </button>
      <ul class="dropdown-menu">
        <li>
          <form v-on:submit.prevent>
            <div class="form-group">
              <input type="text" class="form-control" id="password" placeholder="Enter password" autocomplete="on"
                @keydown.enter="login">
            </div>
            <div class="space">
              <button type="button" class="btn btn-primary" @click="updateQuestion">Login</button><br />
              <p v-if="isWrong" style="color:red;">Mot de passe incorrect</p>
            </div>
          </form>
        </li>
      </ul>
    </div>
    <div class="btn-group dropdown">
      <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
        Supprimer une question
      </button>
      <ul class="dropdown-menu">
        <li>
          <form v-on:submit.prevent>
            <div class="form-group">
              <label>Id à supprimer</label>
              <input v-model="password" type="text" class="form-control" placeholder="id" autocomplete="on"
                @keydown.enter="deleteQuestion">
            </div>
            <div class="space">
              <button type="button" class="btn btn-primary" @click="deleteQuestion">Login</button><br />
              <p v-if="isWrong" style="color:red;">Mot de passe incorrect</p>
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
      question:''
    };
  },
  async created() {
    try {

    } catch (err) {
      console.log(err);
    }
  },
  methods: {
    async deleteQuestion(id) {
      try {
        var val = await quizApiService.deleteQuestion(id, participationStorageService.getToken());
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
  