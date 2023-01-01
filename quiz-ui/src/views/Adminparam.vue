<template>
  <div class="paddingright">
    <button type="button" class="btn btn-primary text-nowrap " @click="this.$router.push('/NewQuestion')">Ajouter une question</button><br />
    <button type="button" class="btn btn-primary text-nowrap " @click="this.$router.push('/Edit')">Modifier une question</button><br />
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
              <button type="button" class="btn btn-primary" @click="deleteQuestion">Delete</button><br />
            </div>
            <span style="color:green;" v-if="success1=='s'">Successfully deleted</span>
            <span style="color:red;" v-else-if="success1=='f'">Failed to delete</span>
          </form>
        </li>
      </ul>
    </div>
    <button type="button" class="btn btn-primary text-nowrap " @click="deleteAllQuestions">Supprimer toutes les
      questions</button><br />
      <span style="color:green;" v-if="success2=='s'">Successfully deleted</span>
  <span style="color:red;" v-else-if="success2=='f'">Failed to delete</span>
  </div>

  <button type="button" class="btn btn-primary text-nowrap " @click="deleteAllParticipations">Supprimer toutes les
    participations</button><br />
    <span style="color:green;" v-if="success3=='s'">Successfully deleted</span>
    <span style="color:red;" v-else-if="success3=='f'">Failed to delete</span>
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
      questionMod: '',
      success1:'',
      success2:'',
      success3:''
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
        if(typeof val=='undefined')
        {
          this.success1='f';
        }
        else
        {
          this.success1='s';
        }
       
      } catch (error) {
       
      }

    },
    async deleteAllQuestions() {
      try {
        var val = await quizApiService.deleteAllQuestions(participationStorageService.getToken());
        if(typeof val=='undefined')
        {
          this.success2='f';
        }
        else
        {
          this.success2='s';
        }
      } catch (error) {
        
      }

    },
    async deleteAllParticipations() {
      try {
        var val = await quizApiService.deleteAllParticipations(participationStorageService.getToken());
        if(typeof val=='undefined')
        {
          this.success3='f';
        }
        else
        {
          this.success3='s';
        }
      } catch (error) {
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
  