# KMDb

Uma plataforma de avaliação/crítica de filmes.

KMDb terá um ou mais admins que ficarão responsáveis pelo cadastro dos filmes, um ou mais críticos/revisores que irão escrever avaliações para os filmes cadastrados e usuários "comuns" que poderão escrever comentários sobre os filmes.

- Admin - será responsável por criar e deletar os filmes na plataforma.
- Crítico - não poderão criar ou deletar filmes, mas sim criar as avaliações para eles.
- Usuários - podem somente adicionar quantos comentários quiserem aos

Cada crítico só poderá fazer uma crítica por filme. Caso necessário, poderão editá-las, mas nunca criar mais de uma.

## Endpoints

### Usuários

`POST /accounts/` - Rota de criação de novos usuários.

Criando um usuário "comum"

```json
// REQUEST
{
  "username": "user",
  "password": "1234",
  "first_name": "John",
  "last_name": "Wick",
  "is_superuser": false,
  "is_staff": false
}
```

```json
// RESPONSE STATUS -> HTTP 201 CREATED
{
  "id": 1,
  "username": "user",
  "first_name": "John",
  "last_name": "Wick",
  "is_superuser": false,
  "is_staff": false
}
```

Criando um Crítico

```json
// REQUEST
{
  "username": "critic",
  "password": "1234",
  "first_name": "Jacques",
  "last_name": "Aumont",
  "is_superuser": false,
  "is_staff": true
}
```

```json
// RESPONSE STATUS -> HTTP 201 CREATED
{
  "id": 2,
  "username": "critic",
  "first_name": "Jacques",
  "last_name": "Aumont",
  "is_superuser": false,
  "is_staff": true
}
```

Criando um administrador

```json
// REQUEST
{
  "username": "admin",
  "password": "1234",
  "first_name": "Jeff",
  "last_name": "Bezos",
  "is_superuser": true,
  "is_staff": true
}
```

```json
// RESPONSE STATUS -> HTTP 201 CREATED
{
  "id": 3,
  "username": "admin",
  "first_name": "Jeff",
  "last_name": "Bezos",
  "is_superuser": true,
  "is_staff": true
}
```

Caso haja a tentativa de criação de um usuário já existente, será 400 - BAD REQUEST com seguinte formato:

```json
// RESPONSE STATUS -> HTTP 400 BAD REQUEST
{
  "username": ["A user with that username already exists."]
}
```

`POST /login/` - Rota de login (deve retornar o token de acesso)

```json
// REQUEST
{
  "username": "critic",
  "password": "1234"
}
```

```json
// RESPONSE STATUS -> HTTP 200 OK
{
  "token": "dfd384673e9127213de6116ca33257ce4aa203cf"
}
```

### Movies

`POST /movies/` - Rota de criação de um novo filme na plataforma

```json
// REQUEST
// Header -> Authorization: Token <token-do-admin>
{
  "title": "O Poderoso Chefão",
  "duration": "175m",
  "genres": [{ "name": "Crime" }, { "name": "Drama" }],
  "launch": "1972-09-10",
  "classification": 14,
  "synopsis": "Don Vito Corleone (Marlon Brando) é o chefe de uma 'família' de Nova York que está feliz, pois Connie (Talia Shire), sua filha,se casou com Carlo (Gianni Russo). Por ser seu padrinho Vito foi procurar o líder da banda e ofereceu 10 mil dólares para deixar Johnny sair, mas teve o pedido recusado."
}
```

```json
// RESPONSE STATUS -> HTTP 201 CREATED

{
  "id": 1,
  "title": "O Poderoso Chefão",
  "duration": "175m",
  "genres": [
    {
      "id": 1,
      "name": "Crime"
    },
    {
      "id": 2,
      "name": "Drama"
    }
  ],
  "launch": "1972-09-10",
  "classification": 14,
  "synopsis": "Don Vito Corleone (Marlon Brando) é o chefe de uma 'família' de Nova York que está feliz, pois Connie (Talia Shire), sua filha,se casou com Carlo (Gianni Russo). Por ser seu padrinho Vito foi procurar o líder da banda e ofereceu 10 mil dólares para deixar Johnny sair, mas teve o pedido recusado.",
  "criticism_set": [],
  "comment_set": []
}
```

