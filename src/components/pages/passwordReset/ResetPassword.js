import React from 'react'
import { createTheme } from '@material-ui/core/styles'
import Typography from '@material-ui/core/Typography'

import FormPasswordReset from './FormPasswordReset'
import './styles.css'
import {ThemeProvider} from "react-bootstrap";
import {CssBaseline} from "@material-ui/core";

const theme = createTheme({
    palette: {
        type: 'dark',
    },
})

export class ResetPassword extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <ThemeProvider theme={theme}>
                <CssBaseline>
                    <div className="ResetPassword">
                        <Typography variant="title" style={{ margin: '16px 0' }}>
                            Password Reset
                        </Typography>
                        <FormPasswordReset />
                    </div>
                </CssBaseline>
            </ThemeProvider>
        )
    }
}
