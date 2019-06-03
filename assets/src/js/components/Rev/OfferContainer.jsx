import React from 'react';
import FinanceOfferItem from "./FinanceOfferItem.jsx";
import TrimImage from "./TrimImage.jsx";
import SavingsOfferItem from "./SavingsOfferItem.jsx";
import LeaseOfferItem from "./LeaseOfferItem.jsx";

function OfferContainer(props) {
    return (
        <div>
            <React.Fragment>
                <TrimImage trim={props.trim}
                           index={props.index}
                />
                <FinanceOfferItem trim={props.trim}
                                  index={props.index}
                                  handleCheckChange={props.handleCheckChange}
                                  checked={props.checked}
                />
                <SavingsOfferItem trim={props.trim}
                                  index={props.index}
                                  handleCheckChange={props.handleCheckChange}
                                  checked={props.checked}
                />
                <LeaseOfferItem trim={props.trim}
                                index={props.index}
                                handleCheckChange={props.handleCheckChange}
                                checked={props.checked}
                />

            </React.Fragment>
        </div>
    )
}

export default OfferContainer;