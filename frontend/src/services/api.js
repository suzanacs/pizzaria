import axios from 'axios'



const api = axios.create({
    baseURL: 'http://universodapizza.com.br/api/'
})


export default api