---
title: "La historia de BadgerDAO: una introducción via DIGG"
description: "BadgerDAO está en la primera línea de dos temas  que son tendencia: la gestión de activos en DeFi (valts/setts) & BTC en Ethereum. Véamos que implica este proyecto y cual es su plan."
date: '2021-01-30T01:13:50.191Z'
categories: [🌌 DeFi, 🔮 Découverte]
tags: [DeFi, Ethereum, Finanzas descentralizadas, Badger, BadgerDAO, DIGG, monedas elásticas, wBTC, renBTC, Curve BTC pools, gitcoin, Meme, vault, setts, farming, liquidity providing, LP, BTC, BTC en Ethereun, plataformización de DeFi]
toc: true
tocNum: true
url: badger-digg
---

A pesar de su reciente lanzamiento de apenas algunas semanas, BadgerDAO se ha transformado un una central DeFI **acogiendo alrededor de >1.2 billones de dólares en activos**. Sin importar que he mencionado Badger en otros artículos en el pasado, creo que es tiempo de consacrarle un artículo a DIGG, sin olvidar su contexto.

![badgerdao-story-tkb-cover](/img/2021/badger-digg/cover.png/)

## Introducción a Badger DAO

BadgerDAO es un proyecto comunitario con una proposición de valor clara: ayudar **a construir la infraestructura necesaria para integrar BTC en DeFi**. Esta visisón fundamental se manifiesta a través de todos sus productos, todos centrados alrededor de la representación de BTC en Ethereum como wBTC o sBTC y los tokens nativos - BADGER y ahora DIGG.

### Una proposición de valor clara: Optimización de BTC en Ethereum

La primera capa de esta cebolla es bastante sencilla: Badger ofrece un servicio tipo Yearn parar los BTC en Ethereum: los usuarios pueden depósitar sus tokens representativos de una posición en un pool de BTC Curve para ganar BADGER & DIGG además de la APY nativa.

![badger-stats](/img/2021/badger-digg/badger-stats.png/ "Resume de los principales indicadores de Badger con Sett.Vision")

También existen bóvedas (llamadas "setts") para los mismos BADGER & DIGG, como también para sus respectivos tokens LP en Uniswap y Sushiswap.

{{< notice tip >}}
Las bóvedas como las de Yearn son inspiradas del diseño de aTokens de Aave: al prinicpio, desde que el cofre es abierto, la correlación entre el activo base y el token de la bóveda ese 1:1. A medida que la bóveda acumula otros tokens suplementarios gracias a sus cosechas, su token representa cada vez más el activo subyacente.
{{< /notice >}}

Esta propoisición de valor no es nueva en si y pudo haber sido propuesta directamente por Yearn. Lo que hace a Badger especial, es **la forma como el equipo aborda la construcción del producto y toda la visión subyacente detrás de este.**

### Un enfoque comunitario

Desde el principio, la comunidad ha sido el centro de Badger. Es claramente remarcable viendo la distribución del token [^1]:

![Resume de la distribución de badger](/img/2021/badger-digg/badger-breakdown.png/ "Resume de la distribución inicial del token BADGER")

![Resume de la distribución de digg](/img/2021/badger-digg/digg-breakdown.png/ "Resume de la distribución inicial del token DIGG")

En efecto, las dos partes más grandes del total circulante han sido asignadas al programa de liquidity mining - recompensando los usuarios del protocolo como también a la tesorería de la DAO encargada de estructurar las operaciones a largo plazo y del crecimiento del protocolo.

Los airdrops, como las bóvedas, han creado un espiral bastante atractivo para los destinatarios: a diferencia del airdrop de UNI donde la opción era simplemente vender o esperar, con BADGER & DIGG, las persons **que creían en el protocolo desde el principio tenían la posibilidad de implicarse a través de las bóvedas gracias a los tokens recibidos.**

El airdrop inicial de BADGER reconcocía las acciones principales relacionadas con BTC en Ethereum, así como los donadores de gitcoin. El segundo airdrop (DIGG) recompensó las interacciones con el ecosistema de Badge en sí.

Además del impulso creado por el lanzamiento y la distribución inicial, la comunidad pudo mantenerlo gracias a un espíritu de Meme floreciente: una distribución de NFT fue organizada en Meme[^2], disponibles para los depositantes en el sett bBADGER o el sett wBTC/BADGER de Uniswap.

En total, había 6 diferentes NFTs disponibles y el primero en coleccionarlos podía reclamar una prima BADGER. El hecho de poseerlos o de cultivar esos NFTs era reconocible por la distribución inicial de DIGG y su inclusión en Badge como multiplicador de rendimiento, lo que aún está en curso de discusión.

