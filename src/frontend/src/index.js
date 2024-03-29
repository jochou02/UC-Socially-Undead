import React from 'react';
import ReactDOM from 'react-dom/client';
import './styles/index.css'

import reportWebVitals from './reportWebVitals';

import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Login from './pages/Login';
import Register from './pages/Register';
import Profile from './pages/Profile';
import ForgotPass from './pages/ForgotPass';
import Karma from './pages/Karma';
import PrefsQuiz from './pages/PrefsQuiz';
import Courses from './pages/Courses';
import Home from './pages/Home';
//import TestProfile from './pages/components/TestProfile';
import WaitTime from './buttons/WaitTime';
import Calendar from './pages/Calendar';
import OtherProfile from './pages/components/OtherProfile';
import Reviews from './pages/Reviews';

import Tutor from './pages/Tutor';


const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  //地図: Add new routes
  <BrowserRouter>
    <Routes>
      <Route path="" element={<Home />} />
      <Route path="home" element={<Home />} />
      <Route path="login" element={<Login />} />
      <Route path="register" element={<Register />} />
      <Route path="profile" element={<Profile />} />
      <Route path="courses" element={<Courses />} />
      <Route path="forgot_pass" element={<ForgotPass />} />
      <Route path="karma" element={<Karma />} />
      <Route path="user_prefs" element={<PrefsQuiz />} />
      <Route path='wait_time' element={<WaitTime />} />

      <Route path="calendar" element={<Calendar />} />

      <Route path="user/:userId" element={<OtherProfile />} />

      <Route path="user/:userId" element={<OtherProfile />} />

      <Route path="reviews/:courseDept/:courseNum" element={<Reviews />} />
        
      <Route path="tutoring" element={<Tutor />} />
    </Routes>
  </BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
