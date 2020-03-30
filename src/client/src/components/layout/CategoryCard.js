import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';

const useStyles = makeStyles({
  // root: {
  //   maxWidth: 345
  // },
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
  const { img } = props;
  const classes = useStyles();

  return (
    <Card className={classes.root}>
      <CardMedia className={classes.media} image={img} title="Grocery Store">
        <Container className={classes.container}>
          <Typography variant="h2" style={{ color: 'white' }}>
            h2. Heading
          </Typography>
        </Container>
      </CardMedia>
    </Card>
  );
}
