import React, { useState } from "react";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";

export default function ImageSummary() {
  const [classification] = useState(null);

  return (
    <Grid>
      <Typography component="h3" variant="h4" align="center">
        Image Summary
      </Typography>

      {classification ? <Grid>Classification</Grid> : ""}
    </Grid>
  );
}
