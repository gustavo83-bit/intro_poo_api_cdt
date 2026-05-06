import requests

def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'


    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        return dados
    else:
        return 'Erro na consultar'
    
    print('=Aula de API com Python: Consulta de CEP =')

    meu_cep = (05349000)

    resula = consultar_cep(meu_cep)

    if isinstance(resultado, dict):
        print(f'endereço:{resultado['logradouro']}')
        print(f'bairro:{resultado['bairro']}')
        print(f'cidade{resultado['localidade']}')
        
    

