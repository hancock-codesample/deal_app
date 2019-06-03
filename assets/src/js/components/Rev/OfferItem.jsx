import React from 'react';

function OfferItem(props) {
    return (
        <div>
            <img src={props.data[props.index.currentTrimIndex].imgurl} width="100%"/>
            <p>{props.data[props.index.currentTrimIndex].name}</p>
            <p>{props.data[props.index.currentTrimIndex].msrp}</p>

        </div>
    );
}

export default OfferItem;