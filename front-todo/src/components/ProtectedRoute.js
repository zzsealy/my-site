import { Navigate, Outlet, useNavigate } from "react-router-dom"


const ProtectedRoute = ({ user }) => {
    const navigate = useNavigate();
    if (!user) {
        return (
            navigate('/login')
        )
    } else {
        return (
            <Outlet />
        )
    }
}

export default ProtectedRoute