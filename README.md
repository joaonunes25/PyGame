# PyGame

INTEGRANTES DO GRUPO:

Juliana Cunha de Santana
Felipe Correia da Costa
João Marcos Nunes

SOBRE O JOGO:

Ghost Dash é um jogo rítmico em estilo runner, onde você controla um fantasminha que deve atacar inimigos no ritmo da música para salvar seus companheiros capturados por abóboras e morcegos.

COMO JOGAR:

D ou F → Atacar inimigos na zona inferior

J ou K → Atacar inimigos na zona superior

Acerte os inimigos no centro da zona para pontuar mais!

O ataque deve ser feito no tempo certo, sincronizado com a batida da música.

Evite tomar dano e tente terminar a fase com vida para alcançar a vitória.

OBJETIVO:

Derrote todos os inimigos no ritmo da música para alcançar a pontuação máxima. Se sua pontuação for perfeita, você será recompensado com uma tela de SUPREMA VITÓRIA.

RECURSOS DO JOGO:

* Sistema de ritmo baseado em BPM sincronizado com inimigos.

* Animações completas de personagem: parado, pulando, atacando.

* Inimigos com movimentação baseada na música.

* Sistema de pontuação por proximidade ao centro da zona.

* Barra de vida e detecção de colisões.

* Parallax nos fundos para profundidade visual.

* Tela de instruções animada e cenas ilustradas.

ESTRUTURA DE CÓDIGO:

main.py: inicializa o jogo
jogoprincipal.py: controla a lógica principal de fase
player.py: classe do jogador com movimentação, ataque, animação e vida
inimigo.py: classe dos inimigos com movimentação, animação e update
pontuação.py: calcula a pontuação baseada na precisão dos ataques
assets/: armazena imagens, sons e fontes utilizadas no jogo
tela_inicial.py: exibe a tela inicial animada
tela_vitoria.py: exibe a tela de vitória da primeira fase
tela_vitoria_suprema.py: exibe a tela de vitória da segunda fase
tela_game_over: exibe a tela de game over ao perder as fases
tela_instrucoes.py: exibe as instruções de como jogar

COMO EXECUTAR O JOGO:

Clone este repositório e execute o jogo na main.py

OBSERVAÇÕES:

* Se quiser adicionar mais fases, basta editar o dicionário FASES no arquivo jogoprincipal.py.

* O jogo foi planejado para resolução 1280x720.

* Certifique-se de que todos os caminhos das imagens e sons estejam corretos.

