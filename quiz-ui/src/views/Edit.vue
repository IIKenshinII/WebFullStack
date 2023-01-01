<template>
        <div class="midd">
          <form v-on:submit.prevent>
              <input v-model="id" type="text" class="form-control" placeholder="Enter id to edit" autocomplete="on"><br />
              <button type="button" class="btn btn-primary" @click="getQuestion">Send</button><br /><br />
              <input v-model="title" type="text" class="form-control" placeholder="title" autocomplete="on"><br />
              <input v-model="text" type="text" class="form-control" placeholder="text" autocomplete="on"><br />
              <input v-model="pos" type="text" class="form-control" placeholder="position" autocomplete="on"><br />
              
              <input v-model="answ1" type="text" class="form-control" placeholder="ans1" autocomplete="on">
              <div>
                <input :disabled="true2||true3|true4" v-model="true1" type="checkbox" id="horns" name="horns">
                <label for="horns">Istrue</label>
              </div>
              
              <input v-model="answ2" type="text" class="form-control" placeholder="ans2" autocomplete="on">
              <div>
                <input :disabled="true1||true3|true4" v-model="true2" type="checkbox" id="horns" name="horns">
                <label for="horns">Istrue</label>
              </div>
              
              <input v-model="answ3" type="text" class="form-control" placeholder="ans3" autocomplete="on">
              <div>
                <input :disabled="true2||true1|true4" v-model="true3" type="checkbox" id="horns" name="horns">
                <label for="horns">Istrue</label>
              </div>
              <input v-model="answ4" type="text" class="form-control" placeholder="ans4" autocomplete="on">
              <div>
                <input :disabled="true2||true3|true1" v-model="true4" type="checkbox" id="horns" name="horns">
                <label for="horns">Istrue</label>
              </div>
              <span v-if="!(true3||true2||true1||true4)" style="color:red;">One answer needs to be true</span><br/>
              <img v-bind:src="image" style="width: 300px; height: 337px; object-fit: contain" > <input v-on:change="changeImage()" type="file" id="myFile" name="filename" ref="myFile"><br/>
              <button type="button" class="btn btn-primary" @click="modifyQuestion">Edit</button><br />
          </form>
        </div>


</template>
<script>
import participationStorageService from "@/services/ParticipationStorageService";
import quizApiService from "@/services/QuizApiService";
export default {
  data() {
    return {
      id:'',
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
    async getQuestion() {
      try {
        var val = await quizApiService.getQuestionid(this.id);
        this.pos=val.data['position'];
        this.image=val.data['image'];
        this.text=val.data['text'];
        this.title=val.data['title'];
        this.answ1=val.data['possibleAnswers'][0]['text'];
        this.true1=val.data['possibleAnswers'][0]['isCorrect'];
        this.answ2=val.data['possibleAnswers'][1]['text'];
        this.true2=val.data['possibleAnswers'][1]['isCorrect'];
        this.answ3=val.data['possibleAnswers'][2]['text'];
        this.true3=val.data['possibleAnswers'][2]['isCorrect'];
        this.answ4=val.data['possibleAnswers'][3]['text'];
        this.true4=val.data['possibleAnswers'][3]['isCorrect'];
      } catch (err) {
        console.log(err);
      }
    },
    async modifyQuestion() {
      try {
        var val = await quizApiService.updateQuestion(this.id, this.getQuestionJSON(), participationStorageService.getToken());
        this.$router.push("/Adminparam");
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