export function convertPrice(price, currency) {
    if (currency === "inr") {
        return "₹" + (75 * price).toFixed(2);
    } else if (currency === "euro") {
        return "€" + (1.16 * price).toFixed(2);
    } else if (currency === "aud") {
        return "$" + (1.34 * price).toFixed(2);
    } else if (currency === "yuan") {
        return "¥" + (6.40 * price).toFixed(2);
    } else if (currency === "yen") {
        return "¥" + (114.21 * price).toFixed(2);
    } else if (currency === "pound") {
        return "£" + (0.74 * price).toFixed(2);
    }
    return "$" + price.toFixed(2);
}