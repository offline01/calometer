import React, { useState, useEffect } from 'react';
import { BrowserRouter, Link, Switch, Route } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import {IconButton, InputAdornment, TextField} from "@material-ui/core";
import {Search} from "@material-ui/icons";
import HomePageView from "./components/pages/homePage";

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/api/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
    <div className="App">
      <HomePageView></HomePageView>
    </div>
  );
}

export default App;
