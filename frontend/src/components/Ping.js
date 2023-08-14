import axios from 'axios'
import { useEffect, useState } from 'react'
import constant from '../constant'

const Ping = () => {
    const [ping, setPing] = useState('ping')
    const pingEffect = () => {
        axios.get(`${constant.baseUrl}/ping`)
            .then((res) => {
                setPing(res.data);
            })
            .catch((error) => {
                console.log(error)
            })
    }

    useEffect(pingEffect, [])
    return (
        <div>
            <h1>{ping}</h1>
        </div>
    )
}

export default Ping