import React, { useState, useEffect } from "react";
import { connect } from "react-redux";

import { Card, Grid, Box } from "@material-ui/core";
import classifyImage from "../api/classifyImage";
import ClassificationSummary from "./ClassificationSummary";
const img = {
  display: "block",
  width: "auto",
  height: "100%"
};

function ImageSummary({ file, user }) {
  const [classification, setClassification] = useState(null);

  useEffect(() => {
    async function fetchData() {
      const { classification: res } = await classifyImage(file, user.access_token);
      setClassification(res);
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
            <p>Classifying...</p>
          )}
        </Box>
      </Grid>
    </Card>
  );
}


function mapStateToProps(state) {
  const { authentication } = state;
  const { user } = authentication;
  debugger;
  return {
    user
  };
}

const connected = connect(mapStateToProps)(ImageSummary);
export default connected;