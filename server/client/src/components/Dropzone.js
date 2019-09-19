import React, { useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import { useDropzone } from "react-dropzone";
import Paper from "@material-ui/core/Paper";
import Typography from "@material-ui/core/Typography";
import Grid from "@material-ui/core/Grid";
import UploadedImages from './UploadedImages';

const useStyles = makeStyles(theme => ({
  paper: {
    textAlign: "center",
    marginTop: theme.spacing(3),
    marginBottom: theme.spacing(3),
    padding: theme.spacing(2),
    [theme.breakpoints.up(600 + theme.spacing(3) * 2)]: {
      marginTop: theme.spacing(6),
      marginBottom: theme.spacing(6),
      padding: theme.spacing(3)
    }
  },
  stepper: {
    padding: theme.spacing(3, 0, 5)
  }
}));

export default function Dropzone() {
  const classes = useStyles();

  const [files, setFiles] = useState([]);

  /* eslint-disable */
  const onDrop = acceptedFiles => {
    let allFiles = [...files, acceptedFiles];
    console.log({ allFiles });
    setFiles(allFiles);
  };

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  return (
    <div {...getRootProps()}>
      <Paper className={classes.paper}>
        <Typography component="h1" variant="h4" align="center">
          Classify Your Flower
        </Typography>

        {files.length ? (
          <Grid>
            <UploadedImages images={files}/>
          </Grid>
        ) : (
          <Grid>
            <input {...getInputProps()} />
            {isDragActive ? (
              <p>Drop the files here ...</p>
            ) : (
              <p>Drag 'n' drop some files here, or click to select files</p>
            )}
          </Grid>
        )}
      

      </Paper>
    </div>
  );
}
