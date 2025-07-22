---
title: "⚔ La Guerra de CRV: entender la carrera de acumulación de capacidad para influenciar el protocolo Curve Finance"
description: "Una guía concisa para seguir la contienda de acumulación de CRV por todos los medios posibles, incluyendo la compra de votos (bribes), y para evalaur las estrategias de Curve en los protocolos DeFi"
date: '2022-04-06T01:13:50.191Z'
categories: [🌌 DeFi, ⚙ Comprender]
tags: [DeFi, Ethereum, Finanzas Descentrlizadas, Curve Finance, CRV, Polygon, Convex, CVX, Votium, vlCVX, veCRV, bribe.crv]
toc: true
tocNum: true
url: crv-wars
---

Desde sus primeros días y desde el lanzamiento del token CRV, se espera, se proyecta y se presume sobre lo que la guerra de CRV podría traer. Ahora con el lanzamiento de Convex, después el de Bribe.crv y finalmente el de Votium, todo se acelera: ahora se pueden comprar los votos VeCRV! Véamos cómo todo esto imapacta Curve y la DeFi en su globalidad.

![curve-wars-cover-tokenbrice](/img/2021/crv-wars/curve-wars-cover-tokenbrice.png)

A primera vista, la pregunta es simple y directa:

1. Curve es el exchange descentralizado más grande de la DeFi en términos de valor total depositado.
2. El token CRV te permite 1/ una parte de los fletes recolectados 2/ **un derecho de voto para influenciar las futuras emisiones de CRV.**
3. => Tener el control de una gran capacidad de voto VeCRV hace que sea **mucho más fácil el desarrollo de un pool Curve**, porque te permite la posibilidad de votar por grandes rendimientos CRV del pool en cuestión.

Sin embargo como siempre en DeFi, nada es tan simple y el diablo está en los detalles. Para entender los enjuegos de la guerra del CRV, es necesario **haber entendido bien los diferentes dispositivos construidos en el**. Lo que le permitirá juzgar la pertinencia de las estrategias dispuestas por los diferentes proyectos que buscan influenciar Curve.


## Convex y la distinción de VeCRV

