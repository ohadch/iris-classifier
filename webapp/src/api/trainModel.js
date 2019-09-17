import axios from "axios";

/**
 * Trains the Iris classification model and returns its accuracy.
 * @param {*} param0 
 */
export default async function trainModel({ C }) {
    const { accuracy } = await axios.post("api/train", { C })
    return accuracy;
}