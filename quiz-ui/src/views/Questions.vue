<template>
    <div class="bg"><QuestionManager /> </div>
         
</template>

<script>
import QuestionManager from './QuestionManager.vue';
export default {
    data() {
        return {};
    },
    async created() {
        console.log("Composant Question");
        try {
        }
        catch (err) {
            console.log(err);
        }
    },
    components: { QuestionManager }
};

</script>
<style >
.bg{
  background-image: url("@/assets/bg.jpg");
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
