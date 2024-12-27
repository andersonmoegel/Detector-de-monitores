

# Monitor Info

Este projeto é uma aplicação simples em Python que exibe informações sobre os monitores conectados ao sistema, incluindo nome, resolução e se o monitor é primário ou secundário.

## Pré-requisitos

Antes de executar o código, você precisa ter o Python instalado em seu sistema, bem como as bibliotecas necessárias. Você pode instalar as bibliotecas usando o `pip`.

### Instalação das Bibliotecas

Execute o seguinte comando no seu terminal para instalar as dependências:

    pip install screeninfo pygetwindow`` 

## Uso

Após instalar as bibliotecas, você pode executar o script Python para obter as informações dos monitores.

### Executando o Código

Salve o código abaixo em um arquivo chamado `monitor_info.py`:

    `enter code here`  `from screeninfo import get_monitors
    import pygetwin
    dow as gw
    def display_monitor_info():
        monitors = get_monitors()
        if monitors:
            print("Informações dos Monitores:")
            for idx, monitor in enumerate(monitors):
                position = "Principal" if monitor.is_primary else "Secundário"
                print(f"Monitor {idx + 1}: {monitor.name} - {monitor.width}x{monitor.height} - {position}")
        else:
            print("Nenhum monitor encontrado.")

# Exibir as informações dos monitores

Em seguida, execute o script:

`python monitor_info.py` 

## Saída Esperada

O script exibirá as informações dos monitores conectados, como no exemplo abaixo:

`Informações dos Monitores:
Monitor 1: Monitor 1 - 1920x1080 - Principal
Monitor 2: Monitor 2 - 1280x1024 - Secundário` 

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Você pode abrir uma issue ou enviar um pull request.


## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
