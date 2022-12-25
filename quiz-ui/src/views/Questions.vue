<template>
<QuestionManager/>
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

</style>