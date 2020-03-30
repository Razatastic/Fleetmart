import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';

const useStyles = makeStyles({
  media: {
    height: 200
  },
  container: {
    height: '100%',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center'
  }
});

export default function CategoryCard(props) {
  const { id, name, img } = props;
  const classes = useStyles();

  return (
    <Card key={id} className={classes.root}>
      <CardMedia className={classes.media} image={img} title="Grocery Store">
        <Container className={classes.container}>
          <Typography variant="h4" style={{ color: 'white' }}>
            {name}
          </Typography>
        </Container>
      </CardMedia>
    </Card>
  );
}
