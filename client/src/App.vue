<template>
  <div id="app">

    <nav>
      <div class="nav-wrapper blue darken-1">
        <a href="#" class="brand-logo center">Cadastro de Livros</a>
      </div>
    </nav>

    <ul>
      <li v-for="(error, index) of errors" :key="index">
        campo <b>{{ error.field }}</b>{{ error.defaultMessage }}
      </li>
    </ul>

    <div class="container">
      {{livroServices_.id}}
      {{livroServices_.titulo}}
      {{livroServices_.autor}}
      {{livroServices_.lido}}
      
      <!--Metodo para salvar os dados do formulário-->
      <form @click.capture="salvar" action="post">
          <label>Id</label>                              <!--livroServices_-->
          <input type="number" placeholder="Id" v-model="livroServices_.id">
          <label>Título</label>
          <input type="text" placeholder="Título do livro" v-model="livroServices_.livro">
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

        <!-- LIstagem de dados -->
        <tbody>
          <tr v-for="livroService of livroServicesLista" :key="livroService.id">
            <td>{{ livroService.id }}</td>
            <td>{{ livroService.livro }}</td>
            <td>{{ livroService.autor }}}</td>
            <td>{{ livroService.lido }}</td>
            <td>
              <button @click="editar(livroService)" class="waves-effect btn-small blue darken-1"><i class="material-icons">EditarBTN</i></button>
              <button @click="remover(livroService)" class="waves-effect btn-small red  darken-1"><i class="material-icons">DeleteBTN</i></button>
            </td>
          </tr>
        </tbody>      
      </table>
    </div>
  </div>
</template>

<script>
import LivroServices from './services/livrosServices'
export default {
  data(){
    return{           
      //Objeto que vem do formulário LIGADO ATRAVÉS DO V-MODEL
      //livroServices_
      livroServices_: {
        id: null,
        livro:null,
        autor:null,
        lido:null
      },            
      //objeto que lista os dados
      livroServicesLista: [],
      
      //quardando os erros do catch()
      errors: []
    }
  },  
  // Métodos para listagem de objetos preferêncialmento
  // fazemos dentro de mounted()
  mounted(){ 
    this.listar()   
  }, 
  // Crianção de métodos listar() salvar() deletar() atualizar()
  methods: {      
    listar(){
      LivroServices.listar_().then(resposta => {
        this.livroServicesLista = resposta.data
      })
    },    
    // Salvando e listando os dados
    salvar(){
      // Condicional para ver se exite o objeto e modificar seus valores
      if(!this.livroServices_.id){
        //this.livroServices_
        LivroServices.salvar_(this.livroServices_).then(resposta => {
            this.livroServices_ = resposta.data
            alert("Salvo com Sucesso!")
            console.log(resposta.data)
            this.listar()
            this.errors = []
            //this.livroServicesOBJ = resposta.data
          }).catch(e => {
            console.log(e.response.data.errors)
            this.errors = e.response.data.errors
          })
      }else{
        //this.livroServices_
        LivroServices.atualizar_(this.livroServices_).then(resposta => {
          this.livroServices_ = resposta.data
          alert("Atualizado com Sucesso!")
          console.log(resposta.data)
          this.listar()
          this.errors = []
          //this.livroServicesOBJ = resposta.data
        }).catch(e => {
          console.log(e.response.data.errors)
          this.errors = e.response.data.errors
        })
      }      
    },

    editar(livroServices_){
      this.livroServices_ = livroServices_  
    },

    // Não consegui implementar o método remover()
    //remover(livroServices_){

      //if(confirm('Deseja realmente excluir o livro?')){
      //  LivroServices.remover_(livroServices_).then({
      //    this.listar();
      //    this.errors = []
      //  }).catch(e => {
      //    this.errors = e.response.data.errors  
      //    console.log(resposta.data)
      //  })
      //}
    //}
  }
}

/*
LivroServices.add(this.livroServices_).then(resposta => {
        this.livroServices_ = {}
        alert(this.livroServices_.id, this.livroServices_.titulo, 
              this.livroServices_.autor, this.livroServices_.lido)

        console.log(resposta.data)
        this.listar_()
        //Limpando os erros da aplicação
        //this.errors = []
        // Tratando o erro com catch()
        // mostrando somente os erros desejados
        // guardando os erros em uma variável erros
      }).catch(e =>{
        console.log(e.response.data.errors)
        this.errors = e.response.data.errors
      })

              //Listando os dados
        //  listar(){
        //    LivroServices.listar_().then(resposta => {
        //      //console.log(resposta.data)
        //      this.livroServices_ = resposta.data
        //      //this.livroServices = resposta.data
        //    })
        //  },
        //console.log(resposta.data)
        // Aqui o nome livroServicesLista vai para a
        // listagem de livros abaixo do formulario

      //alert('salvo com sucesso!')
      //  console.log(resposta.data)

      //alert(this.livroServices_.id, this.livroServices_.titulo, 
      //        this.livroServices_.autor, this.livroServices_.lido)

*/

</script>

<style>
</style>
