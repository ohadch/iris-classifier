import React, { useEffect, useState } from "react";
import { useDropzone } from "react-dropzone";
import { Card } from "@material-ui/core";

export default function Dropzone({ onDrop }) {
  const [files, setFiles] = useState([]);

  const { getRootProps, getInputProps } = useDropzone({
    accept: "image/*",
    onDrop
  });

  useEffect(
    () => () => {
      // Make sure to revoke the data uris to avoid memory leaks
      files.forEach(file => URL.revokeObjectURL(file.preview));
    },
    [files]
  );

  return (
    <section className="container" style={{ textAlign: "center" }}>
      <Card style={{ marginTop: "10px" }}>
        <div {...getRootProps({ className: "dropzone" })}>
          <input {...getInputProps()} />
          <p>Drag 'n' drop some files here, or click to select files</p>
        </div>
      </Card>
    </section>
  );
}
