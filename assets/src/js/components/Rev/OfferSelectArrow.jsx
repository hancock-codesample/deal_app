import React from 'react';

const OfferSelectArrow = ({direction, clickFunction}) => {
    return (
        <button onClick={clickFunction} type="button" className="btn btn-primary">
            Click
        </button>
    );
};

export default OfferSelectArrow;