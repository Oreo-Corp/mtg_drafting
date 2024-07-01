import { useEffect } from 'react';
import axios from 'axios';

const Home = () => {
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/test');
        console.log(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="container">
      <h1>Welcome to MTG Draft</h1>
      <p>Create and join drafts for your favorite Magic: The Gathering sets.</p>
    </div>
  );
};

export default Home;
