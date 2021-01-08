<template>
  <div id="app">

    <nav>
      <div class="nav-wrapper blue darken-1">
        <a href="#" class="brand-logo center">Cadastro Livros</a>
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
          <input v-model="livro.lido" type="text" placeholder="JÃ¡ leu o livros? sim / nÃ£o">

          <button @submit.prevent.stop="salvar()" class="waves-effect waves-light btn-small">Salvar<i class="material-icons left">save</i></button>

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
            <!--{{ livro1.id }}-->
            <td>ID</td>
            <td>LIVRO</td>
            <td>AUTOR</td>
            <td>LIDO</td>
            <td>
              <!--@click.prevent.stop="editar(livro)"-->
              <button  class="waves-effect btn-small blue darken-1"><i class="material-icons">create</i></button>
              <!--@click.prevent.stop="remover(livro)"-->
              <button  class="waves-effect btn-small red darken-1"><i class="material-icons">delete</i></button>
            </td>
          </tr>
        </tbody>
      
      </table>

    </div>

  </div>
</template>

<script>
//import Livros from '../services/Livros'
export default {    
  
}

</script>