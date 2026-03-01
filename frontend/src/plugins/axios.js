import axios from 'axios'

const apiClient = axios.create({
    baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api/',
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json',
    },
})

// Request Interceptor to add JWT Auth Token
apiClient.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access_token')
        if (token) {
            config.headers['Authorization'] = `Bearer ${token}`
        }
        return config
    },
    (error) => Promise.reject(error)
)

// Response Interceptor for handling token expiry
apiClient.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config

        // Check if error is 401 Unauthorized and we haven't retried yet
        if (error.response?.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true

            const refreshToken = localStorage.getItem('refresh_token')
            if (refreshToken) {
                try {
                    const response = await axios.post(`${apiClient.defaults.baseURL}token/refresh/`, {
                        refresh: refreshToken
                    })

                    localStorage.setItem('access_token', response.data.access)
                    originalRequest.headers['Authorization'] = `Bearer ${response.data.access}`
                    return apiClient(originalRequest)
                } catch (refreshError) {
                    // If refresh fails, clearly log out user
                    localStorage.removeItem('access_token')
                    localStorage.removeItem('refresh_token')
                    window.location.href = '/login'
                    return Promise.reject(refreshError)
                }
            }
        }
        return Promise.reject(error)
    }
)

export default apiClient