```json
// RESPONSE STATUS 200 OK
[
  {
    "id": 1,
    "title": "O Poderoso Chefão",
    "duration": "175m",
    "genres": [
      {
        "id": 1,
        "name": "Crime"
      },
      {
        "id": 2,
        "name": "Drama"
      }
    ],
    "launch": "1972-09-10",
    "classification": 14,
    "synopsis": "Don Vito Corleone (Marlon Brando) é o chefe de uma 'família' de Nova York que está feliz, pois Connie (Talia Shire), sua filha,se casou com Carlo (Gianni Russo). Por ser seu padrinho Vito foi procurar o líder da banda e ofereceu 10 mil dólares para deixar Johnny sair, mas teve o pedido recusado.",
    "criticism_set": [],
    "comment_set": []
  },
  {
    "id": 2,
    "title": "Um Sonho de Liberdade",
    "duration": "142m",
    "genres": [
      {
        "id": 2,
        "name": "Drama"
      },
      {
        "id": 3,
        "name": "Ficção científica"
      }
    ],
    "launch": "1994-10-14",
    "classification": 16,
    "synopsis": "Andy Dufresne é condenado a duas prisões perpétuas consecutivas pelas mortes de sua esposa e de seu amante. Porém, só Andy sabe que ele não cometeu os crimes. No presídio, durante dezenove anos, ele faz amizade com Red, sofre as brutalidades da vida na cadeia, se adapta, ajuda os carcereiros, etc."
    "criticism_set": [],
    "comment_set": []
  }
]
```

`GET /movies/` - Rota que lista todos os filmes cadastrados com base na filtragem do request

```json
// REQUEST
{
  "title": "liberdade" // Campo obrigatório
}
```

```json
// RESPONSE STATUS 200 OK
[
  {
    "id": 2,
    "title": "Um Sonho de Liberdade",
    "duration": "142m",
    "genres": [
      {
        "id": 2,
        "name": "Drama"
      },
      {
        "id": 3,
        "name": "Ficção científica"
      }
    ],
    "launch": "1994-10-14",
    "classification": 16,
    "synopsis": "Andy Dufresne é condenado a duas prisões perpétuas consecutivas pelas mortes de sua esposa e de seu amante. Porém, só Andy sabe que ele não cometeu os crimes. No presídio, durante dezenove anos, ele faz amizade com Red, sofre as brutalidades da vida na cadeia, se adapta, ajuda os carcereiros",
    "criticism_set": [],
    "comment_set": []
  },
  {
    "id": 3,
    "title": "Em busca da liberdade",
    "duration": "175m",
    "genres": [
      {
        "id": 2,
        "name": "Drama"
      },
      {
        "id": 4,
        "name": "Obra de época"
      }
    ],
    "launch": "2018-02-22",
    "classification": 14,
    "synopsis": "Representando a Grã-Bretanha,  corredor Eric Liddell (Joseph Fiennes) ganha uma medalha de ouro nas Olimpíadas de Paris em 1924.  Ele decide ir até a China para trabalhar como missionário e acaba encontrando um país em guerra. Com a invasão japonesa no território chinês durante a Segunda Guerra Mundial, Liddell acaba em um campo de concentração.",
    "criticism_set": [],
    "comment_set": []
  }
]
```

`GET /movies/<int: movie_id>/` - Rota que busca o filme especificado pelo id

```json
// RESPONSE STATUS -> HTTP 200 OK
{
  "id": 9,
  "title": "Nomadland",
  "duration": "110m",
  "genres": [
    {
      "id": 2,
      "name": "Drama"
    },
    {
      "id": 4,
      "name": "Obra de época"
    }
  ],
  "launch": "2021-04-15",
  "classification": 14,
  "synopsis": "Uma mulher na casa dos 60 anos que, depois de perder tudo na Grande
  Recessão, embarca em uma viagem pelo Oeste americano, vivendo como uma nômade
	moderna.",
  "criticism_set": [
    {
      "id": 39,
      "critic": {
        "id": 2,
	"first_name": "Jacques",
	"last_name": "Aumont",
    },
  "stars": 8,
  "review": "Nomadland apresenta, portanto, fortes credenciais para ser favorito ao Oscar 2021 e Chloé Zhao tem a chance de fazer história como a segunda mulher (apenas) a vencer o maior prêmio do cinema como diretora. Filme com cara de premiação, mas, ainda assim, com mensagens importantes para todos.",
  "spoilers": false
	},
	...
	],
  "comment_set": [
    {
        "id": 11,
        "user": {
            "id": 1,
            "first_name": "John",
            "last_name": "Wick"
        },
        "comment": "Lindo, nos faz refletir sobre a vida, os anos, envelhecer. Vale a pena assistir"
  },
	...
]
```

