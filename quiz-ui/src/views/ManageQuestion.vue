<template>
  <p>{{ title }}</p><br />
  <p>{{ text }}</p><br />
  <img v-bind:src="image" style="width: 300px; height: 337px; object-fit: contain" /><br />
  <div v-for="answer, index in possibleAnswers">
    <p>{{ answer.text }}</p><br />
  </div>
  <div class="gap">
    <button type="button" class="btn btn-primary text-nowrap " @click="deleteQuestion">Supprimer</button><br />
    <button type="button" class="btn btn-primary text-nowrap " @click="send">Editer</button><br />
    <button type="button" class="btn btn-primary" @click="this.$router.push('/Adminparam')">Annuler</button><br />
    <span style="color:green;" v-if="success1 == 's'">Successfully deleted</span>
    <span style="color:red;" v-else-if="success1 == 'f'">Failed to delete</span>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from "@/services/ParticipationStorageService";
export default {
  props: ['id'],
  data() {
    return {
      success1: '',
      title: '',
      text: '',
      possibleAnswers: [],
      image: '',

    };
  },
  async created() {
    var val = await quizApiService.getQuestionid(this.id);
    this.title = val.data['title'];
    this.text = val.data['text'];
    this.image = val.data['image'];
    this.possibleAnswers = val.data['possibleAnswers'];
    try {
    } catch (err) {
      console.log(err);
    }
  },
  methods: {
    async deleteQuestion() {
      try {
        var val = await quizApiService.deleteQuestion(this.id, participationStorageService.getToken());
        console.log(val)
        if (typeof val == 'undefined') {
          this.success1 = 'f';
        }
        else {
          this.success1 = 's';
          this.$router.push('/Adminparam');
        }

      } catch (error) {
        console.log(error);
      }

    },
    send() {
      this.$router.push({ name: 'Edit', params: { id: this.id } })
    }
  }

};

</script>

<style scoped>
.gap {
  column-gap: 20px;
  justify-content: space-between;
  display: flex;
}
</style>