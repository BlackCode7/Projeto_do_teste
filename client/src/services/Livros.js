import { http } from './config'

// Este é o meu sufixo
export default{
    // Método para listar items
    listar:() => {
        return http.get('Livros')
    }
    

}