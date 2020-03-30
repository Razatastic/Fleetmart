import React from 'react';
import { Link } from 'react-router-dom';
// import SignedInLinks from './SignedInLinks';
// import SignedOutLinks from './SignedOutLinks';
import Button from '@material-ui/core/Button';

export default function Navbar() {
  return (
    <div>
      <Button variant="contained" color="primary">
        Hello World
      </Button>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/login">Login</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}
