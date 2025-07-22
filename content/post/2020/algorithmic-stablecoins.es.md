---
title: "El presente y el futuro de los stablecoins algorítmicos"
description: "Un análisis de DSD, ESD y Basis Cash para imaginar lo que podría ser el stablecoin de mañana."
date: '2020-12-28T01:13:50.191Z'
categories: [🌌 DeFi]
tags: [DeFi, Ethereum, Stablecoins, Maker, MakerDAO, Basis Cash, Empty Set Dollar, Dynamic Set Dollar, USDT, USDC, sUSD, ESD, DSD, BAC, BAS]
---

Desde principios de diciembre, una nueva tendencia aparece en DeFi: los stablecoins algorítmicos. Se ha puesto en marcha una serie de proyectos que han conocido un importante crecimiento, lo que ha generado un mayor interés en este subconjunto del espacio.

Antes de entrar en lo que son y lo que implican, primero abordemos los posibles mercados. Los stablescoins en Ethereum son masivos: hay en circulación alrededor de 20 billones de USDT, 3.5 billones de USDC y 1 billón de DAI. Como puede constatarlo, la mayor parte del volumen se cubre actualmente con stablecoins que requieren alguna forma de confianza, como el **USDC o el USDT: la sociedad que los emite tienen el poder de congelar los activos y de manipular los saldos**. 

![DeFi BRRR](/img/2020/algorithmic-stablecoins/cover.png "Bienvenido! Espero que le guste este recorrido").

Maker ha explorado otro enfoque con el DAI que implica menos compromisos - sin embargo, la extensibilidad es reducida. Por otra parte, hoy en día es difícil considerar el DAI como "suficientemente sin confianza" a pesar que 60% de las garantías para generarlo no lo son (USDC, wBTC, TUSD, etc.).

Cabe recordar que hasta el momento, existe una clara necesidad en el sector de los stablecoins - los que han logrado un activo circulante significativo lo han hecho con importantes concesiones, lo que les ha permitido satisfacer los mercados a pesar de que se trata de servicios que requieren de confianza, y que son más o menos fiables (en particular USDT).  

La razón por la que hoy escribo este artículo es que después de haber seguido durante años la evolución del espacio de los stablecoin, parece que hemos alcanzado un interesante avance con una nueva generación de stablecoins capaces de ofrecer tanto **escalabilidad como confianza**. El temo no es ni simple ni facilmente accesible, sobretodo para los nuevos incorporados. Haré todo lo posible para guiarlo paso a paso en el proceso de reflexión.   

---

### Por qué necesitamos stablecoins que no requieren confianza?

Antes de entrar en que proyecto hace qué y con que fin, revisemos lo siguiente. Hemos establecido que existe una demanda importante de stablecoins, y que ninugna de las opciones bandera de hoy en día son suficientemente trustless. Pero que quiere decir esto exactamente?

En algunas palabras, la **trustlessness significa que la totalidad del sistema no necesita de un punto central de confianza para funcionar correctamente**. Lo conocemos comunmente como "resistencia a la censura", una propiedad diferente que yace de la trustlessness. Desde un punto de vista práctico, a continuación una serie de preguntas que le ayudarán a evaluar la trustlessness: entre más permisivas sean las autorizaciones, menos confianza suele generar el proyecto:

1. Los tokens pueden ser confiscados o congelados?
2. El código y los parámetros del protocolo se pueden actualizar? Bajo que condiciones? Quien lo hace?
3. El protocolo depende de servicios externos, como una fuente de precios (oráculo) que podría ser manipulado?
4. Quien o que podría generar nuevos tokens? Es por iniciativa del usuario (alguien que realice una acción) o del protocolo (una decisión que el protocolo toma en función de los parámetros establecidos)?

La última pregunta es especialmente pertinente, porque ella deja en evidencia un elemento básico de los stablecoins algorítmicos: **su "banco central" es un contrato inteligente** - nadie lo controla, responde simplemente a los parámetros del sistema. Lo retomaremos más adelante.

Con esto, analizaremos los principales elementos disponibles: Ampleforth, Basis Cash, Empty Set Dollar y Dynamic Set Dollar. No voy a entrar en la historia del sector ni en las particularidades de cada proyecto, no dude en consultar el siguiente artículo de Deribit Insights si necesita ampliar en el contexto:

