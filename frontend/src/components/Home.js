import { useState, useEffect } from 'react'
import axios from 'axios'
import { Button, Toast, Col, Row, Card, Typography } from '@douyinfe/semi-ui';


import constant from '../constant'


const Todo = ({ todo }) => {
    return (
        <li>
            {todo.body}
       </li>
   ) 
}

const TodoList = ({ todoList }) => {
    const title = todoList.finish_rate + '  ' + todoList.create_datetime
    const { Text } = Typography;
    return (
        <Card title = {title}
            style={{ maxWidth: 250, display: 'inline-block', }}
            headerExtraContent={
                <Text link>
                    查看详情
                </Text>
        }
        >  
            <ul>
                {todoList.child_todo.map(todo => <Todo key={todo.id} todo={todo}/>)}
            </ul>
        </Card>
    )
}

const Home = () => {
    const [todoLists, setTodoLists] = useState([])


    const totalTodoListHooks = () => {
        const getTodoListPath = `${constant.baseUrl}/todo`
        axios.get(getTodoListPath)
            .then((res) => {
                setTodoLists(res.data)
                console.log(res);
          })

    }
    useEffect(totalTodoListHooks, [])
    return (
        <div className='grid'>
            <Row>
                <Col span={14} offset={4}>
                    {todoLists.map(todoList => <TodoList key={todoList.id} todoList={todoList}/>)}
                </Col>
            </Row>
        </div>
    )
}

export default Home