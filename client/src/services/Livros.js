import { http } from './config'

// Este é o meu sufixo
export default{
    listar:() => {
        return http.get('livros')
    }
}