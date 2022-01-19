---
title: "🗿 Para que, cómo y que es el RAI ?"
description: "El RAI de Reflexer es un nuevo tipo de activo único en Defi. Se basa en un sistema con un plan de desgobernanza. Veamos como evitar los riesgos relacionados a la moneda fiduciaria, la centralización y la confianza al mismo tiempo."
date: '2022-01-19T01:13:50.191Z'
categories: [🌌 DeFi, ⚙ Comprendre]
tags: [DeFi, Ethereum, Finanza descentralizada, Stablecoins, Activos estables, Mercados Monetarios, Reflexer, RAI, Maker, Liquity]
toc: true
tocNum: true
url: reflexer-rai
---

RAI es una figura extraña que mucha gente no entiende o aprecia todavia, incluso aquellos más adentrados en DeFi. Por lo que ya era tiempo de proponerles un artículo exhaustivo dedicado a este tema. He incluido todo lo que estimé pertinente para comprender por qué un activo como RAI es necesario, lo que aporta y como funciona.

Prepárese un café y póngase cómodo, que nos vamos de paseo!


![cover](/img/2021/reflexer-rai/cover.gif)

## Entender el contexto de RAI

Antes de entrar en el núcleo del tema, creo que es esencial comprender el contexto de RAI: es decir, los principales activos estables utilizados hoy en día y como también sus límites.

El contexto de RAI es bastante denso, pero la buena noticia es que no es la primera vez que trato este tema en el blog. Lo invito a leer estos artículos bien pertinentes para profundizar:  



