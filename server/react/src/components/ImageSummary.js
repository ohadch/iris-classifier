import React from "react";
import Typography from "@material-ui/core/Typography";
import { Card } from "@material-ui/core";

export default function ImageSummary({ image }) {
  console.log({ image });

  let reader;
  let imageComponent;
  if (image) {
    reader = new FileReader();
    reader.readAsDataURL(new Blob(image));
    imageComponent = <img src={reader.resultl} alt="preview" />; // in constructor don't initilazie with array instaed with blank string
  }

  return (
    <Card style={{textAlign: 'center'}}>
      <Typography component="h3" variant="h4" align="center">
        Image Summary
      </Typography>

      {image ? imageComponent : ""}
    </Card>
  );
}
