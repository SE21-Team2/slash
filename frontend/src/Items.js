import React from "react";

import "./Items.css";

const Items = ({ items }) => (
    <table id="item-table">
        <tr>
            <th>Name</th>
            <th>Price</th>
            <th>Link</th>
            <th>Website</th>
            <th>Rating</th>
        </tr>
        {items.map(item => <Item key={item.link} item={item} />)}
    </table>
);

const Item = ({ item }) => (
    <tr>
        <td>{item.name}</td>
        <td>{item.price}</td>
        <td><a href={item.link}>{item.link}</a></td>
        <td>{item.website}</td>
        <td>{item.rating}</td>
    </tr>
);

export default Items;
