# Resumo

* Tipagem dinâmica.

* Alto nível.

* Orientada a objetos.

* Ponto e vírgula e chaves.

## Declaração de Variáveis

### var

* Forma mais antiga de declarar variáveis.
  
* Tem escopo de função ou global (se declarada fora de uma função).

* Sofre hoisting e é inicializada(a declaração é movida para o topo do escopo, mas não a atribuição, iniciando como undefined).

### let

* Tem escopo de bloco ({}). Isso significa que a variável só existe dentro do bloco onde foi declarada.

* Sofre hoisting, mas não é inicializada, portanto, lança um erro caso seja chamada antes da declaração.

* **Devido ao fato de possuir um hoisting melhor, o let é preferível em escopo global ou de bloco.**

* **Ao reatribuir um valor dentro de um bloco para uma variável declarada globalmente com let, o valor da variável se torna global**

```
let contador = 1;

if (contador == 1) {
  contador = 2;
}

console.log(contador) // Saída: 2
```
### const

* Tem escopo de bloco ({}).
  
* Deve ser inicializada na declaração e não pode ser reatribuída.

* Usada para valores que não devem mudar (constantes).

* **Atenção: Se uma const armazena um objeto ou array, o conteúdo do objeto/array pode ser modificado, mas a variável não pode ser reatribuída para apontar para um novo objeto/array.**

```
const pessoa = {"nome": "Ana"};

pessoa.nome = João // Válido;
```

## Arrow Functions

* Forma mais utilizada de manipular funções:

```
const funcao = (a, b) => {
  return a + b;
}
```

## Iterações

### for of

* Itera sobre objetos/valores de um conjunto.

* Se for lista:

```
const numeros = [1, 2, 3, 4, 5];

for (const [indice, valor] of numeros.entries()) {
  console.log('Indice = ${indice} Valor = ${valor}'); // Para usar f string tem que ser crase
}
```

* Se for dicionário(chamado de objeto aqui):

```
const valor = {"Valores": [1, 2, 3, 4]};

for (const [chave, valor] of Object.entries(valor)) {
  console.log(chave);
  for (const v of valor) {
    console.log(v);
}
```

## Orientação a Objetos

* A classe é declarada com class, nome e chaves.

* O metódo do construtor é chamado de **constructor**.

* Os métodos não possuem tipagem ou identificação, diferentemente de funções convencionais.

* O mecanismo de acesso ao objeto específico é o **this**.

* O to string é **toString**.

* O processo de instanciar a classe é igual ao Java(const objeto = new Classe(atributos).

**Pessoa.mjs**
```
export class Pessoa {
    constructor(nome, idade, telefone) {
        this.nome = nome;
        this.idade = idade;
        this.telefone = telefone;
    }

    set_nome = (nome) => {
        this.nome = nome;
    }

    get_nome = () => {
        return this.nome;
    }

    set_idade = (idade) => {
        this.idade = idade;
    }

    get_idade = () => {
        return this.idade;
    }

    set_telefone = (telefone) => {
        this.telefone = telefone;
    }

    get_telefone = () => {
        return this.telefone;
    }

    toString = () => {
        return `Nome: ${this.nome} Idade: ${this.idade} Telefone: ${this.telefone}`
    }
}
```

**Main.mjs**
```
import { Pessoa } from './Pessoa.mjs';

const pessoa1 = new Pessoa('Antônio', 20, 999999999999);

console.log(pessoa1.get_nome());
console.log(pessoa1.get_idade());
console.log(pessoa1.get_telefone());
console.log(pessoa1.toString());
```
