<template>
    <v-card>
        <v-card-title>
            {{title}}
        </v-card-title>
        <v-card-text>
            {{body}}
        </v-card-text>
    </v-card>    
</template>

<script>
export default {
    name: "ClassificationSummary",
    props: {
        classification: Object
    },
    computed: {
        title() {
            return this.classification ? "Your flower is probably..." : "Oops :("
        },
        body() {
            let [name, probability] = this.mostProbableClassification;
            return `${name.endsWith("s") ? '' : 'A'} ${name}! (${probability * 100}%)`
        },
        mostProbableClassification() {
            return Object.entries(this.classification).reduce((a, b) => a[1] > b[1] ? a : b)
        }
    }
}
</script>