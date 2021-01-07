import { http } from './config'

// Este é o meu sufixo
export default{
    // Método para listar items
    listar:() => {
        return http.get('Livros')
    },
    // Métodos para salvar items
    salvar:(livros) => {
        return http.post('Livros', livros)
    },
    edit:(livros) => {
        return http.put('Livros', livros)
    },
    delete:(livros) => {
        return http.delete('Livros', {data: livros})
    }

}