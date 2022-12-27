<template>
  <h2>Classement des meilleurs utilisateurs :</h2><br />
  <ul class="listgrp">

    <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
      <li class="affichageresult">{{ scoreEntry.playerName }} - {{ scoreEntry.score }}</li>
    </div>
  </ul>
  <br />
  <router-link to="/NewQuizPage">Démarrer le quiz !</router-link>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
export default {
  data() {
    return {
      registeredScores: []
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    try {
      const value = await quizApiService.getQuizInfo();
      var registered = value.data['scores'];
      this.registeredScores = registered;

    } catch (err) {
      console.log(err);
    }
  }
};

</script>
<style scoped>
.affichageresult {
  border-style: outset;
  border-color: rgb(121, 216, 216);
}

ul.listgrp {
  list-style-type: none;
  list-style: georgian inside url('src/assets/crown.png');
  overflow-y: scroll;
  height: 200px;
  width: 100%;
}
</style>