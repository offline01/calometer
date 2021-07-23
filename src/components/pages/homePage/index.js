import {Button, Grid, IconButton, InputAdornment, TextField, Typography} from '@material-ui/core'
import {Search} from "@material-ui/icons";
import React from "react";

class HomePageView extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className="HomePage">
                <div className="Header" style={{ padding: 20 }}>
                    <Grid container
                          spacing={1}
                          direction="row"
                          justifyContent="flex-start"
                          alignItems="center">
                        <Grid item>
                            <Typography variant="subtitle1">Do you want to eat smarter and workout smarter?</Typography>
                        </Grid>
                        <Grid item>
                            <Button variant="contained">Start for free</Button>
                        </Grid>
                        <Grid item>
                            <Button variant="contained">login</Button>
                        </Grid>
                    </Grid>
                </div>
                <div className="SearchBox">
                    <TextField
                        id="standard-full-width"
                        style={{ margin: 8 }}
                        placeholder="Input the food name you want to search"
                        fullWidth
                        InputProps={{endAdornment:
                                <InputAdornment>
                                    <IconButton onClick={() => { console.log('clicked') }}>
                                        <Search />
                                    </IconButton>
                                </InputAdornment>}}
                    ></TextField>
                </div>
                <div className="Filters">
                    <Grid container spacing={3}>
                        <Grid item xs={4}
                              justifyContent="flex-start"
                              alignItems="center">
                            <Typography variant="subtitle1">Calorie</Typography>
                            <TextField required id="standard-required" label="Minimum" defaultValue="0" />
                            <TextField required id="standard-required" label="Maximum" defaultValue="0" />
                        </Grid>
                        <Grid item xs={4}
                              justifyContent="flex-start"
                              alignItems="center">
                            <Typography variant="subtitle1">Protein</Typography>
                            <TextField required id="standard-required" label="Minimum" defaultValue="0" />
                            <TextField required id="standard-required" label="Maximum" defaultValue="0" />
                        </Grid>
                        <Grid item xs={4}
                              justifyContent="flex-start"
                              alignItems="center">
                            <Typography variant="subtitle1">Fat</Typography>
                            <TextField required id="standard-required" label="Minimum" defaultValue="0" />
                            <TextField required id="standard-required" label="Maximum" defaultValue="0" />
                        </Grid>
                    </Grid>
                </div>
            </div>
        )
    }
}

export default HomePageView;