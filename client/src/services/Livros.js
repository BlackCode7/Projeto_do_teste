import { http } from './config'

// Este é o meu sufixo
export default{
    // Método para listar items
    listar:() => {
        return http.get('livros')
    },
    // Métodos para salvar items
    salvar:(livros) => {
        return http.post('livros', livros)
    },
    atualizar:(livros) => {
        return http.put('livros', livros)
    },
    delete:(livros) => {
        return http.delete('livros', {data: livros})
    }

}