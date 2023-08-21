import { Route, Routes } from 'react-router-dom'
// import { use}

import Home from './components/Home'
import TodoList from './components/TodoList'
import Ping from './components/Ping'
import Login from './components/Login'
import Register from './components/Register'
import ProtectedRoute from './components/ProtectedRoute'

// const LoginStatus = () => {
//   // localStorage.setItem('user', 'drq')
//   const loginStatus = localStorage.getItem('user')
//   if (loginStatus) {
//     return (
//       <button>Logout</button>
//     )
//   } else {
//     return (
//       <button>Login</button>
//     )
//   }
// }

function App() {
  return (
    <>
      {/* <LoginStatus/> */}
      
    <Routes>
        <Route element={<ProtectedRoute user={{'user': 'drq'}} />}>
          <Route path='ping' element={<Ping />} />
          <Route exact path='/' element={<Home />} />
          <Route exact path='todo_list/:id' element={<TodoList />} />
        </Route>
      <Route exact path='login' element={<Login />} />
      <Route exact path='register' element={<Register />} />
    </Routes>
    </>
  );
}

export default App;
