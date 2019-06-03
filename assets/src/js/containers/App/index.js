import React from 'react';
import Title from '../../components/Title';

class App extends React.Component {
  render () {
    const text = 'Maven Software Solutions';
    return (
      <Title text={text} />
    )
  }
}
export default App;