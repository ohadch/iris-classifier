import React, { useState, useEffect } from "react";
import { Card, Grid, Box } from "@material-ui/core";
import classifyImage from "../api/classifyImage";
import ClassificationSummary from "./ClassificationSummary";
const img = {
  display: "block",
  width: "auto",
  height: "100%"
};

export default function ImageSummary({ file }) {
  const [classification, setClassification] = useState(null);

  useEffect(() => {
    async function fetchData() {
      const { classification: res } = await classifyImage(file);
      setClassification(Object.entries(res));
    }

    fetchData();
  }, []);

  return (
    <Card key={file.name}>
      <Grid>
        <img src={file.preview} style={img} alt="preview" />
        <Box style={{ textAlign: "center" }}>
          {classification ? (
            <ClassificationSummary classifications={classification} />
          ) : (
            <p>Loading...</p>
          )}
        </Box>
      </Grid>
    </Card>
  );
}
