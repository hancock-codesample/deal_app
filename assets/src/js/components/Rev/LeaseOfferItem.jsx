import React from 'react';
import Checkbox from "./Checkbox.jsx";

function LeaseOfferItem(props) {
    if (props.trim[props.index].offers.lease == null) {
        return null;
    }
    const nameKey = props.trim[props.index].name + ' lease';
    return (
        <div className="row">
            <div>
                <Checkbox
                    onChange={props.handleCheckChange}
                    checked={props.checked.get((nameKey))}
                    name={props.trim[props.index].name + ' lease'}
                />
            </div>
            <div>
                <p><sup>$</sup>{props.trim[props.index].offers.lease}</p>
                <p className="detail">per month for 36 months with $2199 due at signing</p>
            </div>
        </div>
    )
}

export default LeaseOfferItem;