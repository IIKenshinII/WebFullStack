<template>
    <div >
      <div class="paddingright">
    <button type="button" class="btn btn-primary text-nowrap " @click="this.$router.push('/NewQuestion')">Ajouter une question</button><br />
   
    <button type="button" class="btn btn-primary text-nowrap " @click="deleteAllQuestions">Supprimer toutes les
      questions</button><br />
      <span style="color:green;" v-if="success2=='s'">Successfully deleted</span>
  <span style="color:red;" v-else-if="success2=='f'">Failed to delete</span>
  <button type="button" class="btn btn-primary text-nowrap " @click="deleteAllParticipations">Supprimer toutes les
    participations</button><br />
    <span style="color:green;" v-if="success3=='s'">Successfully deleted<br/></span>
    <span style="color:red;" v-else-if="success3=='f'">Failed to delete<br/></span>
    <button type="button" class="btn btn-primary text-nowrap " style="color:red;background-color:paleturquoise;" @click="logout"><i class="bi bi-box-arrow-right"></i> Logout</button><br />
    </div><br/>
      <ul >
        <li v-for="question,index in questions" :key="question.position" :value="question.position" >
        <p>Question {{ index+1 }} :<a @click="send(index)">{{ question['text'] }}</a></p><br />
      </li>
      </ul>
    </div>

    

</template>
<script>
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";
export default {
  data() {
    return {
      success2:'',
      success3:'',
      size:0,
      questions:[]
    };
  },
  async created() {
    try {
      var value = await quizApiService.getQuizInfo();
      this.size = value.data['size'];
      this.listAllQuestions();
      console.log(this.questions)
      
    } catch (err) {
      console.log(err);
    }
  },
  methods: {
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

    },
      async listAllQuestions()
      {
          for(let i=1;i<=this.size;i++)
          {
            try{
              var val = await quizApiService.getQuestion(i);
              var question={'title': val.data['title'] , 'text':val.data['text'], 'image': val.data['image'], 'possibleAnswers':val.data['possibleAnswers'],'position':val.data['position'],'id':val.data['id']};
              this.questions.push(question);
            }catch(err){
              console.log(err);
            }

          }
      },
      send(index)
      {
        var q=this.questions[index];
        var id=q['id']
        this.$router.push({ name: 'ManageQuestion', params: {id:JSON.stringify(id)}})
      },
      logout()
      {
        participationStorageService.clear();
        this.$router.push('/Login')
      }
  }
};

</script>
<style scoped>
.paddingright {
  display: flex;
  justify-content: space-between;
  column-gap: 50px;
  height: auto;
}
ul {
  list-style-type: none;
  height: 600px;
  width: 100%;
}
a {
  cursor: pointer;
}
</style>
  