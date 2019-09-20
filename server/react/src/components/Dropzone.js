import React from "react";
import ImageUploader from "react-images-upload";

export default function Dropzone({onDrop}) {
    return (
      <ImageUploader
        withIcon={true}
        buttonText="Choose images"
        onChange={onDrop}
        imgExtension={[".jpg", ".gif", ".png", ".gif"]}
        maxFileSize={5242880}
      />
    );
}
