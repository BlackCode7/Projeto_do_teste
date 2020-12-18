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
          <input type="number" placeholder="Id">
          <label>Nome</label>
          <input type="text" placeholder="Nome">
          <label>Autor</label>
          <input type="text" placeholder="Autor">
          <label>Lido</label>
          <input type="text" placeholder="Já leu o livros? sim / não">

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

          <tr>

            <td>Id</td>
            <td>Nome</td>
            <td>Autor</td>
            <td>Lido</td>
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

import Livro from './services/Livros'

export default {
  
  mounted(){
    Livro.listar().then(resposta => {
      console.log(resposta)
    })
  }

}

</script>

<style>

</style>
