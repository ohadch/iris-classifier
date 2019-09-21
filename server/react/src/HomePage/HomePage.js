import React, { useState } from "react";
import { Link } from "react-router-dom";
import { connect } from "react-redux";

function HomePage({ user }) {
  const [images, setImages] = useState([]);

  const onDrop = acceptedFiles => {
    setImages(
      acceptedFiles.map(file =>
        Object.assign(file, {
          preview: URL.createObjectURL(file)
        })
      )
    );
  };

  return (
    <div className="col-md-6 col-md-offset-3">
      <h1>Hello, {user.username}!</h1>
      <p>You're logged in with React & JWT!!</p>
      <p>
        <Link to="/login">Logout</Link>
      </p>
    </div>
  );
}

function mapStateToProps(state) {
  const { users, authentication } = state;
  const { user } = authentication;
  return {
    user,
    users
  };
}

const connectedHomePage = connect(mapStateToProps)(HomePage);
export { connectedHomePage as HomePage };
