import { useState } from "react"
import axios from 'axios'
import { useNavigate } from "react-router-dom"

import constant from '../constant'


const Register = () => {
    const navigate = useNavigate();
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [passwordRepeat, setPasswordRepeat] = useState('')
    const [name, setName] = useState('')

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

    const Register = (event) => {
        event.preventDefault();
        const registerUrl = `${constant.baseUrl}/user/register`
        const registerData = {
            'username': username, 'password': password,
            'passwordRepeat': passwordRepeat, 'name': name
        }
        axios.post(registerUrl, registerData)
            .then((res) => {
                const code = res.data.code
                if (code === 200) {
                    return(
                        navigate('/login')
                    )
                }
                if (code === 1001) {
                    console.log('账户已存在')
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
            <h1>注册</h1>
            <form>
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