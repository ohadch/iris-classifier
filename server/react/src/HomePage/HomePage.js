import React, { useState } from "react";
import { connect } from "react-redux";
import { Grid } from '@material-ui/core';
import Dropzone from './../components/Dropzone';
import UploadedImages from './../components/UploadedImages';

function HomePage({ user }) {
  const [images, setImages] = useState([]);

  const onDrop = acceptedFiles => {
    setImages(
      [...images, ...acceptedFiles.map(file =>
        Object.assign(file, {
          preview: URL.createObjectURL(file)
        })
      )]
    );
  };

  return (
    <Grid>
      <Grid>
        <Dropzone onDrop={onDrop} />
        <UploadedImages images={images} />
      </Grid>
    </Grid>
  );
}

function mapStateToProps(state) {}

const connectedHomePage = connect(mapStateToProps)(HomePage);
export { connectedHomePage as HomePage };
