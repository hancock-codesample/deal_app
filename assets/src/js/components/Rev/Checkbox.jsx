import React from 'react';
import styled from 'styled-components';

const CheckboxContainer = styled.div`
  display: inline-block;
  vertical-align: middle;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  border: 1px solid #479df9;
  margin: 1px;
  position: relative;
  vertical-align: center;
`;

const Icon = styled.svg`
  fill: none;
  stroke: #fff;
  stroke-width: 2px;
  position: absolute;
  top: 50%;
  left: 50%;
`;
// Hide checkbox visually but remain accessible to screen readers.
// Source: https://polished.js.org/docs/#hidevisually
const HiddenCheckbox = styled.input.attrs({type: 'checkbox'})`
  border: 0;
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  white-space: nowrap;
  width: 1px;
`;

const StyledCheckbox = styled.div`
  display: inline-block;
  width: 100%;
  height: 100%;
  background: ${props => (props.checked ? '#479df9' : 'white')};
  border-radius: 50%;
  transition: all 150ms;
  position: absolute;
  top: 0px;
  left: 0px;
  



  ${Icon} {
    visibility: ${props => (props.checked ? 'visible' : 'hidden')}
  }
`;

const Checkbox = ({className, checked = false, value, ...props}) => (
    <label>
        <CheckboxContainer className={className}>
            <HiddenCheckbox checked={checked} {...props} />
            <StyledCheckbox checked={checked}>
                <Icon viewBox="0 0 40 40">
                    <polyline points="20 6 9 17 4 12"/>
                </Icon>
            </StyledCheckbox>
        </CheckboxContainer>
    </label>
);

export default Checkbox;
