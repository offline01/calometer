import React from "react";
import {Search} from "@material-ui/icons";
import {IconButton} from "@material-ui/core";
import {searchFood} from "../../service/api-call";

class Searchbutton extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <IconButton onClick={searchFood}>
                <Search />
            </IconButton>
        )
    }
}