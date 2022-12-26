<template>
<form>
  <div class="form-group">
    <label >Saisissez votre nom :</label>
    <input v-model="username" type="text" class="form-control" id="username" placeholder="Username">
  </div>
  <div class="space">
    <button type="button" class="btn btn-primary" @click="launchNewQuiz">Submit</button>
  </div>
</form><br/>
</template>
<script>
import participationStorageService from "@/services/ParticipationStorageService";
export default {
  data() {
    return {
      username:''
    };
  },
  async created() {
    console.log("Composant New quiz page 'created'");
    try {
      
    } catch (err) {
      console.log(err);
    }
  },
  methods:{
    launchNewQuiz(){
      console.log("Launch new quiz with", this.username);
      participationStorageService.savePlayerName(this.username);
      this.$router.push('/Questions');
    },
  }
};

</script>
<style scope>
.space{
  padding-top: 5px;
}
</style>
