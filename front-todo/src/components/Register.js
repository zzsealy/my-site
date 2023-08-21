import { useState } from "react"
import axios from 'axios'
import { useNavigate } from "react-router-dom"
import { Notification } from "@douyinfe/semi-ui"

import {constant, statusCode} from '../constant'


const Register = () => {
    const navigate = useNavigate();
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [passwordRepeat, setPasswordRepeat] = useState('')
    const [name, setName] = useState('')

    const opts = {
        duration: 3,
        position: 'topRight',
        content: '',
        title: '',
    }
    
    const registerTitle = {
    }

    const loginStyle = {
        display: 'flex',
        justifyContent: 'center', // 水平局中
        alignItems: 'center',
        height: '100vh'
    }

    const loginButtonStyle = {
        margin: '10px 0px 0px 20px',
    }

    const formStyle = {
        flexDirection: 'column', // 切换为列布局
        alignItems: 'centent'
    }

    const inputStyle = {
        margin: '0px 0px 0px 20px',
        color: '#B5AFAD'
    }

    const Register = (event) => {
        event.preventDefault();
        const registerUrl = `${constant.baseUrl}/users/register`
        const registerData = {
            'username': username, 'password': password,
            'passwordRepeat': passwordRepeat, 'name': name
        }
        axios.post(registerUrl, registerData)
            .then((res) => {
                const status_code = res.data.status_code
                debugger;
                if (status_code === statusCode.OK) {
                    return(
                        navigate('/login')
                    )
                }
                if (status_code === statusCode.PASS_NOT_EQUAL) {
                    Notification.error({...opts,  position: 'top', title: '两次密码不一致', content: '请重新输入'})
                }
            })
            .catch((error) => {
                console.log(error)
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

    const handlePasswordRepeat = (event) => {
        let passwordRepeat = event.target.value
        setPasswordRepeat(passwordRepeat)
    }

    const handleName = (event) => {
        let name = event.target.value
        setName(name)
    }

    return (
        <div style={loginStyle}>
            <form style={formStyle}>
                <div><h1 style={registerTitle}>注册</h1></div>
                <div style={inputStyle}><strong>账号:</strong> <input onChange={handleUsername}></input></div>
                <div style={inputStyle}><strong>密码:</strong> <input type='password' onChange={handlePassword}></input></div>
                <div style={inputStyle}><strong>重复密码:</strong> <input type='password' onChange={handlePasswordRepeat}></input></div>
                <div style={inputStyle}><strong>名字:</strong> <input onChange={handleName} placeholder='输入一个昵称'></input></div>
                <br></br>
                <button style={loginButtonStyle} onClick={Register}>注册</button>
            </form>
        </div>
    )
}

export default Register