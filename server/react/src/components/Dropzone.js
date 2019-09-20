import React from "react";
import ImageUploader from "react-images-upload";

export default class Dropzone extends React.Component {
  constructor(props) {
    super(props);
    this.state = { pictures: [] };
  }

  render() {
    return (
      <ImageUploader
        withIcon={true}
        buttonText="Choose images"
        onChange={this.props.onDrop}
        imgExtension={[".jpg", ".gif", ".png", ".gif"]}
        maxFileSize={5242880}
      />
    );
  }
}
