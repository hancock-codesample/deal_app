import React from 'react';
import OfferSwitcher from './OfferSwitcher.jsx';
import Step2 from './Step2.jsx';
import Step3 from './Step3.jsx';

class RevMaster extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            currentStep: 1,
            email: '',
            firstName: '',
            lastName: '',
            checkedItems: new Map(),
        };
        this.handleCheckChange = this.handleCheckChange.bind(this);
    }

    handleCheckChange(e) {
        const item = e.target.name;
        const isChecked = e.target.checked;
        this.setState(prevState => ({checkedItems: prevState.checkedItems.set(item, isChecked)}));
    }

    handleChange = event => {
        const {name, value} = event.target;
        this.setState({
            [name]: value
        })
    };

    handleSubmit = event => {
        event.preventDefault();
        const {email, firstName, lastName} = this.state;
        alert(`Your registration detail: \n 
           Email: ${email} \n 
           firstName: ${firstName} \n
           lastName: ${lastName}`)
    };

    _next = () => {
        let currentStep = this.state.currentStep;
        currentStep = currentStep >= 2 ? 3 : currentStep + 1;
        this.setState({
            currentStep: currentStep
        })
    };

    _prev = () => {
        let currentStep = this.state.currentStep;
        currentStep = currentStep <= 1 ? 1 : currentStep - 1;
        this.setState({
            currentStep: currentStep
        })
    };

    /*
    * the functions for our button
    */
    previousButton() {
        let currentStep = this.state.currentStep;
        if (currentStep !== 1) {
            return (
                <button
                    className="btn btn-secondary"
                    type="button" onClick={this._prev}>
                    Previous
                </button>
            )
        }
        return null;
    }

    nextButton() {
        let currentStep = this.state.currentStep;
        if (currentStep < 3) {
            return (
                <button
                    className="btn btn-primary float-right"
                    type="button" onClick={this._next}>
                    Next
                </button>
            )
        }
        return null;
    }

    render() {
        return (
            <div className="hi">
                <React.Fragment>

                    <form onSubmit={this.handleSubmit}>
                        {/*
        render the form steps and pass required props in
      */}
                        <OfferSwitcher
                            currentStep={this.state.currentStep}
                            data={this.props.data}
                            handleCheckChange={this.handleCheckChange}
                            checked={this.state.checkedItems}

                        />
                        <Step2
                            currentStep={this.state.currentStep}
                            handleChange={this.handleChange}
                        />
                        <Step3
                            currentStep={this.state.currentStep}
                            handleChange={this.handleChange}
                        />
                        {this.previousButton()}
                        {this.nextButton()}

                    </form>
                </React.Fragment>
            </div>
        );
    }
}

export default RevMaster;