👉 [Estabilidad, elasticidad y reflexividad: una profunda inmersión en los Stablecoins Algorítmicos](https://insights.deribit.com/market-research/stability-elasticity-and-reflexivity-a-deep-dive-into-algorithmic-stablecoins/)

Así, en lugar de entrar en detalles de cada sistema, voy a dibujar **un croquis presentando los principios fundamentales sobre los que ha sido construída esta generación de stablecoins**, basándome en los parámetros y los enfoques de concepción comúnes a todos los proyectos.

---
### Contrato Intelignete Central

La primera dimensión interesante es la "banca central" del sistema - es decir quien o que puede generar nuevos tokens y bajo que condiciones? **El USDC y el USDT reflejan a grandes trazos un banco central** - una entidad está a cargo del proyecto y de la emisión de nuevos tokens. 

Como Maker no es sino un contrato que permite a sus usuarios la generación de DAI a partir de ciertas garantías, el enfoque es diferente aquí. Principalmente, **Maker/DAI le permite ser su propio banco central**. Por lo que el banco central de Maker es un contrato inteligente, pero necesita de una intervención humana para generar DAI.

Los stablecoins algorítmicos van mucho más lejos, porque **la necesidad humana es retirada del proceso de creación**. En estos sistemas, nadie tiene la capacidad de crear tokens - sólo lo puede hacer el contrato inteligente que los gestiona. Esto es muy elegante y minimalista, pero requiere de un conjunto de incentivos cuidadosamente diseñados para garantizar que los stablecoins acaben acercándose a su valor nominal. Para ser más simple, **con los stablecoins algorítmicos, el banco central es un contrato inteligente.**

### Un ejercito de estabilizadores

Con los stablecoins algorítmicos, sobretodo en sus inicios, las rupturas de los cotejos son frecuentes. Para llevar el establecoin a su punto de anclaje, los protocolos preveen diferentes tipos de incitaciones.

Cuando el valor del stablecoin es superior a un dólar, **el protocolo genera nuevos tokens y los distribuye como incitación** a los usuarios que proveen liquidez o que bloquean sus tokens,lo que contribuye a hacer bajar el precio.

Cuando el stablecoin se negocea por debajo de $1, el sistema de bonos (ou obligaciones) entra en juego: **los usuarios puede destruir sus stablecoins a cambio de un bono** que representa su valor + una prima. En todo caso, sólo lo pueden hacer efectivo una vez que el precio vuelva a ser superior al dólar.

Como puede verlo, en un nivel elevado, estos mecanismos son simples. Contienen sutilezas que debe conocer si quiere participar en el sistema. **Los usuarios que los comprenden y los siguen pueden ayudar el protocolo a estabilizarse**, y si es el caso, pueden ganar dinero en el proceso. Estas sencillas reglas conducen a la emergencia de un ejercito de estabilizadores, quienes utilizan todos los mecanismos para estabilizar el precio: 

Esta concepción lleva la teoría del juego y de la mímica a otro nivel. 

![DSD Meme](/img/2020/algorithmic-stablecoins/dsd-meme.jpeg "Un meme DSD")

### Fase de expansión agresiva

Como el aprovisionamiento en stablecoins algorítmicos es elástico, su mecanismo es puesto a prueba rápidamente. De hecho, al momento del lanzamiento, la oferta circulante de stablecoins generalmente es baja y las interesantes incitaciones crean una fuerte demanda.

Por ejemplo, **Basis Cash se lanzó con 50 000 tokens BAC** distribuídos a los primeros participantes. Luego de un mes, hay **40 millones de BAC en cicrculación**:se generaron porque el BAC se cambiaba por más de un dólar la mayoría del tiempo desde su lanzamiento. Hasta ahora, no ha habido un momento en el que el BAC se negocée a >1$, por lo que el sistema de bonos de la base (BAB) aún no ha sido probado.

{{< notice info >}}
La expansión y la contracción se realizan en los "epochs". El epoch de Basis Cash tiene una duración de 24 horas. ESD de 8 horas y DSD de 2 horas.
{{< /notice >}}

Por el contrario, el ESD y el DSD ya ambos han conocido varios ciclos de expansión y de contracción, el protocolo funciona como previsto:

![DSD Market Cap de los últimos 7 días](/img/2020/algorithmic-stablecoins/dsd-mktcap.png "El Market Cap de DSD muestra claramente las fases de expansión/contracción")

### AProvechamiento de la Composibilidad de DeFi

Otro elemento clave de los stablecoins algorítmicos es la composabilidad. A menudo lo pensamos como "cómo puedo vincular mi producto/servicio terminado con los demás?". Estos proyectos van mucho más lejos, porque **utilizan otros protocolos como Uniswap como parte central de su sistema desde el principio.** Basis, ESD y DSD tienen tres de los componentes principales:

1. Un mecanismo interno de bloqueo/incitación de las fases de expansión (DAO o Boardroom)
2. Un mecanismo de "burn&redeem" para las fases de contracción
3. Un par Uniswap (/USDC ou /DAI)

Su propia estructura demuestra una adaptación de DeFi y de su composabilidad. Poniendo el (los) par(es) Uniswap en el centro del protocolo ayuda de muchas formas - porque **Uniswap es la base que los usuarios de DeFi conocen bien.** 

A pesar de que Uniswap sea el pool principal, la liquidez de otros DEX es cada vez más examinada. Con el lanzamiento de Omakase, Sushi ha integrado dos nuevos pools incitativos de stablecoins algorítmicos: ESD/ETH & DSD/USDC.

La composabilidad es fundamental para los stablecoins algorítmicos y varios proyectos ya toman medidas para integrarse más rápidamente en el ecosistema. En los próximos meses, deberíamos ver las próximas etapas con la llegada de algunos stablecoins algorítmicos como garantía en las plataformas de préstamo.

### Oráculo Minimalista

Los oráculos son utilizados como parametro de base en el sistema algorítmico de los stablecoins: son la **fuente real del precio del stablecoin**. Es primordial asegurarse que el oráculo es seguro y que no puede ser manipulado.

Para esto, la precedente generación de proyectos, en particular Maker, tendía a sobredimensionar la ingeniería. Primeramente, el parámetro de entrada de Maker era casi el precio puro y bruto de ETH. Sin embargo, para volver el sistema menos dependiente de las "liquidaciones fugaces", Maker construyó su propio oráculo, y utiliza varios plazos y promedios del precio de liquidación para **para integrar un tipo de inercia en su sistema**.

Por otro lado, como lo hemos visto anteriormente, nuestros stablecoins tienden a ser minimalistas y a aprovechar la composabilidad de DeFi. **Con sus pares Uniswap, ya tienen una fuente de precios robusta y una liquidez importante, lo que los hace difícil de manipular**. Por lo que el precio Uniswap se toma como base, pero generalmente calculado como un TWAP (Time Weighted Average Price) con el fin de evitar las manipulaciones del precio justo antes de los bajones.

Aunque minimalistas, los sistemas son eficaces y refinados: a medida que los proyectos de stablecoins se desarrollan, sus liquidez en Uniswap deberá aumentar, haciendo el oráculo más robusto y el precio más difícil a manipular. 

Por mi parte, soy entusiasta en cuanto a la dirección que toma este subconjunto del espacio. Que tenga o no la intención de participar en la fase de inicio de estos stablecoins, pienso que es bastante util de documentarse al respecto porque son un buen indicador de las principales tendencias del espacio. 

---

### 🧰 Caja de herramientas para los stablecoins algorítmicos

Antes de terminar, déjeme presentarle algunas herramientas prácticas para seguir la evolución de estos stablecoins. De antemano, cada proyecto tiene su propio rastreador que proporciona las principales medidas de la época actual:

- **[Basis Cash Tools](https://bc.tools/)**
- **[Herramienta de seguimiento de ESD](https://esd.tools/)**
- **[Herramienta de seguimiento de DSD](https://dsd.tools/)**

Finalmente, puede consultar información más detallada sobre el sistema de ESD y de DSD en este cuadro: **[ESD/DSD Bonding](https://duneanalytics.com/tongnk/esd_1)**

### Aviso legal

{{< notice warning >}}
**ESTE ARTÍCULO NO CONSTITUYE UN CONSEJO DE INVERSIÓN.**

No soy un consejero financiero calificado, pero a quien le importa? Si hablamos es de DeFi.
{{< /notice >}}

Me siento legítimo para escribir este artículo porque he seguido de cerca Basis Cash, Empty Set Dollar y Dynamic Set Dollar, como también Basis Dollar & Share menos cuidadosamente. Frax es otro proyecto híbrido que merece ser examinado - No lo he mencionado porque no lo conozco lo suficiente.

{{< notice note >}}
**💰 Bag Disclosure** : Tengo BAC/BAS (Basis Cash), ESD (Empty Set Dollar) y DSD (Dynamic Set Dollar).
{{< /notice >}}

Espero que esta lectura lo haya ilustrado. De ser así, puede **[seguirme en Twitter](https://twitter.com/tokenbrice/)** o en este blog por RSS (abajo toda la información👇)