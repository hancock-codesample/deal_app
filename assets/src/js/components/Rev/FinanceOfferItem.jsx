import React from 'react';
import Checkbox from "./Checkbox.jsx";

function FinanceOfferItem(props) {
    if (props.trim[props.index].offers.finance == null) {
        return null;
    }
   const nameKey = props.trim[props.index].name + ' finance';
    return (
        <div className="row">
            <div>
                <Checkbox
                    onChange={props.handleCheckChange}
                    checked={props.checked.get((nameKey))}
                    name={props.trim[props.index].name + ' finance'}
                />
            </div>
            <div>
                <p className="detail">Up To</p>
                <p><sup>$</sup>{props.trim[props.index].offers.finance}</p>
                <p className="detail">APR financing for up to 60 months PLUS $2000 Off</p>
            </div>
        </div>
    )
}

export default FinanceOfferItem;