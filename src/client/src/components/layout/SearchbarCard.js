import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import '../../styles/Typewriter.css';
import Typist from 'react-typist';

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
      <CardMedia
        className={classes.media}
        style={{}}
        image={img}
        title="Grocery Store"
      >
        <Container className={classes.container}>
          <Typography variant="h3" style={{ color: 'white' }}>
            <Typist>
              Your one stop shop for produce.
              <Typist.Backspace count={8} delay={1000} />
              <span>beverages.</span>
              <Typist.Backspace count={10} delay={1000} />
              <span>ice cream.</span>
              <Typist.Backspace count={10} delay={1000} />
              <span>everything.</span>
              {/* <Typist.Backspace
                count={34}
                delay={1000}
                cursor={{ hideWhenDone: true }}
              />
              <span>Welcome to Fleetmart</span> */}
            </Typist>
          </Typography>
        </Container>
      </CardMedia>
    </Card>
  );
}
