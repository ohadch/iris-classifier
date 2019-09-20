import React from "react";
import Typography from "@material-ui/core/Typography";
import { Card } from "@material-ui/core";

export default function ImageSummary({ image }) {
  console.log({ image });

  let reader;
  let imageComponent;
  if (image) {
    reader = new FileReader();
    reader.readAsDataURL(image);
    imageComponent = <img src={reader.resultl} alt="preview" />; // in constructor don't initilazie with array instaed with blank string
  }

  return (
    <Card style={{textAlign: 'center'}}>
      <Typography component="h5" variant="h5" align="center">
        { image.name }
      </Typography>

      {image ? imageComponent : ""}
    </Card>
  );
}
