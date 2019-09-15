import React, { Component } from 'react'

class Counter extends Component {
  // YOUR CODE GOES BELOW
  constructor(props){
  	super(props);
  	this.state = {
  		counter: 0
  	};

  }

  increment = () => {
  	this.setState((state) => {
    	return {counter: state.counter + 1}
  	});
  }

  decrement = () => {
  	this.setState((state) => {
    	return {counter: state.counter - 1}
  	});
  }

  render() {
    return (
        <div>
        	<p>Counter: {this.state.counter + this.props.counter}</p>
        	<button onClick={ this.increment } >Increment</button>
        	<button onClick={ this.decrement } >Decrement</button>
        </div>
    )
  }
}

export default Counter
