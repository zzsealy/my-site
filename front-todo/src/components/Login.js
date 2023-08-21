import { useState } from "react"
import axios from 'axios'
import { useNavigate, Link } from "react-router-dom"

import {constant} from '../constant'
import { Banner } from '@douyinfe/semi-ui';




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
        width: '200px',
        margin: '0 auto',

    }

    const loginButtonStyle = {
        margin: '10px 0px 0px 20px',
    }

    const inputStyle = {
        margin: '0px 0px 0px 20px'
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
            <h1>登录</h1>
            {showBanner? LoginBanner: null}
                <form>
                    <div style={inputStyle}><strong>账号:</strong> <input onChange={handleUsername}></input></div>
                    <div style={inputStyle} ><strong>密码:</strong> <input type='password' onChange={handlePassword}></input></div>
                    <br></br>
                    <button style={loginButtonStyle} onClick={Login}>登录</button>
                    <button style={loginButtonStyle} ><Link to='/register'>注册</Link></button>
                </form>
        </div>
    )
}

export default Login