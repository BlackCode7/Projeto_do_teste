<template>
  <div id="app">

    <nav>
      <div class="nav-wrapper blue darken-1">
        <a href="#" class="brand-logo center">Cadastro de Livros</a>
      </div>
    </nav>

    <ul>
      <li v-for="(error, index) of errors" :key="index">
        campo <b>{{ erro.field }}</b>{{ erro.defaultMessage }}
      </li>
    </ul>

    <div class="container">
      {{livroServices_.id}}
      {{livroServices_.titulo}}
      {{livroServices_.autor}}
      {{livroServices_.lido}}
      
      <!--Metodo para salvar os dados do formulário-->
      <form @submit.prevent="salvar()">
          <label>Id</label>
          <input type="number" placeholder="Id" v-model="livroServices_.id">
          <label>Título</label>
          <input type="text" placeholder="Título do livro" v-model="livroServices_.titulo">
          <label>Autor</label>
          <input type="text" placeholder="nome do autor" v-model="livroServices_.autor">
          <label>Lido</label>
          <input type="text" placeholder="já leu o livro? Sim/Não" v-model="livroServices_.lido">
          <button class="waves-effect waves-light btn-small">Salvar<i class="material-icons left">save</i></button>
      </form>

      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>TITULO</th>
            <th>AUTOR</th>
            <th>LIDO</th>
          </tr>
        </thead>

        <tbody>
          <tr v-for="livrosService of livroServices" :key="livrosService.id">
            <td>{{ livrosService.id }}</td>
            <td>{{ livrosService.titulo }}</td>
            <td>{{ livrosService.autor }}}</td>
            <td>{{ livrosService.lido }}</td>
            <td>
              <button class="waves-effect btn-small blue darken-1"><i class="material-icons">create</i></button>
              <button class="waves-effect btn-small red darken-1"><i class="material-icons">delete_sweep</i></button>
            </td>
          </tr>
        </tbody>      
      </table>
    </div>
  </div>
</template>

<script>
import LivroServices from './services/livroServices'
export default {
  data(){
    return{
      //Objeto que vem do formulário
      livroServices_: {
        id: null,
        titulo:null,
        autor:null,
        lido:null
      },
      //objeto que lista os dados
      livroServices: [],
      //quardando os erros do catch()
      errors: []
    }
  },
  
  mounted(){ 
    this.listar_()   
  },

  methods: {
    //Listando os dados
    listar_(){
      LivroServices.listar().then(resposta => {
        //console.log(resposta.data)
        this.livroServices = resposta.data
      })
    },

    // Salvando e listando os dados
    salvar(){
      LivroServices.add(this.livroServices_).then(resposta => {
        this.livroServices_ = {}
        alert('Salva com Sucesso!')
        console.log(resposta.data)
        this.listar_()
        //Limpando os erros da aplicação
        this.errors = []
        // Tratando o erro com catch()
        // mostrando somente os erros desejados
        // guardando os erros em uma variável erros
      }).catch(e =>{
        console.log(e.response.data.errors)
        this.errors = e.response.data.errors
      })
      //alert(this.livroServiceSalva.nome)
    }

  }
}
</script>

<style>
</style>
