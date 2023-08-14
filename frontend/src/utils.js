

const requestConfig = () => {
    const token = window.localStorage.getItem('todo_token')
    if (token) {
        const authToken = `Bearer ${token} `
        const config = {
            'headers': { Authorization: authToken }
        }
        return config
    }
    return {}
}

const add = (a, b) => {
    return a + b
}


export {
    requestConfig,
    add
}


