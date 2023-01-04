<template>
  <div class="bg"></div>
  <form class="form">
    <div class="form-group" >
      <label style="font: italic small-caps bold 16px/2 cursive; color:red">Saisissez votre nom :</label>
      <input v-model="username" type="text" class="form-control" id="username" placeholder="Username"
        @keydown.enter="launchNewQuiz">
    </div>
    <div class="space">
      <button type="button" class="btn btn-primary" @click="launchNewQuiz">Submit</button>
    </div>
  </form><br />
</template>
<script>
import participationStorageService from "@/services/ParticipationStorageService";
export default {
  data() {
    return {
      username: ''
    };
  },
  async created() {

    try {

    } catch (err) {
      console.log(err);
    }
  },
  methods: {
    launchNewQuiz() {
      console.log("Launch new quiz with", this.username);
      participationStorageService.savePlayerName(this.username);
      this.$router.push('/Questions');
    },
  }
};

</script>
<style scope>
.space {
  margin-top: 10%;
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
}

.form{
  margin:auto;
  background-color:rgba(253, 253, 253, 0.788);
  text-align: center;
}
</style>
