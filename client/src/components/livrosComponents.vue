<template>
  <div id="app">

    <nav>
      <div class="nav-wrapper blue darken-1">
        <a href="#" class="brand-logo center">Cadastro de Livros</a>
      </div>
    </nav>

    <div class="container">

      <ul>
        <li v-for="(error, index) of errors" :key="index">
          campo <b> {{error.field}} </b> - {{ error.defaultMessage }}
        </li>
      </ul>    

      <form>

          <label>Id</label>
          <input v-model="livro.id" type="number" placeholder="Id">
          <label>livro</label>
          <input v-model="livro.livro" type="text" placeholder="Nome">
          <label>autor</label>
          <input v-model="livro.autor" type="text" placeholder="Autor">
          <label>Lido</label>
          <input v-model="livro.lido" type="text" placeholder="Já leu o livros? sim / nÃ£o">
          <!--@click.prevent.stop="salvar()"-->
          <button @click.prevent.stop="salvar()" class="waves-effect waves-light btn-small">Salvar<i class="material-icons left">save</i></button>

      </form>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>NOME DO LIVRO</th>
            <th>NOME DO AUTOR</th>
            <th>LIDO</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="livro in livros" :key="livro.id">
              <td>{{ livro.id }}</td>
              <td>{{ livro.livro }}</td>
              <td>{{ livro.autor }}</td>
              <td>{{ livro.lido }}</td>
              <td>
                <button @click.prevent.stop="editar(livro)" class="waves-effect btn-small blue darken-1"><i class="material-icons">create</i></button>
                <button @click.prevent.stop="add(livro)" class="waves-effect btn-small red darken-1"><i class="material-icons">delete</i></button>
              </td>
          </tr>
        </tbody>
     </table>
    </div>
  </div>
</template>

<script>
// Mudei o nome da varial de import para ficar mais claro e diferenciar 
// Mais os nomes entre variáveis
// dois ponto(../)para procurar fora da pasta components
import LivrosServices from '../services/livrosServices'

export default {    
  data(){
    return {
      //livros: null,
      livros: null               
    }
  },  
  
  //montando a resposta que vem de services Livros
  //dentro da variavel Livro
  mounted(){
    LivrosServices.listar().then(resposta => {
      console.log(resposta.data)
      this.livros = resposta.data
    })    
  },

  // outros metodos

}

</script>