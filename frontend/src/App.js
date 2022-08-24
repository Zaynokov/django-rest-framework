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
import LoginForm from './components/Auth';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom'
import Cookies from 'universal-cookie';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': [],
      'projects': [],
      'notes': [],
      'token': ''
    }
  }

  set_token(token) {
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState({ 'token': token }, () => this.loadData())
  }

  is_authenticated() {
    return this.state.token != ''
  }

  get_authenticated_user() {
    axios.get('http://127.0.0.1:8000/api/users/')
  }

  logout() {
    this.set_token('')
  }

  get_token_from_storage() {
    const cookies = new Cookies()
    const token = cookies.get('token')
    this.setState({ 'token': token }, () => this.loadData())
  }

  get_token(username, password) {
    axios.post('http://127.0.0.1:8000/api-token-auth/', {
      username: username,
      password: password
    })
      .then(response => {
        this.set_token(response.data['token'])
      }).catch(error => alert('Неверный логин или пароль'))
  }

  get_headers() {
    let headers = {
      'Content-Type': 'application/json'
    }
    if (this.is_authenticated()) {
      headers['Authorization'] = 'Token ' + this.state.token
    }
    return headers
  }

  loadData() {
    const headers = this.get_headers()
    axios.get('http://127.0.0.1:8000/api/users', { headers })
      .then(response => {
        const users = response.data.results;
        this.setState(
          {
            'users': users
          }
        )
      }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/api/projects', { headers })
      .then(response => {
        const projects = response.data.results;
        this.setState(
          {
            'projects': projects
          }
        )
      }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/api/notes', { headers })
      .then(response => {
        const notes = response.data.results;
        this.setState(
          {
            'notes': notes
          }
        )
      }).catch(error => console.log(error))
  }

  componentDidMount() {
    this.get_token_from_storage()
  }

  render() {
    return (
      <div>
        <Router>
          <nav>
            <ul>
              <li>
                <Link to='users'>Users</Link>
              </li>
              <li>
                <Link to='projects'>Projects</Link>
              </li>
              <li>
                <Link to='notes'>Notes</Link>
              </li>
              <li>
                {this.is_authenticated() ? <button onClick={() => this.logout()}>{}Logout</button> :
                  <Link to='/login'>Login</Link>}
              </li>
            </ul>
          </nav>
          <Routes>
            <Route exact path='/users' element={<UserList users={this.state.users} />} />
            <Route exact path='/projects' element={<ProjectList projects={this.state.projects} />} />
            <Route exact path='/notes' element={<NoteList notes={this.state.notes} />} />
            <Route path='/projects/:id' element={<ProjectDetail projects={this.state.projects} />} />
            <Route exact path='/login' element={<LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
            <Route path='*' element={<NotFound404 />} />
          </Routes>
        </Router>
        <Footer />
      </div>
    )
  }
}

export default App;
