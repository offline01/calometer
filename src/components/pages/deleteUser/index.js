import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import "./Deleteuser.css";
import fetch from "isomorphic-fetch";

export default function Deleteuser() {
    const [email, setEmail] = useState("");
    const [pwd, setPwd] = useState("");

    function validateForm() {
        return email.length > 0 && pwd.length > 0;
    }

    function handleSubmit(event) {
        event.preventDefault();
        const body = {
            email: email,
        }
        console.log(body);
        const args = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body)
        }
        fetch('/api/user/delete_user', args)
            .then(res => res.json())
            .then(str => console.log(str['status']))
    }

    return (
        <div className="Deleteuser">
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
                <Form.Group size="lg" controlId="pwd">
                    <Form.Label>Password</Form.Label>
                    <Form.Control
                        type="pwd"
                        value={pwd}
                        onChange={(e) => setPwd(e.target.value)}
                    />
                </Form.Group>


                <Button block size="lg" type="submit" disabled={!validateForm()}>
                    Please delete my account
                </Button>
            </Form>
        </div>
    );
}