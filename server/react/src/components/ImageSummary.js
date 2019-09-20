import React, { useState } from "react";
import { Card, Grid } from "@material-ui/core";
import classifyImage from "../api/classifyImage";

const img = {
  display: "block",
  width: "auto",
  height: "100%"
};

export default function ImageSummary({ file }) {
  const [classification, setClassification] = useState(null);

  classifyImage(file).then(res => setClassification(res));

  return (
    <Card key={file.name}>
      <Grid>
        <img src={file.preview} style={img} alt="preview" />
        <div>{classification || <p>Loading...</p>}</div>
      </Grid>
    </Card>
  );
}
