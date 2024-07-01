import { useState } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

const LoginModal = ({ show, handleClose, handleShowRegister }) => {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:5000/api/login', {
        email: formData.email,
        password: formData.password
      });

      if (response.status === 200) {
        alert('Logged in successfully!');
        handleClose();
      }
    } catch (error) {
      console.error('There was an error logging in!', error);
    }
  };

  if (!show) {
    return null;
  }

  return (
    <div className="modal" style={{ display: 'block' }}>
      <div className="modal-dialog">
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title">Log in</h5>
            <button type="button" className="close" onClick={handleClose}>
              <span>&times;</span>
            </button>
          </div>
          <div className="modal-body">
            <form onSubmit={handleSubmit}>
              <div className="form-group">
                <label htmlFor="email">Email</label>
                <input type="email" className="form-control" id="email" name="email" value={formData.email} onChange={handleChange} required />
              </div>
              <div className="form-group">
                <label htmlFor="password">Password</label>
                <input type="password" className="form-control" id="password" name="password" value={formData.password} onChange={handleChange} required />
              </div>
              <button type="submit" className="btn btn-primary">Log in</button>
            </form>
            <hr />
            <button className="btn btn-secondary" onClick={() => { handleClose(); handleShowRegister(); }}>Create Account</button>
            <button className="btn btn-link">Forgot Password?</button>
          </div>
        </div>
      </div>
    </div>
  );
};

LoginModal.propTypes = {
  show: PropTypes.bool.isRequired,
  handleClose: PropTypes.func.isRequired,
  handleShowRegister: PropTypes.func.isRequired
};

export default LoginModal;
