import axios from 'axios'

// Este é o meu prefixo
export const http = axios.create({
    baseURL: 'http://127.0.0.1:5000/'
})