import React from "react";
import Grid from "@material-ui/core/Grid";
import ImageSummary from "./ImageSummary";

const thumbsContainer = {
  display: "flex",
  flexDirection: "row",
  flexWrap: "wrap",
  marginTop: 16
};


export default function UploadedImages({ images }) {
  const thumbs = images.map(file => (
    <ImageSummary file={file} />
  ));

  return (
    <Grid>
      <aside style={thumbsContainer}>{thumbs}</aside>
    </Grid>
  );
}
