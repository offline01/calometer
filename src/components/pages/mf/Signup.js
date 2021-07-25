import React, { Component } from "react";

export class SignUp extends Component {
    render() {
        return (
            <form>
                <h3>Sign Up</h3>
                <div className="form-group">
                    <label>Email</label>
                    <input type="text" className="form-control" placeholder="Email" />
                </div>
                <div className="form-group">
                    <label>User name</label>
                    <input type="text" className="form-control" placeholder="User name" />
                </div>
                <div className="form-group">
                    <label>Password</label>
                    <input type="text" className="form-control" placeholder="Password" />
                </div>
                <div className="form-group">
                    <label>First name</label>
                    <input type="text" className="form-control" placeholder="First name" />
                </div>

                <div className="form-group">
                    <label>Last name</label>
                    <input type="text" className="form-control" placeholder="Last name" />
                </div>

                <div className="form-group">
                    <label>date of birth</label>
                    <input type="text" className="form-control" placeholder="date of birth" />
                </div>

                <div className="form-group">
                    <label>Sex</label>
                    <input type="text" className="form-control" placeholder="Sex" />
                </div>

                <button type="submit" className="btn btn-primary btn-block">Sign Up</button>
                <p className="forgot-password text-right">
                    Already registered <a href="#">sign in?</a>
                </p>
            </form>
        );
    }
}