import React from 'react';
import './search.styles.css';
import Autosuggest from 'react-autosuggest';
import { createHashHistory } from 'history'
import {Link} from 'react-router-dom';

//import Button from 'react-bootstrap/Button'

// When suggestion is clicked, Autosuggest needs to populate the input
// based on the clicked suggestion. Teach Autosuggest how to calculate the
// input value for every given suggestion.
const getSuggestionValue = suggestion => suggestion.labelName.english;

// Use your imagination to render suggestions.
const renderSuggestion = suggestion => (
  <div>
    {suggestion.labelName.english}
  </div>
);

class Example extends React.Component {
  constructor(props) {
    super(props);
  
    // Autosuggest is a controlled component.
    // This means that you need to provide an input value
    // and an onChange handler that updates this value (see below).
    // Suggestions also need to be provided to the Autosuggest,
    // and they are initially empty because the Autosuggest is closed.
    this.state = {
      value: '',
      suggestions: [],
      choices: []
    };
  }

  onChange = (event, { newValue }) => {
    this.setState({
      value: newValue
    });
  };

  // Autosuggest will call this function every time you need to update suggestions.
  // You already implemented this logic above, so just use it.
  onSuggestionsFetchRequested = ({ value }) => {
	fetch('http://127.0.0.1:8000/api/product_id?query=' + value)
	.then((response) => response.json())
	.then((responseJson) => {
		this.setState({suggestions: responseJson});  //***** put the result -> state
	})
	.catch((error) => {
		console.error(error);
	})
  };

  // Autosuggest will call this function every time you need to clear suggestions.
  onSuggestionsClearRequested = () => {
    this.setState({
      suggestions: []
    });
  };

onSuggestionSelected = (event, { suggestion, suggestionValue}) => {
	//console.log(suggestion);
	var joined = this.state.choices.concat(suggestion);
	this.setState({ choices: joined })
  console.log(this.state.choices);
  this.setState({value: ""});  //***** put the result -> state

};

getAdress = () => {
  var str = "/map?ids=";

  for(let i=0;i<this.state.choices.length;i++)
  {
    if(i==0)
      str += this.state.choices[i]["ean"];
    else
      str += "," + this.state.choices[i]["ean"];
  }
    return str;
}


  render() {
    const { value, suggestions } = this.state;

    // Autosuggest will pass through all these props to the input.
    const inputProps = {
      placeholder: 'Type a product...',
      value,
      onChange: this.onChange
  };

	

    // Finally, render it!
    return (
		<div className="container">
      	<Autosuggest
			suggestions={suggestions}
			onSuggestionsFetchRequested={this.onSuggestionsFetchRequested}
			onSuggestionsClearRequested={this.onSuggestionsClearRequested}
			onSuggestionSelected={this.onSuggestionSelected}
			renderSuggestion={renderSuggestion}
			getSuggestionValue={getSuggestionValue}
			inputProps={inputProps}
			/>

    <a href={this.getAdress()}>
      <button>SHOP ({this.state.choices.length})</button>
    </a>

		</div>
    );
  }
}

export default Example