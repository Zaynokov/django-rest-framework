import logo from './logo.svg';
import './App.css';
import React from "react";
import axios from 'axios';
import UserList from './components/User';
import ProjectList from './components/Project';
import NoteList from './components/Note';
import Menu from './components/Menu'
import Footer from './components/Footer';
import NotFound404 from './components/NotFound404';
import ProjectDetail from './components/ProjectDetail';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': [],
      'projects': [],
      'notes': []
    }
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/users')
      .then(response => {
        const users = response.data.results;
        this.setState(
          {
            'users': users
          }
        )
      }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/api/projects')
      .then(response => {
        const projects = response.data.results;
        this.setState(
          {
            'projects': projects
          }
        )
      }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/api/notes')
      .then(response => {
        const notes = response.data.results;
        this.setState(
          {
            'notes': notes
          }
        )
      }).catch(error => console.log(error))
  }

  render() {
    
    return (
      <div>
        <Router>
          <Menu />
            <Routes>
              <Route exact path='/users' element={<UserList users={this.state.users} />} />
              <Route exact path='/projects' element={<ProjectList projects={this.state.projects} />} />
              <Route exact path='/notes' element={<NoteList notes={this.state.notes} />} />
              <Route path='/projects/:id' element={<ProjectDetail projects={this.state.projects} />} />
              <Route path='*' element={<NotFound404/>} />
            </Routes>
        </Router>
        <Footer />
      </div>
    )
  }
}



export default App;
