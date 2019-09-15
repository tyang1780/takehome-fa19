import React, { Component } from 'react'

class App extends Component {
  // YOUR CODE GOES BELOW

  render() {
    return (
      <div>
      	 <p>ID: {this.props.id} Name: {this.props.name} Nickname: {this.props.nickname} Hobby: {this.props.hobby}</p>
      </div> 
    )
  }
}

export default App
