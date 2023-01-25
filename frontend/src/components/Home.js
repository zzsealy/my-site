import { useState, useEffect } from 'react'
import axios from 'axios'
import constant from '../constant'


const Todo = () => {
    return (
        <p>todo</p>
    )
}

const Home = () => {
    const [todoList, setTodoList] = useState([])


    const totalTodoListHooks = () => {
        const getTodoListPath = `${constant.baseUrl}/todo`
        axios.get(getTodoListPath)
            .then((res) => {
                setTodoList(res)
                console.log(res);
          })

    }
    useEffect(totalTodoListHooks, [])
    return (
        <div>
            <h1>hello</h1>
        </div>
    )
}

export default Home