`DELETE /movies/<int:movie_id>/`- Rota que deleta filmes

`POST /movies/<int:movie_id>/review/` - Rota de criação de um review de um crítico

```json
// REQUEST
// Header -> Authorization: Token <token-de-critic>
{
  "stars": 7,
  "review": "Nomadland podia ter dado muito errado. Podia ser dramático demais, monótono demais ou opaco demais. Felizmente, o que vemos é algo singelo, pois a direção de Zhao (que também edita, assina e produz o longa) não ignora a frieza da realidade, mas sabe encontrar a magia da naturalidade. Sim, rimei sem querer e parece meio poético, mas é assim que o filme funciona mesmo. Viva Chloé Zhao - para sempre! Logo, os holofotes voltaram para esta obra independente da cineasta que, sinceramente, merece toda a atenção que recebeu.",
  "spoiler": false,
}
// RESPONSE STATUS 201 CREATED
{
  "id": 39,
  "critic": {
    "id": 2,
    "first_name": "Jacques",
    "last_name": "Aumont"
    },
  "stars": 7,
  "review": "Nomadland podia ter dado muito errado. Podia ser dramático demais, monótono demais ou opaco demais. Felizmente, o que vemos é algo singelo, pois a direção de Zhao (que também edita, assina e produz o longa) não ignora a frieza da realidade, mas sabe encontrar a magia da naturalidade. Sim, rimei sem querer e parece meio poético, mas é assim que o filme funciona mesmo. Viva Chloé Zhao - para sempre! Logo, os holofotes voltaram para esta obra independente da cineasta que, sinceramente, merece toda a atenção que recebeu.",
  "spoilers": false
}
```

`PUT /movies/<int:movie_id>/review/` - Rota que altera uma crítica já realizada

```json
// REQUEST
// Header -> Authorization: Token <token-do-critic>
// Todos os campos são obrigatórios
{
  "stars": 8,
  "review": "Nomadland apresenta, portanto, fortes credenciais para ser favorito ao Oscar 2021 e Chloé Zhao tem a chance de fazer história como a segunda mulher (apenas) a vencer o maior prêmio do cinema como diretora. Filme com cara de premiação, mas, ainda assim, com mensagens importantes para todos.",
  "spoilers": false
}
//RESPONSE
{
  "id": 39,
  "critic": {
    "id": 2,
    "first_name": "Jacques",
    "last_name": "Aumont"
    },
  "stars": 8,
  "review": "Nomadland apresenta, portanto, fortes credenciais para ser favorito ao Oscar 2021 e Chloé Zhao tem a chance de fazer história como a segunda mulher (apenas) a vencer o maior prêmio do cinema como diretora. Filme com cara de premiação, mas, ainda assim, com mensagens importantes para todos.",
  "spoilers": false
}
```

`POST /movies/<int:movie_id>/comments/` - Rota que o Usuário faz um comentário

```json
// REQUEST
// Header -> Authorization: Token <token-do-user>
{
  "comment": "Lindo filme. Com certeza assistam."
}
```

```json
// RESPONSE STATUS -> HTTP 201 CREATED
{
  "id": 1,
  "user": {
    "id": 1,
    "first_name": "John",
    "last_name": "Wick"
  },
  "comment": "Lindo filme. Com certeza assistam."
}
```

`PUT /movies/<int:movie_id>/comments/` - Rota que altera um comentário realizado

```json
// REQUEST
// Header -> Authorization: Token <token-do-user>
{
  "comment_id": 1,
  "comment": "Lindo, nos faz refletir sobre a vida, os anos, envelhecer. Vale a pena assistir"
}
```

```json
// RESPONSE STATUS 200 OK

{
  "id": 11,
  "user": {
    "id": 1,
    "first_name": "John",
    "last_name": "Wick"
  },
  "comment": "Lindo, nos faz refletir sobre a vida, os anos, envelhecer. Vale a pena assistir"
}
```
