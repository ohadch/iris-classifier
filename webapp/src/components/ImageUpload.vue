<template>
  <v-layout column>
    <v-flex>
      <h1>{{ msg }}</h1>
    </v-flex>

    <v-flex v-if="uploading">Uploading...</v-flex>

    <v-flex v-if="classification">
      <ClassificationSummary :classification="classification" />
    </v-flex>

    <v-flex>
      <v-card>
        <div class="my-8">
          <image-uploader
            :preview="true"
            :className="['fileinput', { 'fileinput--loaded': hasImage }]"
            capture="environment"
            :debug="1"
            doNotResize="gif"
            :autoRotate="true"
            outputFormat="file"
            @input="setImage"
          >
            <label for="fileInput" slot="upload-label">
              <figure>
                <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                  <path
                    class="path1"
                    d="M9.5 19c0 3.59 2.91 6.5 6.5 6.5s6.5-2.91 6.5-6.5-2.91-6.5-6.5-6.5-6.5 2.91-6.5 6.5zM30 8h-7c-0.5-2-1-4-3-4h-8c-2 0-2.5 2-3 4h-7c-1.1 0-2 0.9-2 2v18c0 1.1 0.9 2 2 2h28c1.1 0 2-0.9 2-2v-18c0-1.1-0.9-2-2-2zM16 27.875c-4.902 0-8.875-3.973-8.875-8.875s3.973-8.875 8.875-8.875c4.902 0 8.875 3.973 8.875 8.875s-3.973 8.875-8.875 8.875zM30 14h-4v-2h4v2z"
                  />
                </svg>
              </figure>
              <span class="upload-caption">
                {{
                hasImage ? "Replace" : "Click to upload"
                }}
              </span>
            </label>
          </image-uploader>
        </div>
      </v-card>
    </v-flex>
    <v-flex></v-flex>
  </v-layout>
</template>

<script>
import classifyImage from "@/api/classifyImage";
import ClassificationSummary from "@/components/ClassificationSummary";

export default {
  name: "ImageUpload",
  components: {
    ClassificationSummary
  },
  data() {
    return {
      msg: "Upload Your Flower Image",
      hasImage: false,
      image: null,
      uploading: false,
      classification: null
    };
  },
  methods: {
    setImage(output) {
      this.hasImage = true;
      this.image = output;
      console.log(this.image);
      this.uploadImage();
    },
    async uploadImage() {
      this.uploading = true;

      // Uploads the image and classifies it
      let { classification } = await classifyImage(this.image);
      this.classification = classification;

      this.uploading = false;
    }
  }
};
</script>

<style>
#fileInput {
  display: none;
}
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.my-8 {
  margin-top: 4rem;
  margin-bottom: 4rem;
}
</style>
