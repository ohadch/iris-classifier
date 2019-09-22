<template>
  <v-form @submit.prevent="handleTrainSubmit">
    <v-card>
      <v-card-title>Train Youer Model</v-card-title>
      <v-card-text>
        <v-text-field label="C Parameter" />
      </v-card-text>
      <v-card-actions>
        <v-btn type="submit">Train</v-btn>
        <p v-if="accuracy">Accuracy: {{ accuracy }}</p>
      </v-card-actions>
    </v-card>
  </v-form>
</template>

<script>
// import trainModel from "@/api/trainModel"
export default {
  name: "ModelTraining",
  data() {
    return {
      accuracy: null
    };
  },
  methods: {
    handleTrainSubmit() {
      this.accuracy = "0.98";
    }
  }
};
</script>