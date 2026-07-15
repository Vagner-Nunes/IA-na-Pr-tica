[![Python CI Pipeline](https://github.com/Vagner-Nunes/IA-na-Pr-tica/actions/workflows/ci.yml/badge.svg)](https://github.com/Vagner-Nunes/IA-na-Pr-tica/actions/workflows/ci.yml)
# IA-na-Pr-tica
Acelerando o desenvolvimento e garantindo a qualidade com um fluxo de trabalho automotizado por IA
# IA na Prática: Fluxo de Trabalho Automatizado com GitHub Copilot e Actions



## 1. Análise do Problema (Contexto do Desafio)
A nossa empresa fictícia, focada em ferramentas de colaboração online, enfrenta o clássico dilema da engenharia de software: **Velocidade vs. Qualidade**. O crescimento acelerado e a pressão do roadmap geraram quatro gargalos críticos:
* **Desenvolvimento Lento:** Engenheiros gastando tempo precioso em códigos boilerplate e repetitivos.
* **Baixa Cobertura de Testes:** Testes unitários negligenciados por serem vistos como tarefas burocráticas que atrasam as entregas.
* **Ciclo de Feedback Lento:** Bugs descobertos apenas em QA manual ou produção, elevando drasticamente o custo de correção.
* **Inconsistência no Código:** Falta de padronização entre desenvolvedores júniores e plenos, aumentando a dívida técnica.

## 2. O Papel da IA no Ciclo de Desenvolvimento (CI/CD, Testes e Geração)
A Inteligência Artificial Generativa atua como um catalisador no ciclo de vida do software (SDLC):
* **Geração de Código:** Ferramentas como o GitHub Copilot eliminam o atrito inicial, gerando estruturas de classes e algoritmos padrão em segundos, permitindo que o desenvolvedor foque na arquitetura e na regra de negócio.
* **Escrita de Testes:** A IA inverte a percepção de que testar é demorado. Com prompts contextualizados, ela gera cenários de teste de borda (edge cases) que o desenvolvedor poderia esquecer. Como aponta *Martin Fowler*, a cobertura de testes deve focar na qualidade e na confiança que ela traz ao código, e não apenas em atingir uma métrica numérica de 100%.
* **Integração Contínua (CI/CD):** Automatizar a execução desses testes via GitHub Actions garante que nenhum código quebre a aplicação em produção, fornecendo feedback imediato a cada `push`.

## 3. Estudo de Caso Real: AMD (Advanced Micro Devices)
Para embasar a viabilidade da proposta, analisamos o caso real da **AMD**. Ao implementar o GitHub Copilot em suas equipes de software, a empresa registrou uma **redução de até 25% no tempo de desenvolvimento** de novas funcionalidades e uma aceitação massiva dos desenvolvedores, que relataram maior satisfação ao eliminar tarefas repetitivas. Combinado com pipelines de CI/CD automatizados, o tempo de validação de Pull Requests caiu significativamente, garantindo estabilidade nas entregas de software que controlam hardwares complexos.

---

## 4. Estrutura do Projeto Prático
Este repositório contém uma API simples utilizando **Python e Flask** para gerenciar tarefas colaborativas.

* **Tecnologias:** Python 3.10, Flask, Pytest.
* **Assiduidade de IA:** As funções de negócio e testes foram documentadas com os prompts utilizados no Copilot.

[Link para o Vídeo Pitch no YouTube](https://youtu.be/YeQokL-yZZ0)
