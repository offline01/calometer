import {Button, Grid, IconButton, InputAdornment, TextField, Typography} from '@material-ui/core'
import {Search} from "@material-ui/icons";
import React from "react";
import fetch from "isomorphic-fetch";

class HomePageView extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            foods: [],
            name: undefined,
            c_low: -1,
            c_high: -1,
            p_low: -1,
            p_high: -1,
            f_low: -1,
            f_high: -1,
            ch_low: -1,
            ch_high: -1
        }
        this.searchFood = this.searchFood.bind(this);
        this.handelSearchBoxChange = this.handelSearchBoxChange.bind(this);
    }

    searchFood() {
        const body = {
            name: this.state.name,
            c_low: this.state.c_low,
            c_high: this.state.c_high,
            p_low: this.state.p_low,
            p_high: this.state.p_low,
            f_low: this.state.f_low,
            f_high: this.state.f_high,
            ch_low: this.state.ch_low,
            ch_high: this.state.ch_low
        }
        const args = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body)
        }
        console.log(args)
        fetch('/api/food_search', args)
            .then(res => res.json())
            .then(jsonStr => this.setState({foods: jsonStr['foods']}))

        // dummy code below -> wait for backend API to be finished
        // this.setState({foodName: "suibian"})
    }

    handelSearchBoxChange(e) {
        this.setState({
            name: e.target.value
        })
        // console.log(this.state.name) //test
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
                                    <IconButton onClick={this.searchFood}>
                                        <Search />
                                    </IconButton>
                                </InputAdornment>}}
                        onChange={this.handelSearchBoxChange}
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
                <div className="SearchResult" style={{ padding: 20 }}>
                    {this.state.foods === [] ?
                        <div></div> : <Typography variant="subtitle1">{this.state.foods.map(food => <div>{food['food name']}</div>)}</Typography>}
                </div>
            </div>
        )
    }
}

export default HomePageView;