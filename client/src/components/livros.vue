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
          <button class="waves-effect waves-light btn-small">Salvar<i class="material-icons left">save</i></button>

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
              <!--@click.prevent.stop="editar(livro)" -->
              <button class="waves-effect btn-small blue darken-1"><i class="material-icons">create</i></button>
              <!--@click.prevent.stop="deletar(livro)"-->
              <button class="waves-effect btn-small red darken-1"><i class="material-icons">delete</i></button>

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
import serviceLivros from '../services/Livros'
export default {    
  data(){
    return {
      //livros: null,
      livro: {        
        id: null,
        livro: null,
        autor:null,
        lido: null
      },
      
      serviceLivros:[],
      errors:[]    
    }
  },  
  
  //montando a resposta que vem de services Livros
  //dentro da variavel Livro
  mounted(){
    this.listar()
  },

  methods: {
    
    // Listar os itens da lista de livros
    listar(){
      serviceLivros.listar().then(resposta => {
        this.serviceLivros = resposta.data
      })
    },
        
  }
}

</script>