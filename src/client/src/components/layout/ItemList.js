import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import { useParams } from 'react-router-dom';
import ItemListElement from './ItemListElement';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles(theme => ({
  root: {
    width: '100%',
    backgroundColor: theme.palette.background.paper
  }
}));

export default function ItemList() {
  const classes = useStyles();
  let { id } = useParams();

  return (
    <Container>
      <Typography
        variant="h3"
        gutterBottom
        style={{ margin: 20, marginLeft: 0 }}
      >
        Items
      </Typography>
      <List className={classes.root}>
        <ItemListElement />
        <ItemListElement />
        <ItemListElement />
      </List>
    </Container>
  );
}
