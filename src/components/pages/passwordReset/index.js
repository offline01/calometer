import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import "./Resetpassword.css";
import fetch from "isomorphic-fetch";

export default function Resetpassword() {
    const [email, setEmail] = useState("");
    const [old_pwd, setOldpwd] = useState("");
    const [new_pwd, setNewpwd] = useState("");

    function validateForm() {
        return email.length > 0 && new_pwd.length > 0;
    }

    function handleSubmit(event) {
        event.preventDefault();
        const body = {
            email: email,
            old_pwd: old_pwd,
            new_pwd: new_pwd
        }
        console.log(body);
        const args = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body)
        }
        fetch('/api/user/change_password', args)
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
                <Form.Group size="lg" controlId="old_pwd">
                    <Form.Label>Old Password</Form.Label>
                    <Form.Control
                        type="old_pwd"
                        value={old_pwd}
                        onChange={(e) => setOldpwd(e.target.value)}
                    />
                </Form.Group>
                <Form.Group size="lg" controlId="new_pwd">
                    <Form.Label>New Password</Form.Label>
                    <Form.Control
                        type="new_pwd"
                        value={new_pwd}
                        onChange={(e) => setNewpwd(e.target.value)}
                    />
                </Form.Group>

                <Button block size="lg" type="submit" disabled={!validateForm()}>
                    Reset Password
                </Button>
            </Form>
        </div>
    );
}