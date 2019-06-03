import React from 'react';
import Checkbox from "./Checkbox.jsx";

function SavingsOfferItem(props) {
    if (props.trim[props.index].offers.savings == null) {
        return null;
    }
    const nameKey = props.trim[props.index].name + ' savings';
    return (
        <div className="row">
            <div>
                <Checkbox
                    onChange={props.handleCheckChange}
                    checked={props.checked.get((nameKey))}
                    name={props.trim[props.index].name + ' savings'}
                />
            </div>
            <div>
                <p>Savings</p>
            </div>
            <div>
                <p className="detail">Up To</p>
                <p><sup>$</sup>{props.trim[props.index].offers.savings}</p>
                <p className="detail">Total Savings</p>
            </div>
        </div>
    )
}

export default SavingsOfferItem;