import React from 'react';

function TrimImage(props) {
    return (
        <div>
            <img src={props.trim[props.index].imgurl} className="trim-image"/>
        </div>
    )
}

export default TrimImage;