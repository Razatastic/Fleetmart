import React, { useEffect } from 'react';
import axios from 'axios';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';
import CategoryCard from '../components/layout/CategoryCard';
import groceryStore from '../assets/grocery-store.jpg';
import SearchbarCard from '../components/layout/SearchbarCard';

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
    paddingTop: 25
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary
  }
}));

export default function Home() {
  const classes = useStyles();

  useEffect(() => {
    axios.get(`http://127.0.0.1:5000/test_route`).then(res => {
      console.log(res);
    });
  });
  return (
    <Container maxWidth="md">
      <div className={classes.root}>
        <Grid container spacing={8}>
          <Grid item xs={12}>
            <SearchbarCard img={groceryStore} />
          </Grid>
          <Grid item xs={6}>
            <CategoryCard img={groceryStore} />
          </Grid>
          <Grid item xs={6}>
            <CategoryCard img={groceryStore} />
          </Grid>
        </Grid>
      </div>
    </Container>
  );
}
