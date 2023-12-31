# PyHolofotes

PyHolofotes é um programa **Python** para controlar um sistema **Arduino RELE**, injetando pulsos em superfícies para análises térmicas de defeitos não aparentes com uma câmera termográfica. Ele foi implementado no Laboratório de Transferência de Calor da UEMA, proporcionando uma plataforma eficiente e precisa para coleta de dados térmicos.

## Como Baixar e Executar

Para baixar o executável, Cheque `Releases` e procure a versão mais recente do arquivo `.zip` compativel com **seu sistema operacional**. Depois de baixar, **extraia o arquivo** e execute o programa.

## Requisitos

### Do Computador
Antes de executar o programa, **certifique-se** de ter instalado os seguintes pacotes:

- pyserial
- CustomTkinter
- packaging
- pyFirmata

Esses pacotes podem ser instalados usando pip:

```bash
pip install requirements.txt
```

### Do Arduino
O arduino deve ser caregado com o script `arduino_code.ino` para que seja viavel a utilização do código, o carregamento pode ser feito por meio do software **Arduino IDE**.

## Licença

Este projeto está licenciado sob a **licença MIT**. Para mais detalhes, consulte o arquivo `LICENSE`.

## Contribuições

Contribuições são bem-vindas! Se você encontrar algum bug ou tiver uma sugestão de melhoria, por favor, crie uma issue ou envie um pull request (Certifique-se de **rodar os testes** antes de enviar um pull request).

## Prints do Projeto

| SetUp | Configure | About |
| -------- | -------- | -------- |
| ![SetUp](https://i.imgur.com/0AUpqNl.png) | ![Configure](https://i.imgur.com/U2sXa7W.png) | ![About](https://i.imgur.com/TPglUzN.png) |


## Código Fonte

O código fonte deste projeto está disponível no GitHub. Para clonar o repositório, use o seguinte comando:

```bash
git clone git@github.com:Veras-D/PyHolofotes.git
```
