import React from 'react';
import './styles/App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { Navbar } from './components/layout';
import { SignIn, SignUp } from './components/auth';
import { Home } from './pages';
import CssBaseline from '@material-ui/core/CssBaseline';

function App() {
  return (
    <>
      <CssBaseline />
      <Router>
        <div>
          <Navbar />

          {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
          <Switch>
            <Route exact path="/">
              <Home />
            </Route>
            <Route path="/signin">
              <SignIn />
            </Route>
            <Route path="/signup">
              <SignUp />
            </Route>
          </Switch>
        </div>
      </Router>
    </>
  );
}

export default App;
