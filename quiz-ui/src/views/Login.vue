<template>
  <div class="bg3"></div>
  <form v-on:submit.prevent class="form">
    <div class="form-group">
      <input v-model="password" type="password" class="form-control" id="password" placeholder="Enter password"
        autocomplete="on" @keydown.enter="login">
    </div>
    <div >
      <button type="button" class="btn btn-primary space" @click="login">Login</button><br />
      <p v-if="isWrong" style="color:red;">Mot de passe incorrect</p>
    </div>
  </form><br />
</template>
<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
export default {
  data() {
    return {
      password: '',
      isWrong: false
    };
  },
  async created() {
    console.log("Composant login created");
    if(participationStorageService.getToken()!=null)
    {
      this.$router.push('/Adminparam');
    }
    try {

    } catch (err) {
      console.log(err);
    }
  },
  methods: {
    async login() {
      try {
        var val = await quizApiService.postLogin({ 'password': this.password });
        if (val == null) {
          this.isWrong = true;
        }
        else {
          participationStorageService.saveToken(String(val.data['token']));
          console.log(participationStorageService.getToken());
          window.location.reload();
          
        }

      } catch (err) {
        console.log(err);
      }
    },
  }
};

</script>
<style scoped>
.space {
  padding-top: 1%;
}

.bg3 {
  background-image: url("@/assets/bg3.jpg");
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
