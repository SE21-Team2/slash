import React from "react";

const CurrencySelect = ({ currency, setCurrency }) => (
    <div className="option">
        <h4>Currency:</h4>
        <select value={currency} onChange={e => setCurrency(e.target.value)}>
            <option value="usd">US Dollar</option>
            <option value="inr">Indian Rupee</option>
            <option value="euro">Euro</option>
            <option value="aud">Australian Dollar</option>
            <option value="yuan">Yuan</option>
            <option value="yen">Yen</option>
            <option value="pound">British Pound</option>
        </select>
    </div>
);

export default CurrencySelect;