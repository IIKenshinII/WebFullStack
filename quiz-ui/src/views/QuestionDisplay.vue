<template>
  <div class="cent">
    <p>{{ question.questionTitle }}</p><br />
    <p>{{ question.questionText }}</p><br />
    <img v-bind:src="question.questionImage" style="width: 300px; height: 337px; object-fit: contain" /><br />
    <div v-for="answer, index in question.possibleAnswers">
      <a class="p-3 mb-2 text-dark border border-dark te" @click="$emit('click-on-answer', index + 1)">{{
        answer.text
      }}</a>
    </div>
  </div>


</template>

<script>
export default {
  props: { question: { type: Object } },
  emits: ["click-on-answer"],
  async created() {
    console.log("Composant Question display");
    try {
    } catch (err) {
      console.log(err);
    }
  }
};

</script>

<style >
a {
  cursor: pointer;
}


.cent {

  margin-left: 30%;
  margin-right: 30%;
  margin-top: 1%;
  margin-bottom: 10%;
  background-color: rgba(253, 253, 253, 0.788);

}

.te {
  display: inline-block;
  width: 500px;
}

.border:hover {
  background-color: rgb(75, 230, 44);
}
</style>