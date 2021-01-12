<template>
  
</template>

<script>
//mudei o nome do import pra poder diferenciar
//import componenteLivro from './components/livros'
import LivroService from './services/livrosServices'

export default {

  data() {
    return {
      // Referencia ao LivroService no mounted
      livroservice: null
    }     
  },
  mounted() {
    LivroService.listar().then(resposta => {
      console.log(resposta.data)
      //pegando livroservices de data(){} para receber
      //o resposta.data
      this.livroservice = resposta.data
    })    
  }    
}

</script>

<style>
</style>

