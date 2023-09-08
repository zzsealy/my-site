import { useState, useEffect, useMemo } from 'react'
import axios from 'axios'
import { Button, Col, Row, Card, Pagination, CardGroup, DatePicker, Divider, Banner, Select } from '@douyinfe/semi-ui';
import { useNavigate  } from 'react-router-dom';
import {statusCode, constant} from '../constant'
import { requestConfig } from '../utils'


const Todo = ({ todo }) => {
    if (!todo.content) {
        return (
            <br></br>
        )
    }
     else {
         return (
             <li>
                {todo.content.length > 7 ?
                todo.content.slice(0, 7): todo.content
                 }
        </li>
         )
    }
}

const TodoList = ({ todoList }) => {
    const title = `${todoList.title}`
    let blankLi = []
    if (todoList.child_todo.length < 4) {
        for (let i = todoList.child_todo.length; i < 4; i++){
            blankLi.push({'id': i, 'content': ''})
        }
    }
    return (
        <Card title = {title}
            style={{ maxWidth: 250, display: 'inline-block', }}
            shadows='hover'
        >  
            <ul>
                {todoList.child_todo.slice(0, 3).map(todo => <Todo key={todo.id} todo={todo} />)}
                {blankLi.map(todo => <Todo key={todo.id} todo={todo} />)}
                {todoList.child_todo.length > 3 ? 
                    '....' : ''
                }
            </ul>
                {todoList.can_change === true ? <p style={{'float': 'right', 'color': 'rgba(var(--semi-lime-5), 1)'}}>进行</p>
                    : <p style={{'float': 'right', 'color': 'rgba(var(--semi-yellow-4), 1)', }}>关闭</p>}
            <small style={{'color': 'rgba(var(--semi-grey-4), 1)'}}>{`完成时间 ${todoList.finishDate}`}</small>
        </Card>
    )
}




