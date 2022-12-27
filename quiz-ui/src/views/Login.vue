<template>
  <form v-on:submit.prevent>
    <div class="form-group">
      <input v-model="password" type="password" class="form-control" id="password" placeholder="Enter password" autocomplete="on" @keydown.enter="login">
    </div>
    <div class="space">
      <button type="button" class="btn btn-primary" @click="login">Login</button><br/>
      <p v-if="isWrong" style="color:red;">Mot de passe incorrect</p>
    </div>
  </form><br/>
  </template>
  <script>
  import quizApiService from "@/services/QuizApiService";
  import participationStorageService from "@/services/ParticipationStorageService";
  export default {
    data() {
      return {
        password:'',
        isWrong:false
      };
    },
    async created() {
      console.log("Composant login created");
      try {
        
      } catch (err) {
        console.log(err);
      }
    },
    methods:{
      async login(){
        try
        {
          var val=await quizApiService.postLogin({'password':this.password});
          if(val==null)
          {
            this.isWrong=true;
          }
          else
          {
            participationStorageService.saveToken(String(val.data['token']));
            console.log(participationStorageService.getToken());
            this.$router.push('/Adminparam');
          }

        }catch(err){
          console.log(err);
        }
      },
    }
  };
  
  </script>
  <style scope>
  .space{
    padding-top: 5px;
  }
  </style>
  