<template>
  <div class="midd">
    <form v-on:submit.prevent>
        <input v-model="title" type="text" class="form-control" placeholder="title" autocomplete="on" required><br />
        <input v-model="text" type="text" class="form-control" placeholder="text" autocomplete="on" required><br />
        <input v-model="pos" type="text" class="form-control" placeholder="position" autocomplete="on" required><br />
        
        <input v-model="answ1" type="text" class="form-control" placeholder="ans1" autocomplete="on" required>
        <div>
          <input :disabled="true2||true3|true4" v-model="true1" type="checkbox" id="horns" name="horns">
          <label for="horns">Istrue</label>
        </div>
        
        <input v-model="answ2" type="text" class="form-control" placeholder="ans2" autocomplete="on" required>
        <div>
          <input :disabled="true1||true3|true4" v-model="true2" type="checkbox" id="horns" name="horns">
          <label for="horns">Istrue</label>
        </div>
        
        <input v-model="answ3" type="text" class="form-control" placeholder="ans3" autocomplete="on" required>
        <div>
          <input :disabled="true2||true1|true4" v-model="true3" type="checkbox" id="horns" name="horns">
          <label for="horns">Istrue</label>
        </div>
        <input v-model="answ4" type="text" class="form-control" placeholder="ans4" autocomplete="on" required>
        <div>
          <input :disabled="true2||true3|true1" v-model="true4" type="checkbox" id="horns" name="horns">
          <label for="horns">Istrue</label>
        </div>
        <span v-if="!(true3||true2||true1||true4)" style="color:red;">One answer needs to be true</span><br/>
        <div v-if="image!==''">
          <img v-bind:src="image" style="width: 300px; height: 337px; object-fit: contain" >
        </div>
         <input v-on:change="changeImage()" type="file" id="myFile" name="filename" ref="myFile"><br/>
        <button type="submit" class="btn btn-primary" @click="postQuestion">Add</button><br />
    </form>
  </div>


</template>
<script>
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";
export default {
  data() {
      return {
      pos: '',
      title:'',
      text:'',
      image:'',
      answ1:'',
      answ2:'',
      answ3:'',
      answ4:'',
      true1:false,
      true2:false,
      true3:false,
      true4:false,
      };
  },
    async created() {
      try {

      } catch (err) {
      console.log(err);
      }
    },
methods: {
    async postQuestion() {
    try {
      if((this.true3||this.true2||this.true1||this.true4))
      {
        var val = await quizApiService.addQuestion( this.getQuestionJSON(), participationStorageService.getToken());
        console.log(val.data);
        this.$router.push("/Adminparam");
        
      }
    } catch (err) {
      console.log(err);
    }

  },
    getQuestionJSON()
    {
      var possibleAnswers=[];
      possibleAnswers.push({'text':this.answ1,'isCorrect':this.true1});
      possibleAnswers.push({'text':this.answ2,'isCorrect':this.true2});
      possibleAnswers.push({'text':this.answ3,'isCorrect':this.true3});
      possibleAnswers.push({'text':this.answ4,'isCorrect':this.true4});
      return {'position':this.pos,'image':this.image,'title':this.title,'text':this.text,'possibleAnswers':possibleAnswers};
    },
    changeImage()
    {
      var file = this.$refs.myFile.files[0];
      let reader=new FileReader();
      reader.addEventListener("load", () => {
      // on convertit l'image en une chaîne de caractères base64
      this.image = reader.result;
      }, false);
      if(file)
      {
        reader.readAsDataURL(file);
      }
    }

}
};

</script>

<style>
.midd{
margin-top: 10rem;
}
</style>