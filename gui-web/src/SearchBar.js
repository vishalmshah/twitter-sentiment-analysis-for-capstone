import React, { Component } from 'react'
// import axios from 'axios'
import './search.css'

class SearchBar extends Component {
  constructor() {
    super();

    this.state = {
      data: {
        search: ''
      },
      sentiment: null
    };
  }

  // universal onChange Function
  onChange = e => {
    this.setState({
      data: { ...this.state.data, [e.target.name]: e.target.value }
    });
  }

  onSubmit = (e) => {
    e.preventDefault();
    // this.setState({ sentiment: fetch('/api/tweet').then(res => res) })
    this.props.submit(this.state.data)
  }

  render() {
    const { data } = this.state;

    return (
      <div>
        <form onSubmit={this.onSubmit}>
          <input
            type='search'
            id='search'
            name='search'
            placeholder='Tweet Here'
            value={data.search}
            onChange={this.onChange}
          />
        </form>
      </div>
    );
  }

}

export default SearchBar
