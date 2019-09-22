import React from 'react'
import { Typography, Grid } from '@material-ui/core'

export default function ClassificationSummary({ classifications }) {

    let [classificationName, classificationProbability] = classifications.reduce((a, b) => a[1] > b[1] ? a : b)
    console.log(classifications)
    return <Grid>
        <Typography variant="h5">{classificationName}</Typography>
    </Grid>

}