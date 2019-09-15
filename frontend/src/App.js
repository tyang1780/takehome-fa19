import React, { Component } from 'react'
import Instructions from './Instructions'
import Contact from './Contact'
import Counter from './Counter'

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      name : '',
      nickname : '',
      hobby : '',
      counter : 3,
      contacts: [
        {id: 1, name: "Angad", nickname: "greg", hobby: "dirty-ing"},
        {id: 2, name: "Roy", nickname: "uwu", hobby: "weeb"},
        {id: 3, name: "Daniel", nickname: "oppa", hobby: "losing money with options trading"},
      ]
    }
  }

  handleChange = (event) => {
    this.setState({[event.target.name]: event.target.value});
  }

  addContact = () => {
    this.setState(state => {
      const list = state.contacts.push({id: state.counter + 1, name:state.name, nickname: state.nickname, hobby:state.hobby});

      return {
        name : '',
        nickname : '',
        hobby : '',
        counter: state.counter + 1,
        list
      }
    })
  }

  render() {
    return (
      <div className="App">
        <Instructions complete={true}/>
        <Counter counter={this.state.counter}/>

        {this.state.contacts.map(x => (
          <Contact id={x.id} name={x.name} nickname={x.nickname} hobby={x.hobby} />
        ))}

          <label>
            Name:
            <input type="text" name="name" value={this.state.name} onChange={this.handleChange}/>
          </label>
          <label>
            Nickname:
            <input type="text" name="nickname" value={this.state.nickname} onChange={this.handleChange}/>
          </label>
          <label>
            Hobby:
            <input type="text" name="hobby" value={this.state.hobby} onChange={this.handleChange}/>
          </label>
          <button type="button" onClick={this.addContact}>Submit</button>

      </div>
    )
  }
}

export default App
