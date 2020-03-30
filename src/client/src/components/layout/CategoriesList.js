import React, { useState, useEffect } from 'react';
import Grid from '@material-ui/core/Grid';
import CategoryCard from './CategoryCard';
import axios from 'axios';
import { Link } from 'react-router-dom';

export default function CategoriesList() {
  const [categoryList, setCategoryList] = useState([]);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:5000/categories`)
      .then(vals => vals.data)
      .then(data => setCategoryList(data));
  }, []);

  return (
    <>
      {categoryList.map(category => (
        <Grid item xs={6}>
          <Link
            // to={category.name.replace(/\\|\/|\s/g, '').toLowerCase()}
            to={`item:${category.id}`}
            style={{ textDecoration: 'none' }}
          >
            <CategoryCard
              id={category.id}
              name={category.name}
              img={category.image}
            />
          </Link>
        </Grid>
      ))}
    </>
  );
}
