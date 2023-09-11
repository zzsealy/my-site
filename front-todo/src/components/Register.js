import { useState } from "react"
import axios from 'axios'
import { useNavigate } from "react-router-dom"
import { Notification } from "@douyinfe/semi-ui"
import { Input } from '@douyinfe/semi-ui';

import {constant, statusCode} from '../constant'


const Register = () => {
    const navigate = useNavigate();
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [passwordRepeat, setPasswordRepeat] = useState('')
    const [name, setName] = useState('')

    const opts = {
        duration: 3,
        position: 'topRight',
        content: '',
        title: '',
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
    
    const registerTitle = {
        textAlign: 'center',
        fontSize: '3rem',
        marginBottom: '-2px'
    }

    const registerStyle = {
        display: 'flex',
        justifyContent: 'center', // 水平局中
        alignItems: 'center',
        height: '100vh'
    }

    const loginButtonStyle = {
        margin: '10px 0px 0px 20px',
        width: '240px',
        height: '24px'
    }

    const formStyle = {
        flexDirection: 'column', // 切换为列布局
        alignItems: 'centent'
    }

    const inputAndLableStyle = {
        margin: '0px 0px 10px 20px',
        color: '#B5AFAD'
    }

    const inputStyle = {
        width: '240px',
        height: '24px',
    }


    const Register = (event) => {
        event.preventDefault();
        const registerUrl = `${constant.baseUrl}/users/register`
        const registerData = {
            'email': email, 'password': password,
            'passwordRepeat': passwordRepeat, 'name': name
        }
        axios.post(registerUrl, registerData)
            .then((res) => {
                const status_code = res.data.status_code
                if (status_code === statusCode.OK) {
                    return(
                        navigate('/login')
                    )
                }
                if (status_code === statusCode.PASS_NOT_EQUAL) {
                    Notification.error({...opts,  position: 'top', title: '两次密码不一致', content: '请重新输入'})
                } else if (status_code === statusCode.EMAIL_EXIST){
                    Notification.error({...opts,  position: 'top', title: '邮箱已经存在', content: ''})
                } else {
                    Notification.error({...opts,  position: 'top', title: '发生错误', content: ''})
                }
            })
            .catch((error) => {
                console.log(error)
            })
    }

    const handleEmail = (email) => {
        setEmail(email)
    }

    const handlePassword = (password) => {
        setPassword(password)
    }

    const handlePasswordRepeat = (passwordRepeat) => {
        setPasswordRepeat(passwordRepeat)
    }

    const handleName = (name) => {
        setName(name)
    }

    return (
        <div style={registerStyle}>
            <span style={todoTitle}>待办事项！</span>
            <form style={formStyle}>
                <div><h1 style={registerTitle}>注册</h1></div>
                <div style={inputAndLableStyle}>
                    <div><small>邮箱:</small></div>
                     <Input showClear style={inputStyle} onChange={handleEmail}></Input>
                </div>
                <div style={inputAndLableStyle}>
                    <div><small>密码:</small></div>
                     <Input showClear style={inputStyle} type='password' onChange={handlePassword}></Input>
                </div>
                <div style={inputAndLableStyle}>
                    <div><small>重复密码:</small></div>
                    <Input showClear style={inputStyle} type='password' onChange={handlePasswordRepeat}></Input>
                </div>
                <div style={inputAndLableStyle}>
                    <div><small>名字:</small></div>
                    <Input showClear style={inputStyle} onChange={handleName} placeholder='输入一个昵称'></Input>
                </div>
                <br></br>
                <button style={loginButtonStyle} onClick={Register}>注册</button>
            </form>
        </div>
    )
}

export default Register