![un NFT Meme-Badger](/img/2021/badger-digg/badger-nft-satoshi.gif/ "Uno de los 6 Badger x Meme NFTs - Satoshi")

{{< notice tip >}}
Si es optimista del curso del token a corto plazo, generalmente es una mala idea de entrar en una posición 50/50 proveyendo liquidez sobre este, sobretodo si espera a que el otro activo del par (ETH, stablecoin o en este caso wBTC) se mantenga relativamente estable en el mismo período. Si teme que este escenario se produzca con BADGER o DIGG, puede simplemente depósitar en las cajas fuertes de BADGER o de DIGGS (no hay riesgo de perdida inpermanente).
{{< /notice >}}

---

## Entonces, DIGG ?

DIGG es la segunda gran etapa del proyecto DAO de Badge: un nuevo tipo de representación de BTC en Ethereum. A diferencia del wBTC o del renBTC, **DIGG no es respladado por un stock de BTC**. Utiliza un mecanismo de reajuste iniciado por Ampleforth para tratar de entregar en el tiempo un activo que siga el curso del BTC.

Antes de sumergirnos en el funcionamiento del DIGG, hablemos rápidamente del pre y post lanzamiento.

### Wen DIGG?

El lanzamiento del DIGG era un acontecimiento bastante esperado. A pesar que desde afuera, parecía que se tomaba más tiempo del previsto, lo que se pasaba al interior era fascinante: la **comunidad inicial de Badge participó activamente en las deicisiones claves de DIGG.**

Después de las discusiones al seno de la comunidad, se decidió comenzar con una oferta de lanzamiento relativamente baja (4000) para permitir realizar una **prueba de stress al mecanismo de reajuste desde el inicio**. los reajustes igualmente empezaron desde el inicio - 24h después del lanzamiento del token.

![wen-digg](/img/2021/badger-digg/wen-digg.jpeg/ "Wen DIGG meme contest")

Badger siendo Badger, la máquina de publicidad estaba, por supuesto, en el punto con un "Wen DIGG?" para asegurarse de que todo el mundo estuviera al tanto.

Ahora sin tanto esperar, metámosnos en el centro del tema: los reajustes.

### Los reajustes

El DIGG es lo que llamamos una "moneda elástica", como lo ha iniciado Ampleforth. Esto significa que la oferta principal de DIGG no ha sido fijada, pero fluctúa diariamente en función del precio promedio ponderado en el tiempo de DIGG con respecto a su anclaje - el BTC.

Entre más el DIGG está "por fuera de su perímetro", lo que significa que su precio es superior al precio de BTC, más la oferta de DIGG es diluída, el DIGG suplementraio producido se distribuye proporcionalmente entre sus poseedores - pasa lo mismo en el otro sentido: contracción si el precio es inferior al anclaje.

Al igual que el APML, con DIGG, todos los poseedores (incluyendo los tokens de los pools de liquidez) son afectados por los reajustes, que sea positivo a negativo. Sin embargo, con el DIGG, al igual que con los tokens de señoreaje, existe **un mecanismo para abstraer los reajustes con el objetivo de permitir una mejor composabilidad dentro de DeFI: es bDIGG**, lo discutiremos luego.

Los reajustes se hace a una hora fija, para DIGG es a las 15h EST, a las 21H para mis queridos lectores franceses.

{{< notice tip >}}
Los tokens de reajustes explotan mecanismos similares a los de los stablecoins algorítmicos / tokens de señoreaje, así que no dude en leer mi **[precedente tiquete sobre el tema]({{< relref path="/content/posts/2021/seigniorage-basis-vs-esd.fr.md" >}})** para más información.
{{< /notice >}}

Por ejemplo, después del primer día, el reajuste genesis fue positivo y lanzó una producción y una redistribución de alrededor del 12% de la oferta inicial. Varios reajustes positivos siguieron.

Por el moment, el mecanismo de reajustes es bastante simple, pero podría estar mejor alineado con los incentivos del conjunto en el futuro para ayudar a DIGG a mantener su anclaje.

<div align = "center">

{{< tweet 1354963274387886090 >}}

</div>


### Próxima etapa para los Setts

Con el lanzamiento de DIGG, la próxima gran etapa de Badger, como protocolo, es comenzar a **incrementar su eficacia en términos de capital**: para decirlo más simplemente, permitir a sus usuarios de **hacer préstamos a partir de sus posiciones en los setts**.

Para ser más claro (extrapolando un poco): imágine el Badger actual, teniendo una función suplementaria que le permita minar DAIs a partir de sus setts como ya se hace con ETH en Maker. No lo haría?

