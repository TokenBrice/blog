---
title: "Viva la lucha libre (y verificable onchain)"
description: "Un artículo-tésis donde explico el porqué de mi amor por luchadores y lo que espero de ellos"
date: '2021-10-04T01:13:50.191Z'
categories: [🃏 NFT]
tags: [Coleccionables, Tokens Non Fongibles, NFT, Compra de NFT, Mercado NFT, Rendimientos NFT, NFT comunitario, Chainlink VRF, Resiliencia NFT, NFT y Arte]
toc: true
tocNum: false
url: luchadores-nft
---

Este artículo va a ser más personal de lo que acostumbro, pero en vista del tema no podía ser diferente. Nos interesaremos en un proyecto con el que estoy muy involucrado: Los Luchadores. Se trata de luchadores totalmente onchain, que pronto serán personajes en un futuro juego, también onchain.

Más que el proyecto en sí, le explicaré la tésis que estoy desarrollando sobre ese tema. Creo que este enfoque puede ser interesante y ayudarle a construir sus convicciones personales sobre otro tipo de colecciones.

En este artículo, no explico los mecanismos de los Luchadores o del juego asociado a venir. No dude en leer  [el libro blanco disponible en inglés](https://whitepaper.luchadores.io) para mayor información sobre el tema.

![luchadores-cover](/img/2021/luchadores-nft/luchadores-cover.png)

---

## 📑 Mi tésis sobre los Luchadores

Si no es de los mejores informados sobre los NFTs y mis actividades en el tema, no dude en ir a echarle un vistazo a la [página de introducción](https://tokenbrice.xyz/nft/).

Mi interés y mi entusiasmo por los Luchadores están en cuatro razones principales, así que, vayamos al grano:


### 🔮 Un proceso de creación innovante e inclusivo

La creación de Luchadores fue un proceso completamente onchain gracias a la utilización de la VRF de Chainlink. Esto permite **generar cantidades aleatorias de forma verificable**. Gracias a esta tecnología, el minaje de un Luchador se realizó con la garantía de que no había ningún tipo de manipulación posible, y la prueba de cálculo está disponible.

Fue esta dimensión técnica innovante que me permitió identificar este proyecto. Limitado a un **número total de 10 000 Luchadores**, el minaje estuvo disponible durante **3 meses** (Mayo->Agosto de 2021), con un poco de exaltación en los últimos días.

El largo período del minaje permitió a todo aquel que quisiera, poder participar, con tiempo de sobra para obtener unos costos de transacción más adecuados si así lo hubiesen deseado.

La generación se hacía por el precio de 2 LINK (costos necesarios para el sistema VRF), pagados en ETH + el precio del gas. En función del precio de LINK y de los costos de la transacción en la red, los mineros han pagado entre 0.015 y 0.025 ETH por Luchador.

La generación aleatoria verificable dió lugar a algunas "curiosidades" bastantes divertidas en los Luchadores:

![luchadores-distribution](/img/2021/luchadores-nft/luchadores-distribution.png "Tabla de ocurrencia por atributos de Luchadores")

La distribución de la rareza fue una curba normal: hay más de 8000 Luchadores (81,3%) en el grupo de 3, 2 o 4 atributos, los más comúnes. Entre más nos acercamos a los extremos, más raro se hacen los Luchadores.

 |Común (3, 2, 4)|Raro (1, 5)|Épico (6, 0)|Legendario (7)
:--|:--|:--|:--|:--
**Cantidad Generada**|8130|1654|205|11
**Porcentaje**|81.30%|16.54%|2.05%|0.11%

* Pudo haber un Luchador con 8 atributos, pero no fue así. Y muy probablemente hubiese existido uno sólo: así que ningún dios Lucha.
* En ocasiones, el atributo "bigotes" se generó en un Luchador en el que su color de piel se parece mucho al del bigote, lo que creó un **[bigote oculto](https://luchadores.io/luchador/8085)**. Estos Luchadores son objeto de una atención particular.

![luchadores-hidden_mustache_difference](/img/2021/luchadores-nft/hidden_mustache_difference.png "Una diferencia sutil pero significativa")

### ⛓ EL enfoque onchain

Además de la generación totalmente onchain, el visual de Luchadores está en un formato optimizado (svg) que permite **conservarlo directamente en la cadena Ethereum**, proporcionando así una importante resistencia a los elementos asociados a cada NFT.

Esto no termina aquí porque el juego que viene, del que discutiremos más adelante, se basará igualmente en los **mecanismos de generación verificable**. Así, en la arena,  los golpes vitales o las escabullidas serán el fruto de un azar verificable y muy difícil de manipular.

![luchadores-art-for-all](/img/2021/luchadores-nft/AFA-score.png "Los proyectos mejor notados en ArtForAll")


No soy el único a remarcar este enfoque de resistencia, que de igual manera ha llamado la atención de Link marines. Luchadores es también el único proyecto 100/100 con Avastars en [ArtForAll, un servicio que evalúa la resiliencia de los NFTs](https://artforall.io/score?search=).

De esta manera, se podría describir el proyecto como "onchain maximalista" pero no es el caso: compromisos, desgraciadamente necesarios, se plantean en el nivel en el que es posible permitirlos: los sorteos aleatorios relacionados con el juego, serán realizados en una sidechain (Polygon) o rollup. Esto permitirá **mantener el juego accesible y poco costoso**, aprovechando al máximo las garantías del NFT, que siempre está listo en la cadena de Ethereum. 


### 🎮 El juego de Luchadores

El juego en sí toca mi fibra nostálgica, no hay duda. De hecho, la lucha se realizará **por turnos**, con un sistema de atributos (estadísticos), habilidades pasivas y habilidades de activación.

![luchadores-stats](/img/2021/luchadores-nft/luchadores-stats.png "Los atributos serán determinantes en la arena")

Lo dejo documentarse sobre el impacto de los atributos y de las habilidades, pero como fan de los juegos por turnos, de estrategias y de RPG, puedo decirle que estoy preparado para reflexionar 🧙 

![luchadores-arena](/img/2021/luchadores-nft/final-lucha-arena.png "También se prevén las batallas por equipos")

**Un token asociado** (LUCHA) se puede ganar en el juego. También será distribuido entre los poseedores del NFT Luchadores durante el primer año. El token se utilizará de diferentes maneras en el juego (respeto, sistema de prodigio, renombrarlos?) y también se puede **estaquear para ganar MASK**, un token no transferible (↪ sólamente in-game), útiles para equipar sus Luchadores.


### 📜 La comunidad y su historia

El juego ha sido desarrollado por una sóla persona, Luchador, a quien se le han venido sumando progresivamente otros perfiles necesarios para el desarrollo:

* Desde el principio, otros miembros de la comunidad han surgido como Teh_Griz y LuchaBroy: convirtiéndose en los primeros moderadores en Discord.
* Yo me fui involucrando poco a poco, para ayudar a hacer conocer el proyecto, desarrollar la comunidad francófona y proponer mi saber donde es más pertinente, más información más adelante.
* Un diseñador de juegos y dos pixel artists ([AbueloRetroWave](https://www.instagram.com/AbueloRetroWave/) & [m3r0j](https://www.artstation.com/m3r0j))

Por el momento sólo hablamos de implicaciones formales. Pero no se puede olvidar todas las iniciativas de la comunidad. Es imposible nombrarlas todas pero citaré por lo menos algunos:

* Nicosz quien ha desarrollado una [herramienta en Phyton para analizar los datos relacionados a los Luchadores](https://github.com/sznicolas/luchadata).
* Un [dashboard para seguir los principales métricos de los Luchadores](https://dune.xyz/lokhidor/Luchadores), propuesto por cnhkp.eth, gracias a Dune Analytics y a la ayuda de Nicosz.
* O también OxMule quien ha [traducido el whitepaper](https://whitepaper.luchadores.io/v/francais/) en unos cuantos días. 
* Sin olvidar los numerosos coleccionistas y "francotiradores" de Discord quienes lo animan cada día, como Chainlinkers, uno de los primeros miembros de la comunidad quien se ganó dos sorteos el día de su cumpleaños convirtiéndose en una leyenda.

---

## 🐒 Mi participación

Descubrí los Luchadores en Mayo, he minado unos 80 y seguí el proyecto muy pasivamente al principio. En Junio, cuando la popularidad comenzó a hacerse más palpable, me impliqué más activamente, al principio como moderador en la comunidad francófona y luego como administrador del servidor Discord.

Veo mi implicación en el proyecto como una oportunidad para enseñar sobre las dimensiones de los NFTs. No escogí este proyecto al azar: considero que el enfoque SVG onchain utilizado por los Luchadores está entre los más creíbles, a pesar de su contraste gráfico (-> style pixel).

Concretamente, animo la comunidad con diferentes sorteos y ayudo a hacer conocer los Luchadores.


### 🃏 Mis Luchadores

No tuve mucha suerte en el minaje de mis Luchadores, pero la he recompensado a través de mis adquisiciones. Si bien es cierto que la mayoría corresponden a una limpieza mecánica del precio piso, sobre todo entre los 0,025 y 0,035 ETH, también he adquirido algunos Luchadores con más rarezas entre los cuales 3 de 7 atributos.

Mi mejor pesca ha sido la de "Batman", uno de 7 atributos quien será uno de mis principales combatientes en la arena :

#### ⭐ Lucha 7 atributos #8956

![luchadores-8956](/img/2021/luchadores-nft/luchadores-8956.png "Un Luchador 7 atributos, a ganar en la arena")

Ahora tengo en posesión 3 Luchadores de 7 atributos, **quiero poner en juego uno**. Este no se irá con quien ofrezca más, no.

**EL [Luchador #8956](https://luchadores.io/luchador/8956) se lo ganaran en la arena**, y se irá etonces con el jugador más habilidoso. Me muero por compartirles más detalles sobre el mecanismo de atribución cuando el juego esté disponible.


#### 🎁 Las donaciones

He minado alrededor de 80 Luchadores, y comprado más de 150 en OpenSea.

Pienso utilizar una buena parte como "presupuesto promocional" para los Luchadores - lo que ya es el caso. Varias distribuciones han tenido lugar, y he regalado unos 50, de entre los cuales 25 a los top farmers de blé de DeFi France.

Por lo demás, como yo soy fan del concepto de "ir a muerte" (implicación directa con consecuencias), y visto mi compromiso con el proyecto, no lo veo de otra manera. No tengo Luchadores en otras carteras, los guardo todos en [mon ENS por transparencia.](https://opensea.io/tokenbrice?search[sortBy]=LISTING_DATE&search[query]=luchadores)

---

## 📈 El valor de un luchador

{{< notice warning >}}

⚠ Este artículo no es un consejo de inversión. Escoger cuando y que jpeg/svg adquirir es una elección personal.

{{< /notice >}}

Al principio los Luchaodres se intercambiaban a un costo apróximado del precio de minaje, antes de establecerse un precio piso de alrededor 0.03 ETH. Después, al final de septiembre, con la llegada del whitepaper, la tendencia es palpable y se refleja en el floor (precio piso), alrededor de 0.07 ETH últimamete.

Un luchador, sí, pero a que precio? No espere una respuesta directa de mi parte a esta pregunta. Al día de hoy y en la etapa de desarrollo que está, sigue siendo una apuesta. Sin embargo el enfoque es pertinente y pienso que los Luchadores tienen con que entrar a ser parte de los galardonados de los NFTs, yendo más lejos de las fronteras de la interactividad, hecha posible gracias a estos objetos numéricos.

Adquirir hoy en día un Luchador implica pagar mínimo 3 veces lo que costaba hace unas semanas - por lo tanto sería un buen negocio si la tendencia continúa 🔮 : bienvenido al mundo de los NFTs, donde el precio es un mecanismo social y altamente reflexivo. 

En esto, es hacer sus apuestas, nada vale más 🎲. 

---

{{< notice note >}}

_Apenas toco el tema en el blog porque quería tomarme mi tiempo para bien organizar mis reflexiones. Para quienes me siguen en vivo o en Twitter me han escuchado hablar del proyecto desde Mayo y han podido minar directamente, si lo hubieran querido._

{{< /notice >}}

Espero que este artículo le haya permitido entender lo que me fascina de una colección de luchadores, y en general de cómo analizo una colección, y que también le ayude a evaluar otras.

*🙏 Gracias a [DFr3sh](https://twitter.com/DFr3sh2) por la traducción de este artículo al español*