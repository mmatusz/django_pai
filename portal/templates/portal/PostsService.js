"use strict";
import axios from 'axios';
const URI = "http://localhost:8000/api/v1/";

export default {
    getAllPosts() {
        return axios.get(URI + "post/");
    },
}