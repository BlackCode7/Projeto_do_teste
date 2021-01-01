<template>
  <div id="app">

    <nav>
      <div class="nav-wrapper blue darken-1">
        <a href="#" class="brand-logo center">Cadastro Livros</a>
      </div>
    </nav>

    <div class="container">

      <form>

          <label>Id</label>
          <input v-model="livro.id" type="number" placeholder="Id">
          <label>livro</label>
          <input v-model="livro.livro" type="text" placeholder="Nome">
          <label>autor</label>
          <input type="text" placeholder="Autor">
          <label>Lido</label>
          <input type="text" placeholder="JÃ¡ leu o livros? sim / nÃ£o">

          <button @click.prevent="mensage()" class="waves-effect waves-light btn-small">Salvar<i class="material-icons left">save</i></button>

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
          <tr v-for="livro1 in livros" :key="livro1.id">
            <td>{{ livro1.id }}</td>
            <td>{{ livro1.livro }}</td>
            <td>{{ livro1.autor }}</td>
            <td>{{ livro1.lido }}</td>
            <td>
              <button class="waves-effect btn-small blue darken-1"><i class="material-icons">create</i></button>
              <button class="waves-effect btn-small red darken-1"><i class="material-icons">delete</i></button>
            </td>
          </tr>
        </tbody>
      
      </table>

    </div>

  </div>
</template>

<script>

import Livros from '../services/Livros'


export default {  
  
  data(){
    return {
      livros: null,
      livro: {
        id: null,
        livro1: null,
        autor:null,
        lido: null
      },
      erros:[]    
    }
  },
  
  //montando a resposta que vem de services Livros
  //dentro da variavel Livro
  mounted(){
    Livros.listar().then(resposta => {
      console.log(resposta.data)
      this.livros = resposta.data
    })
  },

  methods: {
        
  }

}

</script>

<style>

</style>
