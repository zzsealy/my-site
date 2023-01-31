import { Route, Routes } from 'react-router-dom'
import Home from './components/Home'
import TodoList from './components/TodoList'


function App() {
  return (
    <Routes>
      <Route exact path='/' element={<Home />} />
      <Route exact path='todo_list/:id' element={<TodoList />} />
    </Routes>
  );
}

export default App;