Antes de entrar en el campo de batalla - es decir, las diferentes aplicaciones utilizadas en esta guerra de CRV, es necesario profundizar en uno en particular: Convex. Ya he discutido sobre el en este blog, explicando [la dimensión flywheel de Convex con el CvxCRV](https://tokenbrice.xyz/content/posts/2021/defi-flywheel.fr.md).

Las interacciones de Convex con Curve van mucho más allá del CvxCRV que no es sino un elemento.

De hecho, **podríamos describir Convex como una división entre la gubernanza y las rentabilidad de VeCRV** ampliando cada uno de los elementos de un token a parte, me explico:
  

### CvxCRV = VeCRV-Rendimiento++

CvxCRV corresponde a un VeCRV propiedad de Convex. Son bloqueados para siempre, pero la liquidez en CvxCRV/CRV permite a sus depositantes de saldar sus posiciones.

**En terminos de gubernanza, CvxCRV pierde todas sus capacidades**. De hecho, Un titular de VeCRV puede votar en las emisiones (de CRV) y elecciones de gubernanza. Un titular de CvxCRV no tiene otro beneficio que los rendimientos.

No obstante, **el rendimiento se incrementa en comparación a una simple posesión de VeCRV**:

1. Rendimiento del token 3pool - la parte de fletes colectados en Curve - exactamente como VeCRV
2. Rendimiento en CRV (10% de todos los tokens cultivados por Convex, distribuídos entre todos los depositantes CvxCRV)
3. Rendimiento en CVX casi al equivalente
4. Potenciales airdrops como Ellipsis

Así, CvxCRV corresponde a un simple compromiso con respecto a VeCRV: las capacidades de gubernanza se pierden (-> vlCVX), en contrapartida el rendimiento es considerablemente ampliado y diversificado.

### vlCVX = VeCRV-gob++

En el otro extremo, Convex propone otra interesante abstracción de Curve. Se trata de su token nativo CVX. En efecto, **cada CVX corresponde a un poder de voto de VeCRV** (que proviene de CvxCRV).

Para mobilisarlo, el depositante debe "vote lock" sus CVX en vlCVX. Dejándolos bloqueados por 16 semanas y 3 días tienen acceso a un poder de gubernanza. A la hora actual, el vlCVX es de lejos el camino más eficaz económicamente hablando para acumular poder de voto en Curve:


<table>
  <tr>
   <td>
   </td>
   <td>Precio
   </td>
   <td>Poder de voto
   </td>
   <td>VeCRV-voto/$
   </td>
   <td>Compromiso
   </td>
  </tr>
  <tr>
   <td>VeCRV
   </td>
   <td>$2.42
   </td>
   <td>1 veCRV
   </td>
   <td>0.41
   </td>
   <td>4 años
   </td>
  </tr>
  <tr>
   <td>vlCVX
   </td>
   <td>$8.2
   </td>
   <td>12,75 VeCRV
   </td>
   <td>1.55
   </td>
   <td>16 semanas + 3 días
   </td>
  </tr>
</table>


A parte de la importante rentabilidad de CVX para influenciar Curve, el compromiso también es menor que en VeCRV. Para el cuadro comparativo, he partido del hecho de un bloqueo de 4 años en CRV. La diferencia está a favor de vlCVX con compromisos menos largos.
  
{{< notice warning >}}
El vlCVX tiene un inconveniente a pesar de todo: al cabo de las 16 semanas de bloqueo inciales, los depositantes se enfrentarán a sanciones si los tokens son inactivos durannte más de 4 semanas.
{{< /notice >}}

Si quiere profundizar en el análisis de los rendimientos ofrecidos por la delegación de CVX y la relación con la compra de voto, no dude en [leer este artículo (EN)](https://medium.com/@portiadog/convex-finance-1cc6c9c1c733) que propone cálculos más detallados:


![bribes-rewards](/img/2021/crv-wars/bribes-rewards.png "Estimación del rendimiento de la delegación de voto en Curve vía vlCVX")


### Bribes : una división confusa

La situación era clara, pero no duró mucho tiempo. De hecho, hay que resaltar que vlCVX no está exento de rendimiento: **los titulares de vlCVX se distribuyen 6% de todos los CRV cultivados por Convex bajo la forma de CvxCRV**.

Además, no es el único rendimiento para el que los titulares de vlCVX pueden ser potencialmente elegidos. En efecto, **el poder de gubernanza puede ofrecer un rendimiento consecuente à través de los mecanismos de bribes** (compra de votos).

Varios proyectos proponen incentivos para votar a favor de un pool Curve determinado. Por ejemplo, Alchemix ofrece recompensas en ALCX, su token nativo, que puede ser reclamado todas la semanas por quienes utilizaron sus VeCRV para votar por aumentar los beneficios CRV del pool AlUSD.

A largo plazo, no es imposible ver que la división inicial prevista por Convex no sea la más honesta. A la hora actual, el rendimiento en CvxCRV está alrededor de 60% mientras que el de CVX es de 15%. Sin emabrgo, **cuando añadimos los bribes en la ecuación, es posible que el rendimiento de vlCVX sea mucho mayor que el de CvxCRV.**


## El campo de batalla

Los servicios de bribes son un elemento esencial de la ecuación de gubernanza de Curve. No obstante, antes de cabar hay que recordar el camino de base (VeCRV) que define el marco de todas sus variantes.

VeCRV se obtiene bloqueando CRV por un período hasta de 4 años. Entre mayor es el tiempo de bloqueo, más el racio VeCRV/CRV se acerca a 1. **El bloqueo se se reduce gradualmente en el tiempo así como el poder de voto**.

Es por esto que las bóvedas construídas en VeCRV operan con una lógica de bloqueo perpetuo de 4 años: con el fin de conservar un poder de voto lo más cerca posible del máximo, **refrescan (refresh) el bloqueo frecuentemente.**


![ecosysteme-vecrv-tokenbrice](/img/2021/crv-wars/ecosysteme-vecrv-tokenbrice.png "Enfoque del ecosistema costruído en VeCRV")


### Bribes v0 : incitación directa en los pools

Antes de hablar de bribe, es necesario recordar que existe una forma primitiva desde los inicios de Curve: las incitaciones adicionales (además de los CRV) para los proveedores de liquidez. Synthetix fue el pionero con su programa de liquidity mining en SNX en el pool sUSD.

Las incitaciones directas son acumublables con los bribes, y de hecho es recomendable. Veremos más abajo como MIM, por ejemplo ha obtenido mucha más actividad compartiendo su presupuesto entre incitación y bribes (después de una fase inicial sin bribes).


### Brive.crv de Cronje [en veCRV]

Como ya lo sabe, los "bribes" son compras de votos VeCRV. Se pagan semanalmente, generalmente los viernes (día de recuento de votos).

Sin embargo, así como hay tantos sistemas para interactuar con VeCRV, existen diferentes mecanismos para los bribes. Comencemos entonces por el que ha estado disponible de primero: [http://bribe.crv.finance/](http://bribe.crv.finance/)

Aquí la unidad de base es el VeCRV. Bribe.crv es una interfase simple que reúne las diferentes ofertas y permite de recoltar sus bribes. El voto se hace directamente en Curve.

Desde sus inicios, un poco timido, el servicio es cada vez más utilizado y muchos proyectos proponen desde ahora los bribes. Los rendimientos de las primeras semanas son excelentes, esperemos que duren. Por ejemplo, yo gané **alrdedor de 10% de retorno sobre mis VeCRV (/precio actual) en 5 semanas** votando por el pool MIM y recibiendo los tokens SPELL en bribes.

Ya vendremos sobre los resultados obtenidos más adelante.


### Votium [en vlCVX]

La alternativa disponible, es [Votium](http://votium.app/). Aquí la unidad base es el vlCVX, los dos servicios no son competencia sino más bien complementarios.

Votium es más reciente por lo que los bribes disponibles son menos numerosos. Por el contrario, **Votium ya controla un poder de voto impresionante: alrededor de 8M CVX, o sea más de 102M de VeCRV**.

Aquí el sistema es potencialmente más pasivo que con bribe.crv porque los depositantes pueden delegar a Votium quien se encargará de votar por ellos cada semana y recolectar los bribes correspondientes.

Incluso con una delegación activa, un depositante puede retomar el control y votar por un pool determinado, directamente en snapshot (-> sin costo en gas). Por lo que a este nivel el sistema es más flexible que bribe.crv.

Otros servicios para gestionar los bribes están en desarrollo y saldrán próximamente. Hasta el momento el juego de bribes está centrado principalmente alrededor de CRV, pero [Paladin](https://www.paladin.vote/), por ejemplo, supone proponer un mecanismo similar pero con otros protocolos.


## Puesta en práctica: tácticas y resultados

Las bases conceptuales sobre este tema son un poco complicadas, pero es primordial entenderlas. Para hacerlo más explícito, pasemos a la práctica con ejemplos concretos.

### Ejemplo de Spell/MIM

[Abracadabra](http://abracadabra.money/) es un servicio tipo Maker. Diferentes activos son aceptados como garantía, breve, activos productivos como xSUSHI o como cvx3pool.

Así como Maker produce DAI, Abracadabra produce un stablecoin (en Dólar) bautizado MIM. La liquidez disponible en MIM, como las oportunidades de renidmiento, son un factor básico del éxito de la plataforma.

Es por esto que Adacadabra ha pasado progresivamente por todas las formas de bribes directas o indirectas de curve:

1. Todo comienza con una incitación en SPELL (token de guberenanza) del pool Curve/MIM.
2. Cuando bribe.crv llegó, **una parte de esta incitación ha sido reposicionada en bribe** - distribuída a los titulares de VeCRV que voten por el indicador MIM.
3. Ahora, con la llegada de vlCVX, el equipo considera reorientar este presupuesto de esta manera.

En algunas semanas, el pool MIM explotó en Curve, en todos los niveles:


* Los rendimientos en CRV fueron excelentes durante varias semanas
* Lo que atrajo liquidez y volúmen, reduciendo ligeramnte el rendimiento pero aumentando la capacidad de propulsar el pool
* A través de esta dinámica, MIM es ahora el quinto pool en Curve en términos de volúmen, con un racio volúmen/TVL.

![curve-pools](/img/2021/crv-wars/crv-pools.png "Enfoque de los pools más grandes de Curve (volúmen)")

Entre otras, el pool está bien equilibrado y más bien denso (> $700M liquidez total).

El ejemplo de Adacadabra es extremadamente instructivo, porque demuestra toda la pertinencia de las abstracciones construídas en VeCRV: **sin aumentar su presupuesto total, Abracadabra ha estado a la altura de atraer más liquidez que en la época de la simple incitación directa en SPELL.**

Así pues, los proyectos DeFi que aprovechan los mecanismos de VeCRV, cvxCRV y vlCVX tienen una ventaja innegable (**económica Y política**) frente aquellos que aún no han captado todas sus sutilezas.


### Ejemplo cruzado: sdveCRV Vs cvxCRV

En efecto, **ahora considero la comprensión de Curve y la capacidad a influenciar eficazmente su gubernanza como una capacidad esencial y necesaria en la mayoría de proyectos DeFi, sobretodo para los proyectos de stablecoin.**

Sin embargo, no es necesario que me crean. Comparemos en la práctica dos enfoques puestos en marcha por proyectos con enjuegps similares: las estrategias de liquidez en cvxCRV (de Convex) y sdveCRV (de StakeDAO) - dos abstracciones construídas en VeCRV.

A pesar de que las situaciones sean parecidas, hay diferencias abismales:



1. Comencemos por recordar que Convex controla más de 30 veces la cantidad de CRV controlada por Stake (102M Vs 3M)
2. Además; sdveCRV tiene serios problemas con su peg: 1 sdveCRV ~= 0.5 CRV


![sdvecrv-peg](/img/2021/crv-wars/sdvecrv-peg.png "V-Cambio de sdveCRV/CRV")


#### Programa de liquidez sdveCRV: incomprensión total y fracaso evidente

Pasemos al análisis. Al principio la liquidez sdveCRV era anti ETH al igual que Yearn. Desde Convex, el equipo de Stake intenta reaccionar para volver sdvrCRV más atractivo.

Sin embargo, el equipo no se tomó el tiempo suficiente para análizar la situación y se precipitó en lo que resultó ser **uno de los fracasos más graves jamás visto en Curve**.

Después de haber creado un anémico pool sdveCRV/CRV a través de la Curve Factory, se sometió un voto para añadir el control del indicador (= incentivos CRV). No solamente [el voto fue rechazado masivamente](https://dao.curve.fi/vote/ownership/83) sino además **el pool sdveCRV fue parametrado aberrante y absolutamente peligroso para los depositantes.**

**Incitar al depósito en un pool parecido hubiese sido como enviar los depositantes al matadero**. En efecto, el factor A (parámetro de amplificación) del pool es [definido a 200](https://curve.fi/factory/34) --- un valor correcto para los activos que siguen el mismo peg, pero delirante si un activo vale dos veces el otro.

![sdvecrv-mim-crv-pools](/img/2021/crv-wars/sdvecrv-mim-crv-pools.png "Comparación de pools Curve (factory) sdveCRV y MIM")

Para darles una idea, incluso el pool MIM mencionado más arriba, absolutamente masivo (7000x la liquidez del pool sdveCRV) ni siquiera ha alcanzado 200 de factor (119 actualmente y en aumentación).

Así pues, Stake no solo a logrado resolver su problema de liquidez en sdveCRV, sino además **dicha secuencia de acontencimientos plantea claramente la pregunta de la comprensión del equipo de Stake de las sutilezas de Curve/Convex**.

Para hacer volver el sdveCRV a su peg y desarrollar su liquidez, necesitarán realizar muchos esfuerzos, en este orden:



* Revisitar los parametros del pool
* Incitaciones directas en SDT en el pool?

Una vez realizadas esta etapas, el equipo tendría un chance de tener el indicador CRV en este pool, pero no antes. Por lo que la situación actual se parece más a un costoso impase: **no hay salida a menos que se caliente la máquina de SDT**.


#### Programa de liquidez cvxCRV: despegue inmediato

El programa de liquidez en cvxCRV muestra por el contrario a que punto el proceso puede ser eficaz. Al principio (y aún hoy), el pool principal de cvxCRV está en Sushiswap, contra CRV.

Esta situación no tiene mucho sentido: **Sushi está lejos de ser ideal para optimizar la liquidez de activos que siguen el mismo peg**. Así, cuando Curve ha lanzado los Factory Pools (V2), el pool [pool cvxCRV/CRV](https://curve.fi/factory/22) ha sido uno de los primeros en sobresalir.

(Observese que el Factor A a 50 - mientras que cvxCRV mantiene su peg mucho mejor que sdveCRV...)

![cvxcrv-pool](/img/2021/crv-wars/cvxcrv-pool.png "Pool (factory) cvxCRV/CRV")

Sin tener incitación de la parte de Convex o Curve, el pool ya ha visto pasar un volúmen importante gracias a los agregadores de DEX como Paraswap. Rápidamente, hubo un voto para añadir el indicador CRV que pasó - y este pool es directamente cultivable vía Convex.

El pool sigue ligeremante desequilibrado (hay tanto por hacer con los CRV, que se vuelven cada vez más raros…) pero aporta ya una alternativa competitiva al pool SLP cvxCRV/CRV aún con una fracción de su liquidez.


## Conclusión

Espero que este artículo le haya ayudado a comprender las sutilezas del ecosistema ampliado de veCRV y sus consecuencias para la batalla de los CRV.

Antes de terminar, debo recordarle que como siempre el alfa se encuentra en los comederos. Si entendió este artículo, no dude en exportar el análisis de la estrategia de liquidez en otros proyectos: estoy seguro que será instructivo!

Menciono a menudo, pero nuca lo suficiente: no solo Curve es el DEX más importante en DeFi sino también **el protocolo más adelantado en términos de gubernanza y de tokenomics, de lejos con respecto a cuaquier otro**. Incluso si no tiene ningún interés por Curve/Convex, es indispensable entender estos protocolos para proyectar bien lo que se pasa en DeFi… Esperando que este artículo le ayudará!

{{< notice tip >}}
Para profundizar su comprensión de CRV, pilar de la DeFi, también le propongo dos sesiones en directo con Charlie; un miembro del equipo Curve:

**[Maratón DeFi Curve Finance en detalle](https://www.youtube.com/watch?v=G5PbqGtjSDQ)**
{{< /notice >}}

{{< youtube EjuPdHv1bX8 >}}

_🙏 Muchas gracias a HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony por su cuidadosa relectura de la edición francesa de este artículo y su traducción al inglés._
