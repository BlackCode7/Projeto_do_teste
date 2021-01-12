import { http } from './configServices'

export default {
    //criando o metodo para listar os métodos
    // com o verbo get() pegando o Livros no 
    // final da url (sufixo)
    listar:() => {
        return http.get('Livros')
    },
    add:(Livro) => {
        return http.post('Livro', Livro)
    }
}
