import React, { Component } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import "./Signup.css";


class App extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        email: '',
        username: '',
        password: '',
        firstname: '',
        lastname: '',
        dateofbirth: '',
        sex: ''
      }
    }
  
    render() {
      return(
        <div className="App">
          <form id="contact-form" onSubmit={this.handleSubmit.bind(this)} method="POST">
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input type="email" className="form-control" value={this.state.email} onChange={this.onMessageChange.bind(this)} />
            </div>
            <div className="form-group">
              <label htmlFor="username">User name</label>
              <input type="text" className="form-control" aria-describedby="emailHelp" value={this.state.username} onChange={this.onMessageChange.bind(this)} />
            </div>
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <textarea className="form-control" rows="5" value={this.state.password} onChange={this.onMessageChange.bind(this)} />
            </div>
            <div className="form-group">
              <label htmlFor="firstname">First name</label>
              <textarea className="form-control" rows="5" value={this.state.firstname} onChange={this.onMessageChange.bind(this)} />
            </div>
            <div className="form-group">
              <label htmlFor="lastname">Last name</label>
              <textarea className="form-control" rows="5" value={this.state.lastname} onChange={this.onMessageChange.bind(this)} />
            </div>
            <div className="form-group">
              <label htmlFor="dateofbirth">Date of birth</label>
              <textarea className="form-control" rows="5" value={this.state.dateofbirth} onChange={this.onMessageChange.bind(this)} />
            </div>
            <div className="form-group">
              <label htmlFor="sex">Sex</label>
              <textarea className="form-control" rows="5" value={this.state.sex} onChange={this.onMessageChange.bind(this)} />
            </div>
            <button type="submit" className="btn btn-primary btn-block">Sign Up</button>
                <p className="forgot-password text-right">
                    Already registered <a href="#">sign in?</a>
                </p>
          </form>
        </div>
      );
    }
  
    onMessageChange(event) {
      this.setState({email: event.target.value})
    }
  
    onMessageChange(event) {
      this.setState({username: event.target.value})
    }
  
    onMessageChange(event) {
        this.setState({password: event.target.value})
    }

    onMessageChange(event) {
      this.setState({firstname: event.target.value})
    }

    onMessageChange(event) {
        this.setState({lastname: event.target.value})
    }
    onMessageChange(event) {
      this.setState({dateofbirth: event.target.value})
    }
    onMessageChange(event) {
        this.setState({sex: event.target.value})
    }
    handleSubmit(event) {
    }
  }
  
  export default App;