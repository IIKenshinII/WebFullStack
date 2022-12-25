<template>
  <p>{{ question.questionTitle }}</p><br />
  <p>{{ question.questionText }}</p><br />
  <div v-for="answer, index in question.possibleAnswers">
    <a @click="$emit('click-on-answer', index + 1)">{{ answer.text }}</a><br />
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

<style scoped>
a {
  cursor: pointer;
}
</style>