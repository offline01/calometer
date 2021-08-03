import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import "./Signup.css";
import fetch from "isomorphic-fetch";

export default function Signup() {
    const [email, setEmail] = useState("");
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [firstname, setFirstname] = useState("");
    const [lastname, setLastname] = useState("");
    const [dob, setDob] = useState("");
    const [sex, setSex] = useState("");

    function validateForm() {
        return email.length > 0 && password.length > 0;
    }

    function handleSubmit(event) {
        event.preventDefault();
        const body = {
            email: email,
            user_name: username,
            pwd: password,
            f_name: firstname,
            l_name: lastname,
            dob: dob,
            sex: sex
        }
        console.log(body);
        const args = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body)
        }
        fetch('/api/user/register', args)
            .then(res => res.json())
            .then(str => console.log(str['status']))
    }

    return (
        <div className="Signup">
            <Form onSubmit={handleSubmit}>
                <Form.Group size="lg" controlId="email">
                    <Form.Label>Email</Form.Label>
                    <Form.Control
                        autoFocus
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                    />
                </Form.Group>
                <Form.Group size="lg" controlId="username">
                    <Form.Label>User Name</Form.Label>
                    <Form.Control
                        autoFocus
                        type="username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                </Form.Group>
                <Form.Group size="lg" controlId="password">
                    <Form.Label>Password</Form.Label>
                    <Form.Control
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </Form.Group>
                <Form.Group size="lg" controlId="firstname">
                    <Form.Label>First Name</Form.Label>
                    <Form.Control
                        autoFocus
                        type="firstname"
                        value={firstname}
                        onChange={(e) => setFirstname(e.target.value)}
                    />
                </Form.Group>
                <Form.Group size="lg" controlId="lastname">
                    <Form.Label>Last Name</Form.Label>
                    <Form.Control
                        autoFocus
                        type="lastname"
                        value={lastname}
                        onChange={(e) => setLastname(e.target.value)}
                    />
                </Form.Group>
                <Form.Group size="lg" controlId="dob">
                    <Form.Label>Date of Birth</Form.Label>
                    <Form.Control
                        autoFocus
                        type="dob"
                        value={dob}
                        onChange={(e) => setDob(e.target.value)}
                    />
                </Form.Group>
                <Form.Group size="lg" controlId="sex">
                    <Form.Label>Sex</Form.Label>
                    <Form.Control
                        autoFocus
                        type="sex"
                        value={sex}
                        onChange={(e) => setSex(e.target.value)}
                    />
                </Form.Group>

                <Button block size="lg" type="submit" disabled={!validateForm()}>
                    Sign Up
                </Button>
            </Form>
        </div>
    );
}