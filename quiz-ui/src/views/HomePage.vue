<template>
  <div class="bg2"></div>
  <h2 style="font: italic small-caps bold 16px/2 cursive; color:blue">Classement des meilleurs utilisateurs :</h2><br />
  <ul class="listgrp">

    <div v-for="scoreEntry, index in registeredScores" v-bind:key="scoreEntry.date">
      <li class="affichageresult" v-if="index == 0"
        style="background-color: black;color:gold;  filter: invert(69%) sepia(99%) saturate(693%) hue-rotate(360deg) brightness(107%) contrast(104%);">
        {{ scoreEntry.playerName }} - {{ scoreEntry.score }}</li>

      <li class="affichageresult" v-else-if="index == 1"
        style="color:silver; background-color: black; filter: invert(89%) sepia(4%) saturate(34%) hue-rotate(322deg) brightness(92%) contrast(78%);">
        {{ scoreEntry.playerName }} - {{ scoreEntry.score }}</li>
      <li class="affichageresult" v-else-if="index == 2"
        style="color:#796221; background-color: black; filter: invert(31%) sepia(95%) saturate(421%) hue-rotate(355deg) brightness(91%) contrast(96%);">
        {{ scoreEntry.playerName }} - {{ scoreEntry.score }}</li>
      <li class="affichageresult" v-else style="color:#796221; background-color: ">
        {{ scoreEntry.playerName }} - {{ scoreEntry.score }}</li>
    </div>
  </ul>
  <br />
  <Router-link style="font: italic small-caps bold 16px/2 cursive; color:blue" to="/NewQuizPage">Démarrer le quiz
    !</Router-link>
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
  border-color: rgb(17, 17, 17);
  background-color: rgb(233, 233, 233);
}

ul.listgrp {
  list-style-type: none;
  list-style: decimal inside url("@/assets/crown.png");
  overflow-y: scroll;
  height: 200px;
  width: 100%;
}

.bg2 {
  background-image: url("@/assets/bg2.jpg");
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  overflow: auto;
  align-items: center;
  text-align: center;

}
</style>