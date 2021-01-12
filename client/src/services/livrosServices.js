// _ sufixo _
import { http } from './configServices'

export default {
    // criando metodo listar
    listar:() => {
        return http.get('Livros')
    }    
}