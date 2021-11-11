import React from "react"




class Login extends React.Component {

    initialState = { "username": '', "password": '', "remember": "n"}

    state = this.initialState

    handleChange = (event) => {
        const { name, value } = event.target;
        this.setState({
            [name]: value,
        })
    }

    submitForm = (event) => {
        event.preventDefault();
        (async () => {
            const rawResponse = await fetch('http://127.0.0.1:5000/apilogin', {
              method: 'POST',
              headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({a: 1, b: 'Textual content'})
            });
            const content = await rawResponse.json();
          
            console.log(content);
          })();
        
    }

    render() {
        const { username, password, remember } = this.state;
        return (
            <form className="loginForm">
                <p>username:</p> <input onChange={this.handleChange} type="username" name="username" value={username}></input>
                <p>password:</p> <input onChange={this.handleChange} type="password" name="password" value={password}></input>
                <div className="form-group form-check">
                    <input name="remember" value={remember} id="remember" type="checkbox"></input> remember me
                </div>
                <input type="submit" onClick={this.submitForm}/>
                
            </form>
        )
    }
}



export default Login