import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const UserPosts = () => {
  const { username } = useParams();
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get(`http://localhost:5000/api/users/${username}/posts`)
      .then(response => {
        setPosts(response.data);
      })
      .catch(error => console.error('Error fetching user posts:', error));
  }, [username]);

  return (
    <div>
      <h1>Posts by {username}</h1>
      {posts.map(post => (
        <div key={post.id} className="post">
          <h2>{post.title}</h2>
          <p>{post.content}</p>
          <small>{new Date(post.date_posted).toLocaleDateString()}</small>
        </div>
      ))}
    </div>
  );
};

export default UserPosts;
