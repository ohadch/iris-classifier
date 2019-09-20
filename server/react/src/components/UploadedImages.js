import React from "react";
import Grid from "@material-ui/core/Grid";
import ImageSummary from "./ImageSummary";

export default function UploadedImages({ images }) {
  return (
    <Grid>
      {images.map((image, i) => (
        <ImageSummary key={i} image={image}></ImageSummary>
      ))}
    </Grid>
  );
}
