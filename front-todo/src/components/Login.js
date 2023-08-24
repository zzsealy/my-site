import { useState } from "react"
import axios from 'axios'
import { useNavigate, Link } from "react-router-dom"
import { Input } from '@douyinfe/semi-ui';
import {constant} from '../constant'
import { Banner, Button} from '@douyinfe/semi-ui';




const Login = () => {
    const navigate = useNavigate();
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [showBanner, setShowBanner] = useState(false)

    const changeShowBanner = () => {
        setShowBanner(!showBanner)
    }

    const LoginBanner = (
        <Banner onClose={changeShowBanner} type='warning'
            description="密码错误"
        />
    )

    const loginStyle = {
        display: 'flex',
        justifyContent: 'center', // 水平局中
        alignItems: 'center',
        height: '100vh'

    }

    const formStyle = {
        flexDirection: 'column', // 切换为列布局
        alignItems: 'centent'
    }

    const todoTitle = {
        position: 'absolute',
        fontSize: '1.8rem',
        top: '80px',
        left: '100px',
        background: "url('./favicon.ico') no-repeat ",
        width: '200px',
        height: '100px',
        paddingLeft: '60px',
        paddingTop: '10px'
    }

    const loginButtonStyle = {
        border: '1px solid black',
        margin: '10px 0px 0px 20px',
        width: '100px',
        height: '24px',
    }

    const inputStyle = {
        width: '240px',
        height: '24px'
    }

    const loginTitle = {
        textAlign: 'center',
        fontSize: '3rem',
        marginBottom: '-2px'
    }

    const inputAndLableStyle = {
        margin: '0px 0px 10px 20px',
        color: '#B5AFAD'
    }

    const Login = (event) => {
        event.preventDefault();
        localStorage.removeItem('todo_token')
        const loginUrl = `${constant.baseUrl}/users/login`
        const loginData = {'username': username, 'password': password}
        axios.post(loginUrl, loginData)
            .then((res) => {
                const status_code = res.data.status_code;
                if (status_code === 200) {
                    const token = res.data.token;
                    localStorage.setItem('todo_token', token)
                    navigate('/')
                    console.log('登录成功')
                }
                if (status_code === 400) { // 验证失败
                    setShowBanner(true)
                }
                console.log('收到登录返回')
            })
    }

    const handleUsername = (event) => {
        let username = event.target.value
        setUsername(username)
    }

    const handlePassword = (event) => {
        let password = event.target.value
        setPassword(password)
    }

    return (
        <div style={loginStyle}>
            <span style={todoTitle}>待办事项！</span>
            {/* {showBanner? LoginBanner: null} */}
                <form style={formStyle}>
                    <div><h1 style={loginTitle}>登录</h1></div>
                    <div style={inputAndLableStyle}>
                        <div>
                            <strong>账号:</strong>
                        </div>
                        <Input style={inputStyle} onChange={handleUsername}></Input>
                    </div>
                    <div style={inputAndLableStyle}>
                        <div>
                            <strong>密码:</strong>
                        </div>
                        <Input style={inputStyle} type='password' onChange={handlePassword}></Input>
                    </div>
                    <br></br>
                        <Button style={loginButtonStyle} onClick={Login}>登录</Button>
                        <Button style={loginButtonStyle} ><Link to='/register'>注册</Link></Button>
                </form>
        </div>
    )
}

export default Login