De hecho, los setts constituirían un colateral claramente apreciable, dado que toman valor a partir del activo base. Así pues, los setts BTC por ejemplo, podrían ser igual de seguros que sus activos subyacentes (ej wBTC), teniendo en cuenta los riesgos suplementarios relacionados al hecho que el activo subyacente está en posición de aprovisionador de liquidez.

En todo caso, antes de tener un mercado nativo de préstamos en Badger, me espero a ver diferentes **tokens y setts relacionados a Badger aceptados como colateral** en otras plataformas de préstamos.

Desde este punto de vista, me gustaría captar su atención sobre el bDIGG en particular. a pesar de que representa una posición 100% del DIGG que se reajusta, **bDIGG en sí no se reajusta**. Es como una capa de abstracción construída sobre el DIGG, un sello de reajustes entre otras cosas. Lo que facilita su integración en otros protocolos, y me espero a ver un día una gran gama de soportes para DIGG.
  
---

## El fin del juego para BadgerDAO & DeFi

El fin de la partida para Badger sería como el descrito anteriormente, con un ecosistema completo alrededor de CLAW o como se llame. [^3] Badger se volvería cada vez más en un servicio tipo Synthetix donde los poseedores se verán proponer diferentes opciones de participación más o menos activas en el ecosistema, con recompensas apropriadas.

Como servicios como Badger integran elementos del mercado monetario como el préstamos, **aumentan la eficacia del capital para sus usuarios**. Lo que antes una representación de BTC producía 20% de APY es ahora lo mismo + poder pedir prestada una parte de su valor en stablecoins para aumentar aún más la rentabilidad, si se ajusta a su apetito por el riesgo.

Esta lógica es más grande que Badger, como se ve en otras plataformas, lo podríamos llamar la **"plataformización de DeFi"**. Yearn propone algo similar con el Iron Bank, donde ciertos servicios podrán prestar con una garantía insuficiente, lo que creará una brecha de eficiencia para los afortunados que sean elegibles.

Además, para volver a Badger, la adopción de un modelo parecido, podría significar otros ingresos nativos y durables que podrían estar relacionados al token BADGER o a su sett. Si se considera que la mayoría de los rendimientos provienen actualmente de las incentivos de los aportes de liquidez, sería bastante sinérgico el sacarle partido.

Teniendo en cuenta **[el exito del modelo de Curve / CRV]({{< relref path="/content/posts/2021/dex-value-capture.fr.md" >}})**, es lógico de ver cada vez más protocolos adoptar estos elementos: lo principal de dar a sus poseedores la posibilidad de comprometer sus tokens por participar en la gubernanza, aprevechar los flujos de los ingresos de la plataforma y aumentar sus propios beneficios por el uso del servicio.


_🙏 Muchas gracias a HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony por su cuidadosa lectura de la edición francesa de este artículo y su traducción al inglés._

{{< notice tip >}}

Este artículo despertó su curiosidad? Ha caído en el buen lugar - Tenemos un ecosistema dinámico en francés para ayudarle a seguir y a comprender la finanza descentralizada. De lo más accesible a lo más especializado :
1. **[💬 El servidor Discord DeFi France](https://discord.gg/3bWZcK2)** para intercambiar con la comunidad.
2. **[☕ La versión françesa del Daily Gwei](https://thedailygweifr.substack.com/)** para artículos resumidos muy accesibles.
3. **[🗞 La newsletter BanklessFR](https://banklessfr.substack.com/)** para entender los conceptos fundamentales.
4. **[🎥 El canal Youtube DeFi France](https://www.youtube.com/channel/UCefQC4Y-X9MBRuYBKc2waiQ)** para profundizar con los lives más avanzados.
5. & Bien claro [este blog](/fr/) que profundiza en temas específicos relacionados con la práctica de la DeFi.

{{< /notice >}}

---

## Notas & Referencias

[^1]: Lo gráficos provienen de [Badger's DAO liquidity mining launch announcement](https://badgerdao.medium.com/badger-dao-liquidity-mining-launch-b2415301bd31#:~:text=Tokens%20distributed%3A%20%24BADGER%20and%20%24,2nd%20product%20of%20the%20DAO.).
[^2]: **[Meme](https://dontbuymeme.com/collections/badger)** es un mecanismo de distribución de NFT donde los usuarios ponen en juego un token dterminado  (en nuestro caso bBADGER) para ganar puntos - las piñas. Después pueden cambiar las piñas por el NFT de su elección.
[^3]: Esto no es la especulación pura - BadgerDAO ya considera como utilizar las [sinergias con UMA y Sushiswap para este hecho](https://twitter.com/spadaboom1/status/1354826775801561091?s=20).
