function add(p1, p2) {
    return p1 + p2;
}

function parse_str_to_int(variable) {
    return parseInt(variable)
}

function formatting_price(price) {
    if (!parseInt(price)) {
        return "";
    }
    if (price > 999999) {
        let priceString = (price / 100).toFixed(2).replace('.', ',');
        let priceArray = priceString.split("").reverse();
        let index = 3
        while (priceArray.length > index + 3) {
            priceArray.splice( index + 3, 0, " ");
            index += 4;
        }
        return priceArray.reverse().join("") + " $";
    } else {
        console.log('in else')
        return ( price / 100).toFixed(2).replace('.',',') + " $";
    }
}
// for node import functions = require('./functions')
module.exports = { add, parse_str_to_int, formatting_price};
