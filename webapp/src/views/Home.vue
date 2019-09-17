<template>
  <v-layout text-center align-center justify-center mt-2>
    <v-flex xs12 sm6 md6>
      <ImageUpload />
    </v-flex>
  </v-layout>
</template>

<script>
import ImageUpload from "@/components/ImageUpload";
export default {
  components: {
    ImageUpload
  }
};
</script>
