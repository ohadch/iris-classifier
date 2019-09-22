import React from "react";
import Grid from "@material-ui/core/Grid";
import ImageSummary from "./ImageSummary";

const thumbsContainer = {
  display: "flex",
  flexDirection: "row",
  justifyContent: "space-between",
  flexWrap: "wrap",
  marginTop: 16
};


export default function UploadedImages({ images }) {
  const thumbs = images.map(file => (
    <ImageSummary style={{marginBottom: "5px"}} file={file} />
  ));

  return (
    <Grid>
      <aside style={thumbsContainer}>{thumbs}</aside>
    </Grid>
  );
}