const Home = () => {
    const navigate = useNavigate();
    const [todoLists, setTodoLists] = useState([])
    const [dateString, setDateString] = useState([])
    const [todoListTitle, setTotoListTitle] = useState('')
    const [count, setCount] = useState(0)
    const [showBanner, setShowBanner] = useState(false)
    const [currentPage, setCurrentPage] = useState(1)
    const [todoListNum, setTodoListNum] = useState(0)
    const [tag, setTag] = useState('')
    const [filterTag, setFilterTag] = useState('')
    const [filterFinishStatus, setFilterFinishStatus] = useState('')
    const tagList = [
        { value: 'short', label: (<span style={{ 'color': 'rgba(var(--semi-red-5), 1)' }}>{'短期目标'}</span>), otherKey: 1},
        { value: 'long', label:(<span style={{ 'color': 'rgba(var(--semi-red-5), 1)' }}>{'长期目标'}</span>), otherKey: 2},
        { value: 'week', label:(<span style={{ 'color': 'rgba(var(--semi-red-5), 1)' }}>{'周目标'}</span>), otherKey: 3},
        { value: 'month', label:(<span style={{ 'color': 'rgba(var(--semi-red-5), 1)' }}>{'月目标'}</span>), otherKey: 4}
    ]

    const changeShowBanner = () => {
        setShowBanner(!showBanner)
    }

    const createTodoListErrorBanner = (
        <Banner onClose={changeShowBanner} type='warning'
            description="请输入TodoList的标题和选择时间"
        />
    )

    const filterTagDropDown = [
        { value: '', label: (<span style={{ 'color': 'rgba(var(--semi-light-blue-4), 1)' }}>{'全部'}</span>), otherKey: 1},
        { value: 'short', label: (<span style={{ 'color': 'rgba(var(--semi-light-blue-4), 1)' }}>{'短期目标'}</span>), otherKey: 1},
        { value: 'long', label:(<span style={{ 'color': 'rgba(var(--semi-light-blue-4), 1)' }}>{'长期目标'}</span>), otherKey: 2},
        { value: 'week', label:(<span style={{ 'color': 'rgba(var(--semi-light-blue-4), 1)' }}>{'周目标'}</span>), otherKey: 3},
        { value: 'month', label:(<span style={{ 'color': 'rgba(var(--semi-light-blue-4), 1)' }}>{'月目标'}</span>), otherKey: 4}
    ]

    const filterFinishDropDown = [
        { value: '', label: (<span style={{ 'color': 'rgba(var(--semi-light-blue-4), 1)' }}>{'全部'}</span>), otherKey: 1},
        { value: 'process', label: (<span style={{ 'color': 'rgba(var(--semi-light-blue-4), 1)' }}>{'进行中'}</span>), otherKey: 1},
        { value: 'finish', label: (<span style={{ 'color': 'rgba(var(--semi-light-blue-4), 1)' }}>{'完成'}</span>), otherKey: 1},
    ]

    const totalTodoListHooks = () => {
        let getTodoListPath = `${constant.baseUrl}/todo/todo_lists?page=${currentPage}`
        if (filterTag) { //标签过滤
            getTodoListPath = getTodoListPath + `&tag=${filterTag}`
        }
        if (filterFinishStatus) {
            getTodoListPath = getTodoListPath + `&status=${filterFinishStatus}`
        }
        const config = requestConfig()
        axios.get(getTodoListPath, config)
            .then((res) => {
                const status_code = res.data.status_code;
                if (status_code === statusCode.OK) {
                    setTodoLists(res.data.todo_list)
                    setTodoListNum(res.data.todo_list_num)
                    console.log(res);
                } 
                if (status_code === statusCode.AUTH_PASS) {
                    navigate('/login')
                }
            })
        document.title = '待办事项|DRQ'
    }
    useEffect(totalTodoListHooks, [count, todoListNum, currentPage, navigate])

    const handleClickTodoList = ({todoList}) => {
        // 点击单个的todo list 跳转到todo list 详情
        const id = todoList.id
        const toUrl = `/todo_list/${id}`
        navigate(toUrl)
        // console.log('点击了')
    }

    const handleTodoListTitle = (event) => {
        const inputTitle = event.target.value;
        setTotoListTitle(inputTitle)
    }

    const handleSelectTag = (value) => {
        setTag(value)
    }

    const handleFilterTag = (value) => {
        setFilterTag(value)
        setCount(count+1)
    }

    const handleFilterFinishStatus = (value) => {
        setFilterFinishStatus(value)
        setCount(count+1)
    }

    const handleClickPage = (currentPage) => {
        setCurrentPage(currentPage)
        setCount(count+1)
    }

    const handleClickCreateTodoList = () => {
        // 点击创建新的todo list
        const todoListPath = `${constant.baseUrl}/todo/todo_lists` 
        const config = requestConfig()
        const postData = {
            'title': todoListTitle,
            'dateString': dateString,
            'tag': tag,
        }
        axios.post(todoListPath, postData, config)
            .then((res) => {
                const status_code = res.data.status_code;
                if (status_code === 200) {
                    setCount(count+1)
                }
                if (status_code === 401) {
                    navigate('/login')
                }
                if (status_code === 400) {
                    setShowBanner(true)
                }
            })
    }

    const todoListStyle = {
        display: 'inline-block',
        background: '#888888'
    }
    return (
        <div className='grid'>
            <Row>
                {showBanner? createTodoListErrorBanner: null}
                <Col span={14} offset={4}>
                    <form style={{'border': '1px solid', 'color': "#c8c8c8", 'marginBottom': '20px'}}>
                        <input placeholder='标题' onChange={handleTodoListTitle} value={todoListTitle}></input>
                            <Divider layout="vertical" margin='12px' />
                        <DatePicker onChange={(date, dateString) => setDateString(dateString)} />
                            <Divider layout="vertical" margin='12px'/>
                        <Select onChange={handleSelectTag} placeholder='选择标签' style={{'width': '140px'}} optionList={tagList} validateStatus='warning'></Select>        
                            <Divider layout="vertical" margin='12px'/>
                        <Button onClick={() => handleClickCreateTodoList()}>创建TodoList</Button>
                    </form>
                    {/* <Button onClick={() => handleClickCreateTodoList()}> 创建TodoList </Button> */}
                    <CardGroup type='grid'>
                        {todoLists.map(todoList =>
                            <div onClick={() => handleClickTodoList({ todoList })} style={todoListStyle}>
                                <TodoList key={todoList.id} todoList={todoList} />
                            </div>)}
                    </CardGroup>
                    <Pagination onPageChange={handleClickPage} total={todoListNum} pageSize={12} style={{ marginBottom: 12 }}></Pagination>
                </Col>
                <Col span={1} offset={1}>
                        <Select onChange={handleFilterTag} placeholder='标签' style={{'width': '100px'}} optionList={filterTagDropDown} validateStatus='warning'></Select>        
                </Col>
                <Col span={1} offset={1}>
                        <Select onChange={handleFilterFinishStatus} placeholder='状态' style={{'width': '100px'}} optionList={filterFinishDropDown} validateStatus='warning'></Select>        
                </Col>
            </Row>
        </div>
    )
}

export default Home