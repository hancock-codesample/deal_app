import React from "react";
import OfferSelectArrow from "./OfferSelectArrow.jsx"
import OfferContainer from "./OfferContainer.jsx";

class OfferSwitcher extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            currentTrimIndex: 0
        };

        this.nextOffer = this.nextOffer.bind(this);
        this.previousOffer = this.previousOffer.bind(this);
    }

    previousOffer() {
        const lastIndex = this.props.data.trim.length - 1;
        const {currentTrimIndex} = this.state;
        const shouldResetIndex = currentTrimIndex === 0;
        const index = shouldResetIndex ? lastIndex : currentTrimIndex - 1;

        this.setState({
            currentTrimIndex: index
        });
    }

    nextOffer() {
        const lastIndex = this.props.data.trim.length - 1;
        const {currentTrimIndex} = this.state;
        const shouldResetIndex = currentTrimIndex === lastIndex;
        const index = shouldResetIndex ? 0 : currentTrimIndex + 1;

        this.setState({
            currentTrimIndex: index
        });
    }


    render() {
        if (this.props.currentStep !== 1) {
            return null
        } else {
            return (

                <div className="form-group">
                    <div>
                        <h2>PICK YOUR<br/>{this.props.data.vehicle} OFFER</h2>
                        <div className="row">
                            <div>
                                <OfferSelectArrow direction="left"
                                                  clickFunction={this.previousOffer}
                                                  glyph="&#9664;"
                                />
                            </div>
                            <div>

                                <OfferContainer index={this.state.currentTrimIndex}
                                                trim={this.props.data.trim}
                                                handleCheckChange={this.props.handleCheckChange}
                                                checked={this.props.checked}
                                />
                            </div>
                            <div>

                                <OfferSelectArrow direction="right"
                                                  clickFunction={this.nextOffer}
                                                  glyph="&#9654;"
                                />
                            </div>
                        </div>
                    </div>

                </div>
            );
        }
    }
}

export default OfferSwitcher;