import React, { Component } from 'react';
import axios from 'axios'
import SearchBar from './SearchBar'
import Tweet from './Tweet'
import './App.css';

class App extends Component {
  constructor() {
    super()

    this.state = {
      data: '',
      sentiment: null
    }
  }

  submit = (data) => {
    // console.log(data)
    axios.post('/api/tweet', { data }).then(res => {
      this.setState({ sentiment: res.data.response, data: data.search })
    })
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <Tweet text={this.state.data} />
          <SearchBar submit={this.submit} />
          <p>Enter your tweet's text to get a sentiment!</p>
          <p>{this.state.sentiment}</p>

        </header>
      </div>
    );
  }

}

export default App;
