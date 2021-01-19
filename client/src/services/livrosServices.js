import  { http } from './configServices'

export default {
    //criando o metodo para listar os métodos
    // com o verbo get() pegando o Livros no 
    // final da url (sufixo)
    listar_:() => {
        return http.get('Livros')
    },

    // Aqui é onde esta o problema do porque não 
    // consigo fazer a aplicação funcionar direito
    // Não entendi como fazer o método retornar os 
    // dados em json
    salvar_:(Livros) => {
        return http.post('Livros', Livros)
    },

    // Método para atualizar os dados
    atualizar_: (Livros)=> {
        return http.put('Livros', Livros)
    }
}
