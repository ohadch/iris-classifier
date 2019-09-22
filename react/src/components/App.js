import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { connect } from "react-redux";

import { history } from "../helpers";
import { userActions } from "../actions";
import { PrivateRoute } from "../components";
import { HomePage } from "../HomePage";
import { LoginPage } from "../LoginPage";
import IconButton from '@material-ui/core/IconButton';
import { makeStyles } from "@material-ui/core/styles";
import CssBaseline from "@material-ui/core/CssBaseline";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import { Button } from "@material-ui/core";

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
    color: "white"
  },
  title: {
    flexGrow: 1,
  },
}));

function App({ user }) {
  const classes = useStyles();

  const logout = () => {
    userActions.logout();
    /* eslint-disable */
    location.reload();
  }

  return (
    <React.Fragment>
      <Router history={history}>
        <CssBaseline />
        <div className={classes.root}>
          <AppBar position="static">
            <Toolbar>
              <IconButton
                edge="start"
                className={classes.menuButton}
                color="inherit"
                aria-label="menu"
              >
                {/* <MenuIcon /> */}
              </IconButton>
              <Typography variant="h6" className={classes.title}>
                Iris Classifier
              </Typography>
              {user ? <Button className={classes.menuButton} onClick={logout}>Logout</Button> : ''}
            </Toolbar>
          </AppBar>
        </div>
        <main className={classes.layout}>
          <div style={{padding: "10px"}}>
            <PrivateRoute exact path="/" component={HomePage} />
            <Route path="/login" component={LoginPage} />
          </div>
        </main>
      </Router>
    </React.Fragment>
  );
}

function mapStateToProps(state) {
  const { alert, authentication } = state;
  const { user } = authentication;
  return {
    alert,
    user
  };
}

const connectedApp = connect(mapStateToProps)(App);
export { connectedApp as App };
