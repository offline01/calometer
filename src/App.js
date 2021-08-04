import React from 'react';
import { BrowserRouter, Link, Switch, Route } from 'react-router-dom';
// import './App.css';
import HomePageView from "./components/pages/homePage";
import Login from "./components/pages/loginPage";
import Signup from "./components/pages/signUp";
import Resetpassword from "./components/pages/passwordReset";
import Deleteuser from "./components/pages/deleteUser";

function App() {
  return (
      <div className="App">
        <BrowserRouter>
          <div>
            <Link className="App-link" to="/">Home</Link>
            &nbsp;|&nbsp;
            <Link className="App-link" to="/login">Login</Link>
              &nbsp;|&nbsp;
            <Link className="App-link" to="/signup">Sign Up</Link>
            &nbsp;|&nbsp;
            <Link className="App-link" to="/resetpassword">Reset Password</Link>
            &nbsp;|&nbsp;
            <Link className="App-link" to="/accountdeletion">Delete Account</Link>
          </div>
          <Switch>
            <Route exact path="/" component={HomePageView}></Route>
            <Route path="/login" component={Login}></Route>
            <Route path="/signup" component={Signup}></Route>
            <Route path="/resetpassword" component={Resetpassword}></Route>
            <Route path="/accountdeletion" component={Deleteuser}></Route>
          </Switch>
        </BrowserRouter>
      </div>
  );
}

export default App;
