import React, { useEffect } from 'react';
import axios from 'axios';

export default function Home() {
  useEffect(() => {
    axios.get(`http://127.0.0.1:5000/test_route`).then(res => {
      console.log(res);
    });
  });
  return (
    <div>
      <h1>home</h1>
    </div>
  );
}