1. [Activos de vocación estable en Ethereum : que enfoques y que enjuegos?](https://tokenbrice.xyz/ethereum-stable-assets/)
2. [Comprender las innovaciones en los mercados monetarios para proyectar sus futuros](https://tokenbrice.xyz/money-market-innovations/)

Si no tiene tiempo para explorar y profundizar sobre el concepto en los artículos propuestos anteriormente, aquí le presento los dos puntos esenciales a tener en cuenta para comprender lo que sigue:

1. A la hora actual, **la inmensa mayoría de la necesidad de stablecoin está cubierta por soluciones centralizadas que requieren de la confianza**, siendo USDT (~66 Mil millonnes) y USDC (~27 Mil millones) las más utilizadas. 
2. Cualquiera que sea su tésis económica de predilección, particularmente en términos de inflación, creo que podemos facilmente convenir en la necesidad de activos estables que no tengan una corelación con una moneda fiduciaria (=gestionada por un estado).  


### La trampa del wUSD

Utilizo el término "wrapped USDC" (wUSDC) para explicar una situación frecuente en los stablecoins alternativos: permite describir de manera concisa y apropriada **las solucionens que utilizan principalmente USDC como colateral**, un stablecoin garantizado por un organismo central (Circle).

En una situación como esta, inútil de seguir, ni siquiera es necesario analizar los detalles del sistema: porque su colateral principal puede ser congelado o confiscado, **los stablecoins producidos de esta manera no pueden ser considerados como descentraliszados o que no requieren de la confianza**.

En esta familia hay un número sorprendente de representantes, los principales son Maker y Frax.


#### Maker = una mayoría de colaterales que necesitan de la confianza

Con Maker (DAI), **alrededor de 60% de los DAI son minados (creación de moneda) con USDC como colateral**, cifra a la que hay que sumarle los que son minados a partir de otros colaterales que al igual necesitan de la confianza como: wBTC, TUSD, GUSD, PAX, USDT, renBTC + todos los pares de UniV2 que incluyen al menos uno de estos tokens + todos los colaterales propios del mundo real como Centrifuge: New Silver. [Detalle en DAIStats](https://daistats.com/#/).

![dai-colateral](/img/2021/reflexer-rai/dai-collateral.png "Cuadro de distribución de colaterlaes utilizados para garantizar el DAI en el sistema MakerDAO.")


Nota: el PSM es un módulo que permite evitar las subidas de precio del DAI sobre el dólar. Los DAI minados por el PSM lo son de manera automática cuando es necesario.

La primera versión de Maker antes de la actualización de Multi Collateral DAI ([MCD - 18/11/2019](https://medium.com/@MakerDAO/update-the-road-to-multi-collateral-dai-2d4c48092270)) utilizaba únicamente ETH como colateral, teniendo así garantias más credibles. Lo que no es el caso hoy en día. 

🙏 Sin embargo agradezco considerablemente al equipo de MakerDAO por sus innumerables aportes al ecosistema - de hecho el modelo Maker MCD es utilizado como base por Reflexer!


#### FRAX? Garantía par el USDC o nada - (algorítmico)

**Del lado de FRAX, sólo el USDC es utilizado como colateral**, bajo diferentes formas - en Yearn/Compound/Aave para producir un rendimiento, o vía los AMOs (Algorithmic Market Operations Controller](https://docs.frax.finance/amo/overview)). Detalle de los activos que sirven para para garantizar el FRAX, [disponible en el sitio oficial](https://app.frax.finance/). 

![frax-collateral](/img/2021/reflexer-rai/frax-collateral.png "Cuadro de los colaterales utilizados en FRAX: USDC y todas sus variantes yield-bearing (riesgos técnicos adicionales) + una parte algorítmica (sin colateral) variable.
")

Al igual que DAI, FRAX desarrolla una infinidad de enfoques interesantes, pero como sus bases son centralizadas, **no pueden ser considerados sino como un mecanismo más de incremento de la liquidez disponible en USDC, a lo sumo**. Sin embargo hacen **contribuciones interesantes en términos de investigación fundamental** que podrían ayudar a establecer una solución más óptima y que no requiera de la confianza (trustless).


### Existen otras alternativas relevantes a RAI?

Al día de hoy, RAI es un activo único sin alternativa comparable. No obstante, existen otros sistemas que comparten ciertas características con RAI, como **la utilización exclusiva de ETH como colateral**.

Así, si está dispuesto a exponerse al dólar, Liquity propone una alternativa muy interesante que tiene igualmente **el mérito de ser totalmente imparable** (lo que por ahora no es el caso de RAI): los contratos no tienen ninguna función administrativa, exactamente como Uniswap V1/V2. Sin embargo quedan los oráculos (necesarios para un servicio de préstamos) y los riesgos asociados.

Ahora que la mesa está lista, pasemos al plato principal: es hora de estudiar los mecanismos subyacentes de RAI. Comencemos por el minaje desde la perspectiva de un usuario antes de profundizar en lo que es DAI concretamente y de como funciona.


## Cómo se crea RAI?

El RAI de Reflexer es de alguna manera **tanto la forma primaria como la final del DAI de Maker**. Primaria, porque retoma la promesa del DAI original (el SAI): sólo el ETH es utilizado como colateral. Y final en la medida donde RAI logra eliminar esa dependecia al dólar.

De esta manera Reflexer se apoya en una base de Maker MCD con algunos cambios, principalmente la integración del controlador PID, la protección contra las liquidaciones y otras más. Vamos a retomar todo esto mas tranquilamente, comencemos por ver como el sistema funciona desde la perspectiva de un usuario.

Al igual que en Maker, RAI es creado directamente por los usuarios de Reflexer. Los que puedan abrir **un "safe" que les permita poner en juego ETH y minar una cantidad proporcional de RAI**. Cada usuario puede decidir la cantidad de RAI minada por la misma cantidad de ETH puesta en juego (-> diferentes niveles de riesgo) y debe gestionar su posición. **Las liquidaciones son posibles y necesarias** porque permiten asegurar que siempre haya un valor suficiente en ETH para garantizar los RAI emitidos.

Sin embargo, aquí el sistema innova con respecto a Maker gracias a su función "Savior". Porque permite **utilizar una posición de aporte de liquidez RAI/ETH en Uniswap V2 como garantía para un safe**. De esta manera, si el precio del ETH bajara brutalmente, lo que podria poner un safe abierto y protegido por esta función en riesgo de liquidación, **el Savior retira automáticamente la cantidad de liquidez necesaria para devolver el safe al nivel de colateralización deseado**.

Esto va a dejar dormir más serenamente a los usuarios que minan el RAI para aportarlo como liquidez!


## Pero, que es RAI realmente?

RAI en sí, es una nueva clase de activos. Tiene la vocación de ser **menos volátil sin necesidad de apoyarse sobre otro activo estable** (las monedas fiduciarias o el oro son los más tradicionales). Para esto, RAI se basa en un sistema que reacciona dinámicamente según las condiciones del mercado.

En el caso de RAI, se debe tener en cuenta dos parámetros esenciales:



1. **El precio de redención** (redemption price) = valor de una unidad de deuda en el sistema
2. **El precio del mercado** (market price) = precio del RAI en el mercado

El sistema no tiene que controlar para nada el precio del RAI en el mercado, ya que está determinado por los compradores y vendedores. No obstante, puede ajustar progresivamente ciertos parámetros para modificar el precio de redención y **hacer converger los dos precios en el curso**.

Por lo tanto, nos encontramos ante una situación fácimente generalizable, personificada por toda una rama de la ingeniería y bautizada **la teoria del control**:

![teoría-del-control](/img/2021/reflexer-rai/theorie-du-controle.png "Circuito de control. Este gráfico, como también los dos que siguen son de la traducción francesa del libro blanco de RAI - muchas gracias PhilH & Ben.Oxmo por ese trabajo calitativo.
")

En el caso de RAI, **el regulador es algorítmico** y una vez más, bien estándar: es el famoso **"Controlador PID"**. Reposa sobre una fórmula matemática bastante extensa que no es necesaria comprender para asimilar la trascendencia del sistema.

Pero hay que asimilar un punto esencial: la inercia ineherente al sistema. El regulador no se puede permitir de realizar cambios bruscos en parámetros (que afectaría su relativa estabilidad), por lo tanto debe operar bajo **una lógica más iterativa y progresista**.

Una vez entendido, me permito recordar que el sistema en sí no puede hacer nada por el precio de RAI. Lo que puede hacer, es variar la tasa de redención, lo que permite modular la incitación en los participantes del sistema. Creando así **oportunidades de arbitraje** para ellos, que una vez ejecutadas permite acercarse al precio de equilibrio entre el precio de redención y el precio de mercado.

Veámoslo más concretamente en la práctica.

Aquí encontramos una lógica que nos recuerda los [stablecoins algorítmicos](https://tokenbrice.xyz/posts/2020/algorithmic-stablecoins/), a pesar de que el producto final del sistema sea totalmente diferente.


### Cuando el precio del mercado > precio de redención

Comenzamos por esta situación porque en mi opinión es más fácil de entender. En el caso donde el precio del mercado sobrepasa el precio de redención. Esto significa que toda persona con ETH disponibles podria potencialmente generar beneficios arbitrando en el mercado.



1. Depósitar ETH y minar RAI;
2. Venta de RAI en el mercado para un beneficio;
3. (Cuando el precio del mercado < redención) recomprar RAI para rembolsar la deuda y liberar los ETH. La diferencia entre los 2 precios de RAI - los gastos generados corresponden al beneficio realizado.

![mercadosupredención](/img/2021/reflexer-rai/marchesupredemption-en.PNG)


Esta situación es mucho más interesante para quienes ya tienen safes y cuentan con la disponibilidad: se ahorran una etapa del escenario presentado más arriba.

En este escenario, existe, por tanto, un incentivo para minar RAI (->aumentar la oferta) y luego revenderlo en el mercado (->presión de resistencia), lo que reduce gradualmente el precio del mercado, haciendolo converger hacia el precio de redención.


### Cuando el precio del mercado < precio de redención

En el caso opuesto, la tasa de redención se vuelve positiva, lo que tiene por efecto de hacer más costosa la deuda existente. Los usuarios con safes activos tienen interés en pagar la deuda, lo que reduce la oferta de RAI.

![mercadoinfredención](/img/2021/reflexer-rai/marcheinfredemption-en.png)


Entre otras, si hubiesen convertido sus RAI por otro activo (por ejemplo por ETH para una exposición apalancada), deberán obtener los RAI en el mercado (->presión alcista) con el objetivo estar en capacidad de rembolsar la deuda.

Como lo ha entendido, los actores del sistema Reflexer tienen todo el interés de seguir la tasa de redención y reaccionar en consecuencia. Si tiene un safe activo, lo innvito a cosultarlo regularmente - [se puede ver en el sitio de Reflexer.](https://stats.reflexer.finance/)

Esta tasa impacta menos a quienes simplemente poseen el RAI, sobretodo si lo utilizan para generar un rendimiento (que puede compensar una tasa negativa) pero sigue siendo al menos una medida a tener en cuenta.


### Ajuste dinámico de la tasa de redención 

**El ajuste dinámico de la tasa de redención es una de las funcionalidades principales de Reflexer / RAI**. Para entender mejor porque es importante, analicemos la situación en Maker pre-MCD:



1. La demanda en DAI corresponde a (una parte de) la demanda de stablecoins.
2. No obstante, los DAI son creados apalancando ETH, por lo que dependen de la necesidad/apetito de apalancar en ETH, siendo esto independiente de la demanda de stablecoins, quienes dependen directamente de las condiciones generales del mercado (bajista, alcista ou otras).
3. Si la demanda es mayor que la oferta, en Maker, no existe un ajuste dinámico. Hay que esperar que la gobernanza vote (y los detalles que vienen con esto), con el fin de disminuir el Costo de la Estabilidad. Y es igual en el otro sentido (cuando la oferta es mayor).

Así, **el equilibrio entre la oferta y la demanda es casi imposible de sostener**, lo que explica por qué el DAI pre-MCD podía encontrarse a menudo por encima de su peg. Maker solucionó este problema integrando diferentes tipos de colaterales, entre los cuales stablecoins que no requieren confianza, luego el PSM, que mina automaticamente DAI desde USDC cada vez que sea necesario. La solución propuesta por Reflexer (ajuste dinámico de la tasa de redención) tiene el mérito de **resolver el problema a nivel del sistema en sí**, lo que permite conservar ETH como solo colateral.


## FLX y el plan de "gobernanza" de RAI

A parte del RAI, el sistema de reflexer tiene un segundo token, FLX, el token de desgobernanza ("ungovernannce"). Es utilizado por la gonernanza del sistema y sirve igualmente como mecanismo de liquidez de emergencia (en caso de impago), con un sistema bastante parecido al Safety Module de Aave.

El token FLX puede ser integrado en el mercado, pero es basicamente **distribuido entre los principales actores implicados en el sistema** - [la lista exhaustiva de incentivos en FLX](https://app.reflexer.finance/earn/incentives) disponible en el sitio de Reflexer.

De esta manera, son elegibles para los FLX (reclamables en el sitio de Reflexer, distribución mensual):



1. Los tenedores de Safes que aportan sus RAIs como liquidez en el par UNIv2 ETH/RAI (migración en proceso y pronto disponible) o también UNIv3 RAI/DAI.
2. También los proveedores de liquidez en FLX//ETH (migración en proceso y pronto disponible).
3. Y finalmente los stakers de FLX en el equivalente al Safety Module de Reflexer.
4. Hay igualmente incventivos en FLX por la utilización de RAI en los diferentes servicios de DeFI, detallados en la última parte.

[El staking de FLX (Uni V2 FLX/ETH)](https://docs.reflexer.finance/incentives/flx-staking) sirve a la vez como mecanismo de incentivo en el aporte de liquidez y como garantía del sistema. Si el sistema es subcolateralizado, los stakers seran diluidos (-> liquidación de los token LP) para que el módulo adquiera RAI y devuelva el equilibrio al sistema.

En estado normal, los stakers simplemente se benefician de un rendimiento más bien atractivo. Igual como en el Safety Module de Aave, ese módulo tiene un plazo para retirar sus depósitos, para evitar el éxodo de liquidez en períodos de crisis: 21 dias.

Ahora que tenemos las bases de FLX, discutamos un poco más de los enjuegos a largo plazo.


### El plan de retiro de la gobernanza

El sistema Reflexer tiene por vocación de ser "governance-minimized". Comenzó desde su inicio, ya que las decisiones que en Maker son tomadas por la gobernanza (Stability Fee de las bóvedas) son automatizadas en Reflexer (Controlador PID).

La visión es automatizar todo lo que se pueda automatizar a largo plazo, una vez el sistema sea maduro, y darle las llaves de los subsistemas que no puedan automatizarse a la comunindad de holders de FLX.

El equipo se ha fijado tres pilares principales en relación con este objetivo [detallados en el artículo de presentación de FLX](https://medium.com/reflexer-labs/introducing-flx-20755214a465). Cada pilar está vinculado a una fecha:



* 14 meses después del lanzamiento - 17 de abril de 2022: reducir al mínimo la gobernanza de los subsistemas principales (liquidación, subasta y taxación).
* 18 meses después del lanzamiento - 17 de agosto de 2022: minimización de la gobernanza en todos los contratos principales, a excepción del Controlador PID, los oráculos y el mecanismo Savior.
* 3era etapa (fecha por confirmar): pasación de poder (hacia los holders de FLX) y mecanismos restantes.

Creo que este recorrido es suficiente para entender claramente el interés de RAI y como funciona. Ahora veámos como funciona RAI en los diferentes protocolos DeFi.


## El ecosistema DeFi en torno a RAI

RAI está siendo adoptado progresivamente en el seno del ecosistema DeFi, y da gusto verlo! Propongo terminar con tour alrededor de las diferentes integraciones de RAI en los protocolos de DeFi, comenzando por los mercados monetarios.


### RAI en Fuse (Rari Capital)

Fuse es une mercado monetario muy innovante porque permite la creación de pools por actores que no pertenecen al equipo, y pronto por cualquiera. Por lo que es bastante lógico que Fuse haya sido uno de los primeros mercados monetarios a soportar RAI. En temas de Pools, también es posible de **utilizar RAI como colateral en Fuse**.

Por el momento RAI es disponible en 3 pools de activos que proponen diferentes niveles de riesgo y de tokens prestables:

![fuse-rai](/img/2021/reflexer-rai/fuse-rai.png)

### RAI en Aave

Después de haber integrado el soporte RAI hace ya algunas semanas, Aave acaba de asignar un presupuesto (muy modesto) de StkAAVE para inncentivar los préstamos y depositos en RAI. Ha sido necesario sacar a la luz una de las contradicciones principales de la plataforma:  Aave es un mercado monetario descentralizado que utiliza (aún) la mayor parte de su presupuesto para incitar los préstamos/depósitos en stablecoins que no son descentralizados (USDC y USDT).

<div align = "center">
{{< tweet 1426577620695719944 >}}
</div>
  
Es de remarcar: que por el momento **el max TVL de RAI es de 0: por lo que RAI no puede servir de colateral en Aave**. sin discriminar, es muy básico de la parte de Aave - se trata del procedimiento "tradicional" y prudente cuando es sobre la integración de un nuevo tipo de colateral. La gobernanza puede votar para aumentar este valor.

  
### RAI en Cream
  
Cream fue uno de los primeros mercados monetarios en incorporar RAI. Y sin embargo se trata de un mercado de segunda categoría extremadamente riesgoso y sin ningún valor agregado, puede ser incluso perjudicial a largo plazo. Bueno, lo dejo hasta ahí , y [los invito a leer este artículo si se pregunta por qué](https://tokenbrice.xyz/money-markets-risk/)
  

### RAI en Idle Finance

Idle Finance es un servicio que permite, como su nombre lo indica, poner en marcha estratégias de rendimientos pasivos. En el caso de RAI, Idle explota los rendimientos disponibles en Fuse como en Aave. Inicialmente, también lo hacía en Cream pero la gobernanza a decidido de recentrar las estrategias para reducir el riesgo: 

<div align = "center">
{{< tweet 1429907701081989121 >}}
</div>
  
Además del rendimiento nativo en RAI, un depósito en Idle Finance también le permite beneficiar:
  
  
  
1. De un rendimiento en FLX, visible aquí.
2. De un rendimiento en StkAAVE (correspondiente a la parte de RAI utilizados en Aave).
3. Y finalmente, también de un rendimiento en IDLE (pronto - aprobado por la gobernanza pero aún sin implementar).
  
Así, si desea obtener RAI en el largo plazo para protegerse contra los riesgos relativos al dólar/euro, un depósito en Idle es muy atractivo para producir un rendimiento totalmente pasivo. Sin embargo tenga cuidado, porque esto conlleva a otros riesgos de Smart Contract: Reflexer + Aave + Fuse + Idle


### RAI + FEI Protocol

FEI es otro stablecoin que busca maximizar la descentralización. Aquí el enfoque es diferente y se basa principalmente en la noción de **"Protocol Controlled Value" (PCV)**. En resúmen, la mayor parte de la liquidez de los pares de FEI está controlada por el propio protocolo. Los fondos se originan desde la creación del protocolo donde los usuarios han comprometido ETH para adquirir FEI y TRIBE (token de gobernanza) en su inicio.
  
De esta manera, FEI es un stablecoin que comparte una característica con RAI y LUSD: está completamente colateralizado por activos trustless (ETH). No obstante, FEI está mucho más cerca de LUSD que de RAi en el sentido de estar indexado al dólar.
  
Recientemente, la DAO de FEI votó para **diversificar parte de los fondos del protocolo para invertir en RAI** con el fin de hacerlo más perenne. Así, hasta 6 millones de dólares (~2M RAI) serán adquiridos y se utilizarán en Aave y Fuse para generar un rendimiento. Otras DAO también proyectan de diversificar parte de sus fondos en RAI (Moloch, DxDAO, Metagame, etc.), por lo que creo que vendrán más iniciativas de este tipo.


<div align = "center">
{{< tweet 1430625935607226368 >}}
</div>

## Conclusión

Espero que esta presentación bastante exhaustiva de RAI le haya enseñado algo. Como siempre, tenga presente que escojo cuidadosamente mis temas y este artículo no constituye de ninguna manera un consejo en inversión. En la ocurrencia, la elección de Reflexer/RAI es porque es un sistema elegante en el que el análisis permite discutir sobre diferentes nociones básicas para mejor entender la DeFi y su conjunto.
  
Confío en que este artículo le haya sido instructivo.
  
Muchas gracias a HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony por su corrección y la edición francesa de este artículo, y su traducción en inglés. Como también a [Guifel](https://twitter.com/guifel_) del equipo de Reflexer por sus sugerencias bien pertinentes._
  
Quiere saber mas? Pues bien, el equipo de Reflexer le propone artículos bien redactados para explicar el sistrma más profundamente - en inglés. Estos son los que le recomiendo leer en particular:
 
* Un artículo [para entender el enfoque desarrollado para asegurar el protocolo](https://medium.com/reflexer-labs/securing-the-money-god-ef21453a299b)
* [Una serie de tres artículos de simulación, perfectos para poner en práctica su comprensión de RAI](https://medium.com/reflexer-labs/rai-system-simulations-part-1-safe-owners-876a6bd55385)

_🙏 Muchas gracias a [DFr3sh2](https://twitter.com/DFr3sh2), que se encargó de la traducción de este artículo al español._