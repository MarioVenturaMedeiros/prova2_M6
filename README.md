# Introdução

Projeto feito para a prova 2 do Módulo 6 do segundo ano do curso de engenharia da computação. Esse projeto foi feito para dececção de faces em um vídeo utilizando Haar cascade. Ele le o video frame a frame, transforma ele em preto e branco para uma detecção melhor do haar cascade, classifica as imagens utilizando dois classificadores diferentes para aumentar a precisão e, assim que o vídeo acaba, ele fecha o programa. Caso queira ver um vídeo demostrando a solução, [clique aqui](https://youtu.be/fI8aRzsdEok)

# Como rodar

Para rodar o projeto, siga os seguintes passos:

1. Clone o repositório:
    ```bash
    git clone https://github.com/MarioVenturaMedeiros/prova2_M6
    cd prova2_M6
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale os requisitos:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute o script `haar.py`:
    ```bash
    cd src
    python3 haar.py
    ```
# Perguntas técnicas

## Haar cascade

Nessa seção será explicada como o haar cascade funciona.

O haar cascade funciona da seguinte forma: primeiramente ele coletará as haar features, que são calculos que são realizados em regiões retangulares adjacentes presentes em uma janela de detecção. Esses calculos consistem em somar as intensidades dos pixels em cada região e calcular a diferença das somas. Para isso, cria-se imagens integrais para calcular essas haar features, evitando ter que calcular a todo pixel, e sim calculando em áreas menores. Após coletas as haar featues, ele utiliza um método de adaboost para treinar quais features são importantes na classificação. Como esse projeto, como demandado pela PIFA, será utilizado para detecção de faces, as haar features escolhidas seriam somente as que tem algo relacionado a faces. Assim, o classificador é realizado em várias fases, que em cada fase é coletada informações de aprendizado pequenas, que são somadas e ajustadas para que o classificador consiga, utilizando tecnicas de boost, indicar se há uma face (positivo) ou se não há uma face (negativo).

## Escolha do haar cascade

Nessa seção será comparado algorítmos de detecção de faces e o porquê da escolha do haar cascade, baseado em viabilidade técnica, facilidade de implementação e versatilidade da solução.

### Viabilidade técnica

- CNN

- Haar cascade

- Filtro de correlação cruzada

- NN linear

O CNN é o melhor algorítmo que poderia ser ultizado para detecção de faces em vídeos, pois conseguem aprender em base de informações de pixeis, sem requerir uma escolha de features manual ou pré-processamento, além de treinar um modelo muito mais robusto e denso por consimur mais espaço, o que acaba minimizando os erros e sendo mais preciso em suas classificações, assim condinzendo bastante com o que a PIFA requere do projeto.

O haar cascade vem em segundo, pois não tem uma precisão muito boa. Ele consegue identificar faces muito bem e há hiperparâmetros para ajudar a melhorar sua eficiência, mas por ser muito leve não consegue comparar a precisão do CNN.

Filtros de correlação cruzada estão em terceiro pois até conseguem identificar faces em imagens, porém são mais usados para aplicar filtros na imagem, e não detecção em si.

NN linear está em ultimo, pois seu uso em imagens está muito mais voltado a criar imagens do que fazer processamento em imagens existêntes, assim saindo um pouco do escopo trazido pela PIFA.

### Facilidade de implementação

- Haar cascade

- Filtro de correlação cruzada

- CNN

- NN linear

O haar cascade é o algoritmo com uma implementação mais fácil dos comparados, pois já apresenta modelos de identificação de faces prontos e também é muito leve, o que acarreta em uma praticidade muito grande para sua criação e aplicação, já que consegue ser processado de maneira facilitada.

O filtro de correlação cruzada vem em segundo pois sua criação, a pesar de não ser criado para isso, consegue ser razoavelmente fácil, pois por meio de filtros consegue entender onde está presente rostos e onde não estão presentes. Porém, ele não é tão leve e não vai conseguir ser muito produtivo, já que teria que aplicar os filtros em todos os pixels e assim fazer outro processamento para comparar o filtro e identificar as faces, reduzindo sua perfomance na aplicação.

O CNN vem em terceiro, pois a pesar de ser o melhor na detecção de imagens, podendo identificar a cara dos jogadores facilmente, o CNN apresenta um arquivo muito grande e uma fase de coleta de dados para ser criado muito grande, assim deixando o processo de criar ele mais difícil por ter que coletar dados de faces de jogadores, além de ser um arquivo pesado para rodar.

O NN linear está em ultimo, pois a criação em si do NN linear para implementação de detecção de faces de jogadores seria mais complicada, o que deixa complexo a implementação desse modelo. 

## Versatilidade da Solução

- Haar cascade

- CNN

- NN linear

- Filtros de correlação cruzada

O haar cascade é o mais versátil, pois ele é leve de rodar, apresenta vários classificadores para identificação de faces e de objetos em geral e assim sendo muito versátil para conseguir ter uma performance satisfatória na maioria dos casos

O CNN vem em segundo pois ele é muito versátil, conseguindo classificar diversas coisas desde que tenha um banco de dados para isso, mas ele não consegue se apresentar tão útil em qualquer situação por ele ser um programa pesado, então dependendo da aplicação ele não consegue se sair tão bem.

NN linear se apresenta em terceiro, pois mesmo que ele não consiga identificar muito bem coisas em imagens, ele é bem versátil para outras aplicações que não necessáriamente involvem processamento de imagens. Notório afirmar que esse projeto em específico foi desenvolvido para processamento de imagens, mas foi englobado mais usos que só imagens nessa seção.

Filtros de correlação cruzada vem em ultimo, pois mesmo que consiga identificar através de filtros as faces, é provavel que algo mais específico como emoções ele não consiga perfomar de maneira tão efetiva, assim sendo pior em geral. 

## Escolha do haar cascade

Como foi apresentado anteriormente, o haar cascade não é o modelo mais preciso, e com certeza o CNN se sairia melhor para o projeto da PIFA do que o haar cascade, mas como esse projeto foi apresentado para ser realizado em muito pouco tempo, a facilidade da criação do haar cascade foi algo que se demonstrou necessário nesse projeto, além de ainda ter uma performance boa para a classificação de rostos de jogadores. 

Porém, por nãos ser o modelo mais preciso, foram adotadas técnicas para melhorar sua precisão, então foram usados dois modelos de haar cascade (cada um representado por uma cor) e considerado como rosto apenas os que os 2 modelos forem consistentes em considerar que é um rosto, além de ser considerados parâmetros para deixar mais preciso sua claissificação e deixar de ter muitos falsos negativos.

## Detecção de emoções

- CNN

- Haar cascade

- NN linear

- Filtro de correlação cruzada

Para a detecção de emoções, uma nova lista foi criada. Assim, o CNN ficou em primeiro lugar por apresentar uma detecção mais precisa, já que deverão ser considerados detalhes na cara para classificar a emoção, então necessitando de um modelo robusto para conseguir classificar as emoções de maneira correta.

Haar cascade fica em segundo lugar, pois conseguirá identificar emoções, mas de uma maneira menos precisa por apresentar um modelo leve e não tão robusto como o CNN.

NN linear fica em terceiro, pois a pesar de ser uma implementação dificultada na classificação, apresentará resultados rasoáveis em algo específico como detecção de emoções

Filtro de correlação cruzada fica em último, pois o modelo terá muita dificuldade de analizar os detalhes da face dos jogadores, assim tendo uma análise imprecisa das emoções.

## Variações de frame

Pela característica de analizar pixel a pixel, o CNN tem a capacidade de considerar variações de um frame a outro. Sua detecção é feita de maneira detalhada, assim ao identificar pixel a pixel, consegue inferir se em uma parte da imagem a pessoa está feliz, o próximo pixel será inferido que a pessoa estará feliz também.

## Bola de ouro

Juntamente ao projeto, a PIFA desejou que nós adivinhassemos quem seria o ganhador da bola de ouro de 2024. Assim, com base no dataset de 2024 do footbal europeu (pois só dão bola de ouro para quem joga na Europa e o Messi), vimos que tem altas chances do ganhador ser ou do Manchester City ou do Real Madrid. Como o Real Madrid ganhou a champions, foi escolhido um jogador de lá. Sendo assim obviamente Cristiano Ronaldo ganhará a bola de ouro. Brincadeiras a parte, o algorítmo deu seu resultado em Vini Jr, o novo ganhador da bola de ouro.